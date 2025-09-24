import torch
from torch import nn


class MiniLoRALinear(nn.Module):
    """Tiny linear layer with a LoRA adapter supporting both A@B and B@A layouts."""

    def __init__(
        self,
        in_features: int,
        out_features: int,
        r: int = 4,
        alpha: float | None = None,
        layout: str = "B@A",
        bias: bool = True,
        dtype: torch.dtype = torch.float32,
    ) -> None:
        super().__init__()
        self.weight = nn.Parameter(torch.empty(out_features, in_features, dtype=dtype))
        nn.init.kaiming_uniform_(self.weight, a=5**0.5)
        self.bias = nn.Parameter(torch.zeros(out_features, dtype=dtype)) if bias else None

        self.r = int(r)
        self.lora_alpha = float(alpha if alpha is not None else r)
        self.layout = layout

        if layout == "A@B":
            self.lora_A = nn.Parameter(torch.randn(out_features, r, dtype=dtype) * 0.02)
            self.lora_B = nn.Parameter(torch.randn(r, in_features, dtype=dtype) * 0.02)
        elif layout == "B@A":
            self.lora_A = nn.Parameter(torch.randn(r, in_features, dtype=dtype) * 0.02)
            self.lora_B = nn.Parameter(torch.randn(out_features, r, dtype=dtype) * 0.02)
        else:
            raise ValueError("layout must be 'A@B' or 'B@A'")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        scale = self.lora_alpha / self.r
        if self.layout == "A@B":
            delta = self.lora_A @ self.lora_B
        else:
            delta = self.lora_B @ self.lora_A
        weight = self.weight + scale * delta
        y = x @ weight.t()
        if self.bias is not None:
            y = y + self.bias
        return y
