from collections.abc import Callable

from typing_extensions import ParamSpec, TypeVar

__all__: list[str] = []

_P = ParamSpec("_P")
_R = TypeVar("_R")

def inheritdoc(method: Callable[_P, _R]) -> Callable[_P, _R]: ...
