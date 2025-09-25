import math
from typing import Optional, Tuple

import torch


@torch.no_grad()
def _solve_sylvester(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor) -> torch.Tensor:
    """Solve the Sylvester equation using the DeepSpeed helper formulation."""
    if A.dtype is torch.bfloat16:
        A = A.to(torch.float32)
        B = B.to(torch.float32)
        C = C.to(torch.float32)
    B = -B
    m = B.shape[-1]
    n = A.shape[-1]
    R, U = torch.linalg.eig(A)
    S, V = torch.linalg.eig(B)
    F = torch.linalg.solve(U, (C + 0j) @ V)
    W = R[..., :, None] - S[..., None, :]
    Y = F / W
    X = U[..., :n, :n] @ Y[..., :n, :m] @ torch.linalg.inv(V)[..., :m, :m]
    return X.real if all(torch.isreal(x.flatten()[0]) for x in (A, B, C)) else X


@torch.no_grad()
def lorapro_full_adjustment(
    A: torch.Tensor,
    B: torch.Tensor,
    gA: torch.Tensor,
    gB: torch.Tensor,
    scale: float,
    step: int,
    m: Optional[torch.Tensor],
    v: Optional[torch.Tensor],
    betas: Tuple[float, float],
    eps: float,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Apply the LoRA-Pro gradient corrections as implemented in DeepSpeed."""
    device = gA.device
    dtypeA, dtypeB = A.dtype, B.dtype
    beta1, beta2 = betas
    jitter = 1e-8

    AA_T = A @ A.t()
    B_TB = B.t() @ B
    eye_B = torch.eye(B.shape[0], device=device, dtype=dtypeA)

    AA_T_inv = torch.linalg.pinv(
        AA_T.float() + jitter * torch.eye(AA_T.shape[0], device=device)
    ).to(dtypeA)

    if step == 0:
        grad_A = gA
        grad_B = (gB @ AA_T_inv) / (scale**2)
        B_TB_inv = None
    else:
        B_TB_inv = torch.linalg.pinv(
            B_TB.float() + jitter * torch.eye(B_TB.shape[0], device=device)
        ).to(dtypeA)
        grad_A = (B_TB_inv @ gA) / (scale**2)
        projector = eye_B - B @ B_TB_inv @ B.t()
        grad_B = (projector @ (gB @ AA_T_inv)) / (scale**2)

    equiv_grad = scale * (B @ grad_A + grad_B @ A)

    if m is None:
        m = (1 - beta1) * equiv_grad
    else:
        m.lerp_(equiv_grad, 1 - beta1)

    if v is None:
        v = (1 - beta2) * (equiv_grad * equiv_grad)
    else:
        v.mul_(beta2).addcmul_(
            equiv_grad.to(torch.bfloat16),
            equiv_grad.conj().to(torch.bfloat16),
            value=1 - beta2,
        )

    step_index = step + 1
    bias1 = 1 - beta1**step_index
    bias2 = 1 - beta2**step_index
    denom = (v.float().sqrt() / math.sqrt(bias2)).add_(eps)
    g = (m / bias1) / denom.to(m.dtype)
    g = g.to(dtypeB)

    grad_A_orin = scale * B.t() @ g
    grad_B_orin = scale * g @ A.t()

    if step == 0:
        new_gA = grad_A_orin
        new_gB = (grad_B_orin @ AA_T_inv) / (scale**2)
    else:
        assert B_TB_inv is not None
        rhs = -(B_TB_inv @ grad_A_orin) @ A.t() / (scale**2)
        X = _solve_sylvester(B.t() @ B, A @ A.t(), rhs)
        X = torch.as_tensor(X, device=device, dtype=dtypeB)

        projector = eye_B - B @ B_TB_inv @ B.t()
        new_gA = (B_TB_inv @ grad_A_orin) / (scale**2) + X @ A
        new_gB = (projector @ (grad_B_orin @ AA_T_inv)) / (scale**2) - B @ X

    gA.copy_(new_gA)
    gB.copy_(new_gB)
    return m, v


@torch.no_grad()
def _solve_sylvester_vec(
    SB: torch.Tensor, SA: torch.Tensor, C: torch.Tensor
) -> torch.Tensor:
    """Solve the Sylvester equation SB X + X SA = C using the vec-trick."""

    orig_dtype = C.dtype
    work_dtype = (
        torch.float32 if orig_dtype in (torch.float16, torch.bfloat16) else orig_dtype
    )

    SB_w = SB.to(dtype=work_dtype).contiguous()
    SA_w = SA.to(dtype=work_dtype).contiguous()
    C_w = C.to(dtype=work_dtype).contiguous()

    r = SB_w.shape[0]
    eye = torch.eye(r, device=SB.device, dtype=work_dtype)
    # (I ⊗ SB + SA^T ⊗ I) vec(X) = vec(C)
    K = torch.kron(eye, SB_w) + torch.kron(SA_w.t().contiguous(), eye)
    rhs = C_w.reshape(-1, 1)
    X = torch.linalg.solve(K, rhs).reshape(r, r)
    return X.to(dtype=orig_dtype)


@torch.no_grad()
def lorapro_efficient_adjustment(
    A: torch.Tensor,
    B: torch.Tensor,
    gA: torch.Tensor,
    gB: torch.Tensor,
    scale: float,
    step: int,
    mA: Optional[torch.Tensor],
    vA: Optional[torch.Tensor],
    mB: Optional[torch.Tensor],
    vB: Optional[torch.Tensor],
    betas: Tuple[float, float],
    eps: float,
    solver: str = "vec",
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """LoRA-Pro gradient correction in Efficient mode (Algorithm 2, arXiv v2)."""

    if scale == 0.0:
        raise ValueError("LoRA scale must be non-zero for efficient adjustment.")

    solver_key = solver.lower()
    if solver_key not in ("vec", "eig"):
        raise ValueError("solver must be either 'vec' or 'eig'.")

    beta1, beta2 = betas
    step_index = step + 1
    if step_index <= 0:
        raise ValueError("Step index must be positive.")

    device = A.device
    work_dtype = (
        torch.float32 if A.dtype in (torch.float16, torch.bfloat16) else A.dtype
    )

    A_w = A.to(dtype=work_dtype)
    B_w = B.to(dtype=work_dtype)
    gA_w = gA.to(dtype=work_dtype)
    gB_w = gB.to(dtype=work_dtype)

    r = A_w.shape[0]
    m_dim = B_w.shape[0]

    jitter = 1e-6
    eye_r = torch.eye(r, device=device, dtype=work_dtype)
    eye_m = torch.eye(m_dim, device=device, dtype=work_dtype)

    SB = B_w.t() @ B_w
    SA = A_w @ A_w.t()
    SB_reg = SB + jitter * eye_r
    SA_reg = SA + jitter * eye_r

    inv_SB_gA = torch.linalg.solve(SB_reg, gA_w)
    scale_sq = float(scale) ** 2
    inv_scale_sq = 1.0 / scale_sq

    C = -inv_SB_gA @ A_w.t() * inv_scale_sq
    if solver_key == "vec":
        X = _solve_sylvester_vec(SB_reg, SA_reg, C)
    else:
        X = _solve_sylvester(SB_reg, SA_reg, C)
        X = torch.as_tensor(X, device=device, dtype=work_dtype)
    gA_adj = inv_SB_gA * inv_scale_sq + X @ A_w

    inv_SB_BT = torch.linalg.solve(SB_reg, B_w.t())
    projector = eye_m - B_w @ inv_SB_BT
    SA_inv = torch.linalg.solve(SA_reg, eye_r)
    gB_adj = projector @ (gB_w @ SA_inv) * inv_scale_sq - B_w @ X

    # Adam moments on low-rank factors
    gA_state = gA_adj.to(dtype=A.dtype)
    gB_state = gB_adj.to(dtype=B.dtype)

    if mA is None:
        mA = torch.zeros_like(gA_state)
    if vA is None:
        vA = torch.zeros_like(gA_state)
    if mB is None:
        mB = torch.zeros_like(gB_state)
    if vB is None:
        vB = torch.zeros_like(gB_state)

    mA.mul_(beta1).add_(gA_state, alpha=1 - beta1)
    vA.mul_(beta2).addcmul_(gA_state, gA_state, value=1 - beta2)
    mB.mul_(beta1).add_(gB_state, alpha=1 - beta1)
    vB.mul_(beta2).addcmul_(gB_state, gB_state, value=1 - beta2)

    bias1 = 1 - beta1**step_index
    bias2 = 1 - beta2**step_index

    mA_hat = mA.float() / bias1
    vA_hat = vA.float() / bias2
    mB_hat = mB.float() / bias1
    vB_hat = vB.float() / bias2

    upd_A = (mA_hat / (vA_hat.sqrt() + eps)).to(dtype=gA.dtype)
    upd_B = (mB_hat / (vB_hat.sqrt() + eps)).to(dtype=gB.dtype)

    gA.copy_(upd_A)
    gB.copy_(upd_B)

    return mA, vA, mB, vB
