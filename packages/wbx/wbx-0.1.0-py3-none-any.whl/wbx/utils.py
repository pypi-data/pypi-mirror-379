from typing import Any


def _is_scalar(x: Any) -> bool:
    return isinstance(x, (str, int, float, bool)) or x is None