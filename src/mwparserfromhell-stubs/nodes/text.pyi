from typing_extensions import Self

from ._base import Node

__all__ = ["Text"]

class Text(Node):
    def __init__(self, value: str) -> None: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> Self: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, newval: str) -> None: ...
