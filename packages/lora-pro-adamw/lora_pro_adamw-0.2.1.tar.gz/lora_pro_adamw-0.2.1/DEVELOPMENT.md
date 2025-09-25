# Development Guide

This document collects maintainer-oriented notes for the `lora-pro-adamw` package.

## Reference Sources

Unit tests depend on the official LoRA-Pro reference implementation being present under
`reference/LoRA-Pro`. Clone it once before running the tests:

```bash
git clone https://github.com/mrflogs/LoRA-Pro.git reference/LoRA-Pro
```

The integration tests shell out to the reference implementation's `lorapro_full_adjustment`
function inside that tree, so make sure the clone is intact when executing the suite.

## Test Suite

The project uses `pytest`, and the configuration lives in `pyproject.toml`.

- Install runtime dependencies (and optionally the `dev` extras).
- Run the tests with `uv run pytest` from the repository root.

This executes:

1. A regression test comparing `LoRAProAdamW` against the official LoRA-Pro math on a toy layer.
2. An integration test that cross-checks behaviour on a PEFT LoRA adapter, with gradients corrected
   using the reference implementation.

## Building Packages

Packaging is handled by Hatch. To build both wheel and sdist:

```bash
uv run hatch build
```

Artifacts are emitted under `dist/`.
