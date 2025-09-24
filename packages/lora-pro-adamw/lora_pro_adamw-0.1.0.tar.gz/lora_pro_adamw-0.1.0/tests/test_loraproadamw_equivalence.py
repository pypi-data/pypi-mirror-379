import copy

import pytest
import torch

from lora_pro import LoRAProAdamW
from .ds_reference import deepspeed_lorapro_adjust
from .minilora import MiniLoRALinear
from lora_pro._lorapro import lorapro_adjust as lorapro_reference_adjust


@pytest.mark.parametrize("layout", ["B@A", "A@B"])
@pytest.mark.parametrize("dtype", [torch.float32])
def test_lorapro_matches_deepspeed(layout: str, dtype: torch.dtype) -> None:
    torch.manual_seed(1234)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    in_features, out_features, rank = 16, 12, 8
    batch = 8

    model_a = MiniLoRALinear(
        in_features, out_features, r=rank, alpha=16, layout=layout, dtype=dtype
    ).to(device)
    model_b = copy.deepcopy(model_a).to(device)

    inputs = torch.randn(batch, in_features, device=device, dtype=dtype)
    targets = torch.randn(batch, out_features, device=device, dtype=dtype)

    def loss_fn(model):
        outputs = model(inputs)
        return torch.nn.functional.mse_loss(outputs, targets)

    opt_a = LoRAProAdamW(
        model_a, lr=1e-3, weight_decay=0.01, betas=(0.9, 0.999), eps=1e-8
    )
    opt_b = torch.optim.AdamW(
        model_b.parameters(), lr=1e-3, weight_decay=0.01, betas=(0.9, 0.999), eps=1e-8
    )

    scale = model_b.lora_alpha / model_b.r
    m_ref = v_ref = None
    m_ds = v_ds = None

    tol = dict(rtol=5e-5, atol=5e-6) if dtype == torch.float32 else dict(rtol=5e-3, atol=5e-3)

    for step in range(2):
        opt_a.zero_grad()
        opt_b.zero_grad()

        loss_a = loss_fn(model_a)
        loss_b = loss_fn(model_b)
        loss_a.backward()
        loss_b.backward()

        if layout == "B@A":
            A_param = model_b.lora_A
            B_param = model_b.lora_B
        else:
            A_param = model_b.lora_B
            B_param = model_b.lora_A
        gA = A_param.grad
        gB = B_param.grad

        ds_gA, ds_gB, m_ds, v_ds = deepspeed_lorapro_adjust(
            A_param.detach().clone(),
            B_param.detach().clone(),
            gA.clone(),
            gB.clone(),
            step=step,
            m=None if m_ds is None else m_ds.clone(),
            v=None if v_ds is None else v_ds.clone(),
        )

        ref_gA = gA.clone()
        ref_gB = gB.clone()
        m_ref, v_ref = lorapro_reference_adjust(
            A_param.detach(),
            B_param.detach(),
            ref_gA,
            ref_gB,
            float(scale),
            step=step,
            m=m_ref,
            v=v_ref,
            betas=(0.9, 0.999),
            eps=1e-8,
        )

        torch.testing.assert_close(ds_gA, ref_gA, **tol)
        torch.testing.assert_close(ds_gB, ref_gB, **tol)
        torch.testing.assert_close(m_ds, m_ref, **tol)
        torch.testing.assert_close(v_ds.float(), v_ref.float(), **tol)

        gA.copy_(ds_gA)
        gB.copy_(ds_gB)

        opt_a.step()
        opt_b.step()

    for (name_a, param_a), (name_b, param_b) in zip(
        model_a.named_parameters(), model_b.named_parameters()
    ):
        torch.testing.assert_close(
            param_a, param_b, **tol, msg=f"parameter mismatch after LoRA-Pro step: {name_a}"
        )
