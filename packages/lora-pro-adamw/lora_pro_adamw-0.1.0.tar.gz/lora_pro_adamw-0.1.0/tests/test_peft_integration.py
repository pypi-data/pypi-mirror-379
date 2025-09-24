import copy

import pytest
import torch
from peft import LoraConfig, TaskType, get_peft_model

from lora_pro import LoRAProAdamW
from .ds_reference import deepspeed_lorapro_adjust


class _DummyModel(torch.nn.Module):
    def __init__(self, in_features: int, out_features: int, dtype: torch.dtype) -> None:
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features, bias=False, dtype=dtype)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)


@pytest.mark.parametrize("dtype", [torch.float32])
def test_loraproadamw_matches_peft_reference(dtype: torch.dtype) -> None:
    torch.manual_seed(1234)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    in_features, out_features, rank = 32, 24, 8
    config = LoraConfig(
        task_type=TaskType.FEATURE_EXTRACTION,
        r=rank,
        lora_alpha=16,
        lora_dropout=0.0,
        bias="none",
        target_modules=["linear"],
    )

    base = _DummyModel(in_features, out_features, dtype)
    template = get_peft_model(base, config)

    model_opt = copy.deepcopy(template).to(device)
    model_ref = copy.deepcopy(template).to(device)

    opt_test = LoRAProAdamW(
        model_opt, lr=1e-3, weight_decay=0.0, betas=(0.9, 0.999), eps=1e-8
    )
    opt_ref = torch.optim.AdamW(
        model_ref.parameters(), lr=1e-3, weight_decay=0.0, betas=(0.9, 0.999), eps=1e-8
    )

    moment_states: dict[tuple[str, str], tuple[torch.Tensor | None, torch.Tensor | None]] = {}

    tol = dict(rtol=5e-5, atol=5e-6)

    for step in range(2):
        opt_test.zero_grad()
        opt_ref.zero_grad()
        x = torch.randn(4, in_features, device=device, dtype=dtype)
        target = torch.randn(4, out_features, device=device, dtype=dtype)

        base_opt = model_opt.base_model.model if hasattr(model_opt, "base_model") else model_opt
        base_ref = model_ref.base_model.model if hasattr(model_ref, "base_model") else model_ref

        loss_opt = torch.nn.functional.mse_loss(base_opt(x), target)
        loss_ref = torch.nn.functional.mse_loss(base_ref(x), target)

        loss_opt.backward()
        loss_ref.backward()

        for name, module in model_ref.named_modules():
            if not hasattr(module, "lora_A"):
                continue
            lora_A = getattr(module, "lora_A")
            lora_B = getattr(module, "lora_B")
            if not isinstance(lora_A, torch.nn.ModuleDict):
                continue
            for key in lora_A.keys():
                A_param = lora_A[key].weight
                B_param = lora_B[key].weight
                gA = A_param.grad
                gB = B_param.grad
                state_key = (name, key)
                m, v = moment_states.get(state_key, (None, None))
                ds_gA, ds_gB, m, v = deepspeed_lorapro_adjust(
                    A_param.detach().clone(),
                    B_param.detach().clone(),
                    gA.clone(),
                    gB.clone(),
                    step=step,
                    m=None if m is None else m.clone(),
                    v=None if v is None else v.clone(),
                )
                gA.copy_(ds_gA)
                gB.copy_(ds_gB)
                moment_states[state_key] = (m, v)

        opt_ref.step()
        opt_test.step()

    for (name_a, param_a), (name_b, param_b) in zip(
        model_opt.named_parameters(), model_ref.named_parameters()
    ):
        torch.testing.assert_close(param_a, param_b, **tol, msg=f"Mismatch in {name_a}")
