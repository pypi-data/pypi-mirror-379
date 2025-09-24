# lora_pro_adamw.py
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import torch
from torch import nn
from torch.optim import AdamW, Optimizer

from ._lorapro import lorapro_adjust

# -------- utilities --------


@dataclass
class _Pair:
    A: nn.Parameter
    B: nn.Parameter
    Wshape: Tuple[int, int]  # (out, in) expected full weight shape
    s: float  # alpha / r
    layout: str  # "A@B" or "B@A"


# -------- main optimizer --------


class LoRAProAdamW(Optimizer):
    """
    AdamW + LoRA-Pro gradient correction.

    Usage:
        opt = LoRAProAdamW(
            model,
            lr=1e-4, weight_decay=0.01,
            betas=(0.9, 0.999), eps=1e-8,
            find_peft=True   # try PEFT-style modules too
        )
        ...
        loss.backward()
        opt.step()
        opt.zero_grad()

    Auto-discovery rules (per module):
      - expects attributes 'lora_A' and 'lora_B' (nn.Parameter or nn.Module with .weight)
      - optional: 'lora_alpha' or 'alpha'; 'r' or 'lora_r'
      - layout:
          * if module has .weight (Linear/Conv1D-like), we infer layout so that (delta W) matches .weight.shape
          * else default to "B@A" (PEFT’s usual delta W = s * (B @ A))
    """

    def __init__(
        self,
        model: nn.Module,
        lr: float = 1e-4,
        weight_decay: float = 0.01,
        betas: Tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-8,
        find_peft: bool = True,
    ):
        self.model = model
        self.betas = betas
        self.eps = eps
        self._step = 0

        # discover all params (base AdamW over all model params)
        base_params = list(model.parameters())
        self._base = AdamW(
            base_params, lr=lr, weight_decay=weight_decay, betas=betas, eps=eps
        )

        # collect LoRA A/B pairs
        self._pairs: List[_Pair] = self._find_lora_pairs(model, find_peft=find_peft)
        if len(self._pairs) == 0:
            raise RuntimeError(
                "LoRAProAdamW: no (lora_A, lora_B) pairs found on the model."
            )

        # state for Adam-on-G_eq per pair-id
        self._state_m: Dict[int, torch.Tensor] = {}
        self._state_v: Dict[int, torch.Tensor] = {}

        # make this class look like a torch Optimizer for external tooling
        self.param_groups = self._base.param_groups
        self.defaults = self._base.defaults

    # ----- Optimizer API passthrough -----

    def zero_grad(self, set_to_none: bool = True):
        self._base.zero_grad(set_to_none=set_to_none)

    def state_dict(self):
        return {
            "base": self._base.state_dict(),
            "step": self._step,
            "m": {k: v.detach().cpu() for k, v in self._state_m.items()},
            "v": {k: v.detach().cpu() for k, v in self._state_v.items()},
        }

    def load_state_dict(self, state_dict):
        if "base" in state_dict:
            self._base.load_state_dict(state_dict["base"])
        self._step = int(state_dict.get("step", 0))
        m = state_dict.get("m", {})
        v = state_dict.get("v", {})
        # rebuild on the right device/dtype lazily on next step

        self._state_m = {
            int(k): t.to(self._pairs[int(k)].A.device).to(self._pairs[int(k)].A.dtype)
            for k, t in m.items()
        }

        # keep v potentially in lower precision
        def _vdtype(tref):
            return (
                torch.bfloat16
                if tref.dtype in (torch.float16, torch.bfloat16)
                else tref.dtype
            )

        self._state_v = {
            int(k): t.to(self._pairs[int(k)].A.device).to(
                _vdtype(self._pairs[int(k)].A)
            )
            for k, t in v.items()
        }

    @torch.no_grad()
    def step(self, closure: Optional[callable] = None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        # 1) LoRA-Pro correction per pair (overwrite A.grad/B.grad in-place)
        for idx, p in enumerate(self._pairs):
            if p.A.grad is None or p.B.grad is None:
                continue
            self._adjust_pair(idx, p)

        # 2) Base AdamW step
        self._base.step()
        self._step += 1
        return loss

    # ----- internals -----

    def _get_attr_param(self, obj, name: str) -> Optional[nn.Parameter]:
        if hasattr(obj, name):
            v = getattr(obj, name)
            if isinstance(v, nn.Parameter):
                return v
            if isinstance(v, nn.Module):
                if hasattr(v, "weight") and isinstance(v.weight, nn.Parameter):
                    return v.weight
                if isinstance(v, nn.ModuleDict):
                    for key in ("default", *v.keys()):
                        if key in v:
                            sub = v[key]
                            if hasattr(sub, "weight") and isinstance(sub.weight, nn.Parameter):
                                return sub.weight
            if isinstance(v, dict):
                for key in ("default", *v.keys()):
                    if key in v:
                        sub = v[key]
                        if isinstance(sub, nn.Parameter):
                            return sub
                        if (
                            isinstance(sub, nn.Module)
                            and hasattr(sub, "weight")
                            and isinstance(sub.weight, nn.Parameter)
                        ):
                            return sub.weight
        return None

    def _extract_scalar(self, value) -> Optional[float]:
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, torch.Tensor):
            return float(value.item())
        if isinstance(value, dict):
            for key in ("default", *value.keys()):
                if key in value:
                    return self._extract_scalar(value[key])
        return None

    def _infer_layout(
        self, module: nn.Module, A: nn.Parameter, B: nn.Parameter
    ) -> Tuple[str, Tuple[int, int]]:
        # Try to match module.weight shape if present (Linear-like)
        if (
            hasattr(module, "weight")
            and isinstance(module.weight, nn.Parameter)
            and module.weight.ndim == 2
        ):
            out_in = module.weight.shape  # (out, in)
            # candidates
            c1 = (
                (A @ B)
                if A.dim() == 2 and B.dim() == 2 and A.shape[1] == B.shape[0]
                else None
            )
            c2 = (
                (B @ A)
                if B.dim() == 2 and A.dim() == 2 and B.shape[1] == A.shape[0]
                else None
            )
            if c1 is not None and c1.shape == out_in:
                return "A@B", out_in
            if c2 is not None and c2.shape == out_in:
                return "B@A", out_in

        # Default to PEFT-style delta W = B @ A
        if B.dim() == 2 and A.dim() == 2:
            try:
                test = B @ A
                return "B@A", (test.shape[0], test.shape[1])
            except Exception:
                pass
        # Fallback: try A@B
        if A.dim() == 2 and B.dim() == 2:
            test = A @ B
            return "A@B", (test.shape[0], test.shape[1])
        raise ValueError("Cannot infer layout for LoRA A/B shapes.")

    def _find_lora_pairs(self, model: nn.Module, find_peft: bool) -> List[_Pair]:
        pairs: List[_Pair] = []
        for m in model.modules():
            A = self._get_attr_param(m, "lora_A")
            B = self._get_attr_param(m, "lora_B")
            if A is None or B is None:
                # also try common PEFT internal names
                if not find_peft:
                    continue
                A = A or self._get_attr_param(m, "lora_A_default")  # some forks
                B = B or self._get_attr_param(m, "lora_B_default")
                if A is None or B is None:
                    continue

            # alpha / r
            alpha = self._extract_scalar(getattr(m, "lora_alpha", None))
            if alpha is None:
                alpha = self._extract_scalar(getattr(m, "alpha", None))
            r_attr = getattr(m, "r", None)
            if isinstance(r_attr, dict):
                r = self._extract_scalar(r_attr)
            else:
                r = self._extract_scalar(r_attr)
            if r is None:
                r = self._extract_scalar(getattr(m, "lora_r", None))
            if r is None:
                # infer rank from the shared inner dim
                if A.dim() == 2 and B.dim() == 2:
                    r = min(A.shape[1], B.shape[0])
                else:
                    raise ValueError(
                        "Cannot infer LoRA rank; please add attribute 'r' to your module."
                    )
            if alpha is None:
                alpha = float(r)

            layout, wshape = self._infer_layout(m, A, B)
            s = float(alpha) / float(r)
            pairs.append(_Pair(A=A, B=B, Wshape=wshape, s=s, layout=layout))
        return pairs

    @torch.no_grad()
    def _adjust_pair(self, pid: int, p: _Pair):
        """
        Apply LoRA-Pro closed forms to grads of A,B.
        Supports both layouts: deltaW = s*(A@B) or s*(B@A).
        Internally we normalize to use symbols so that:
          - if layout == "A@B": treat A:(out,r), B:(r,in)
          - if layout == "B@A": treat (rename) A2 = B, B2 = A so shapes align
        """
        if p.A.grad is None or p.B.grad is None:
            return

        if p.layout == "B@A":
            A, B = p.A, p.B
            gA, gB = p.A.grad, p.B.grad
        else:
            # swap to match DeepSpeed convention
            A, B = p.B, p.A
            gA, gB = p.B.grad, p.A.grad

        m = self._state_m.get(pid)
        v = self._state_v.get(pid)

        m, v = lorapro_adjust(
            A.detach(),
            B.detach(),
            gA,
            gB,
            p.s,
            self._step,
            m,
            v,
            self.betas,
            self.eps,
        )

        self._state_m[pid] = m
        self._state_v[pid] = v
