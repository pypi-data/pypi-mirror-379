import ast
import textwrap
from functools import lru_cache
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, Tuple

import torch

DS_SOURCE = Path(__file__).resolve().parent.parent / "reference" / "LoRA-Pro" / "DeepSpeed-0.15.1" / "deepspeed" / "runtime" / "zero" / "stage_1_and_2.py"


def _extract_function_source(tree: ast.AST, source: str, predicate) -> str:
    for node in ast.walk(tree):
        if predicate(node):
            segment = ast.get_source_segment(source, node)
            if segment is None:
                continue
            return textwrap.dedent(segment)
    raise RuntimeError("Requested function not found in DeepSpeed source")


@lru_cache(None)
def _load_deepspeed_lorapro():
    source = DS_SOURCE.read_text()
    tree = ast.parse(source)

    solve_src = _extract_function_source(
        tree,
        source,
        lambda n: isinstance(n, ast.FunctionDef) and n.name == "solve_sylvester",
    )

    # Locate the method definition inside the DeepSpeedZeroOptimizer class
    lorapro_src = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "DeepSpeedZeroOptimizer":
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "lorapro_full_adjustment":
                    lorapro_src = textwrap.dedent(ast.get_source_segment(source, item))
                    break
        if lorapro_src is not None:
            break
    if lorapro_src is None:
        raise RuntimeError("DeepSpeed lorapro_full_adjustment not found")

    namespace = {"torch": torch}
    exec(solve_src, namespace)
    exec(lorapro_src, namespace)
    return namespace["lorapro_full_adjustment"]


def deepspeed_lorapro_adjust(
    A: torch.Tensor,
    B: torch.Tensor,
    gA: torch.Tensor,
    gB: torch.Tensor,
    step: int,
    m: Optional[torch.Tensor],
    v: Optional[torch.Tensor],
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """Run the exact DeepSpeed lorapro_full_adjustment on standalone tensors.

    Returns the corrected gradients for (A, B) along with updated Adam moments.
    """
    lorapro = _load_deepspeed_lorapro()

    shim = SimpleNamespace()
    shim.averaged_gradients = {0: [gA, gB]}
    shim.params_in_partition = {0: [A, B]}
    shim.global_step = step
    shim.exp_avg = {} if m is None else {0: m}
    shim.exp_avg_sq = {} if v is None else {0: v}

    lorapro(shim, 0)

    new_gA = shim.averaged_gradients[0][0].clone()
    new_gB = shim.averaged_gradients[0][1].clone()
    new_m = shim.exp_avg[0].clone()
    new_v = shim.exp_avg_sq[0].clone()
    return new_gA, new_gB, new_m, new_v
