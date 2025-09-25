# LoRA-Pro AdamW

A lightweight Python package that ships a standalone implementation of the **LoRA-Pro** gradient
correction for low-rank adapters together with an AdamW optimizer wrapper. The implementation is a
clean-room port of the original [LoRA-Pro DeepSpeed integration](reference/LoRA-Pro/DeepSpeed-0.15.1/deepspeed/runtime/zero/stage_1_and_2.py)
and is compatible with both plain PyTorch modules and [PEFT](https://github.com/huggingface/peft) LoRA layers.

## Features

- Detects LoRA pairs (`lora_A`, `lora_B`) on vanilla modules or PEFT `ModuleDict` layouts automatically.
- Applies the exact LoRA-Pro closed-form gradient correction before taking an AdamW step.
- Matches the upstream DeepSpeed implementation bit-for-bit in the provided regression tests.
- Ships with pytest-based guards, including an integration test that cross-checks against the DeepSpeed implementation on PEFT adapters.

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
LoRA-Pro gradient correction before delegating to AdamW.

## Acknowledgements & Citation

This package reuses the LoRA-Pro mathematics introduced in:

- **Original implementation:** [mrflogs/LoRA-Pro](https://github.com/mrflogs/LoRA-Pro)
- **Paper:** Zhengbo Wang, Jian Liang, Ran He, Zilei Wang, Tieniu Tan. *LoRA-Pro: Are Low-Rank Adapters Properly Optimized?* ICLR 2025. [[OpenReview]](https://openreview.net/forum?id=gTwRMU3lJ5)

Please cite the paper above when using this optimizer in your research.

## License

Released under the [MIT License](LICENSE).
