from typing import Literal

from ._base import Node

__all__ = ["HTMLEntity"]

class HTMLEntity(Node):
    def __init__(
        self,
        value: object,
        named: bool | None = ...,
        hexadecimal: bool = ...,
        hex_char: Literal["x", "X"] = ...,
    ) -> None: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, newval: object) -> None: ...
    @property
    def named(self) -> bool: ...
    @named.setter
    def named(self, newval: bool) -> None: ...
    @property
    def hexadecimal(self) -> bool: ...
    @hexadecimal.setter
    def hexadecimal(self, newval: bool) -> None: ...
    @property
    def hex_char(self) -> Literal["x", "X"]: ...
    @hex_char.setter
    def hex_char(self, newval: Literal["x", "X"]) -> None: ...
    def normalize(self) -> str: ...
