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
def lorapro_adjust(
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
