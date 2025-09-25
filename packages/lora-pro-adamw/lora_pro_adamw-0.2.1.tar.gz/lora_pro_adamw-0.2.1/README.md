# LoRA-Pro AdamW

A lightweight Python package that ships a standalone implementation of the **LoRA-Pro** gradient
correction for low-rank adapters together with an AdamW optimizer wrapper. The implementation is a
clean-room port of the official [LoRA-Pro reference optimizer](https://github.com/mrflogs/LoRA-Pro)
and is compatible with both plain PyTorch modules and [PEFT](https://github.com/huggingface/peft) LoRA layers.

## Features

- Detects LoRA pairs (`lora_A`, `lora_B`) on vanilla modules or PEFT `ModuleDict` layouts automatically.
- Applies the exact LoRA-Pro closed-form gradient correction before taking an AdamW step.
- Supports both the original "full" mode (mathematically identical to the official LoRA-Pro release) and the new "efficient" mode with a vectorized Sylvester solver.
- Matches the upstream LoRA-Pro reference implementation bit-for-bit in the provided regression tests.
- Ships with pytest-based guards, including an integration test that cross-checks against the official reference implementation on PEFT adapters.

## Installation

```bash
pip install lora-pro-adamw
```

## Quick Start

```python
import torch
from peft import LoraConfig, TaskType, get_peft_model
from lora_pro import LoRAProAdamW


class Toy(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear = torch.nn.Linear(32, 24, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)


config = LoraConfig(
    task_type=TaskType.FEATURE_EXTRACTION,
    target_modules=["linear"],
    r=8,
    lora_alpha=16,
    lora_dropout=0.0,
    bias="none",
)
model = get_peft_model(Toy(), config)
# LoRAProAdamW wraps AdamW and performs the LoRA-Pro gradient correction internally.
# Unlike a vanilla torch.optim optimizer, instantiate it with the *model*, not parameter groups.
optimizer = LoRAProAdamW(model, lr=1e-3, weight_decay=0.0)

inputs = torch.randn(4, 32)
target = torch.randn(4, 24)
loss = torch.nn.functional.mse_loss(model(inputs), target)
loss.backward()
optimizer.step()
optimizer.zero_grad()
```

The optimizer automatically discovers LoRA parameters on the PEFT-wrapped modules and applies the
LoRA-Pro gradient correction before delegating to AdamW. By default, the optimizer runs in "full"
mode, reproducing the official LoRA-Pro implementation exactly. To trade a tiny amount of numerical
difference for significantly lower solver cost, switch to the efficient solver mode:

```python
optimizer = LoRAProAdamW(
    model,
    lr=1e-3,
    weight_decay=0.0,
    lorapro_mode="efficient",      # use vec-trick Sylvester solver
    efficient_solver="vec",        # or "eig" for the eigendecomposition variant
)
```

State dicts include the chosen mode and solver so checkpoints remain compatible with your selected
configuration.

## Acknowledgements & Citation

This package reuses the LoRA-Pro mathematics introduced in the official reference implementation:

- **Reference optimizer:** [mrflogs/LoRA-Pro](https://github.com/mrflogs/LoRA-Pro)
- **Paper:** Zhengbo Wang, Jian Liang, Ran He, Zilei Wang, Tieniu Tan. *LoRA-Pro: Are Low-Rank Adapters Properly Optimized?* ICLR 2025. [[OpenReview]](https://openreview.net/forum?id=gTwRMU3lJ5)

Please cite the paper above when using this optimizer in your research.

## License

Released under the [MIT License](LICENSE).
