from typing import Literal, overload

from typing_extensions import Self

from ._base import Node

__all__ = ["HTMLEntity"]

class HTMLEntity(Node):
    def __init__(
        self,
        value: str,
        named: bool | None = ...,
        hexadecimal: bool = ...,
        hex_char: Literal["x", "X"] = ...,
    ) -> None: ...
    @overload
    def __strip__(
        self,
        *,
        normalize: Literal[True],
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str: ...
    @overload
    def __strip__(
        self,
        *,
        normalize: Literal[False],
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> Self: ...
    @overload
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str | Self: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, newval: str) -> None: ...
    @property
    def named(self) -> bool: ...
    @named.setter
    def named(self, newval: bool | None) -> None: ...
    @property
    def hexadecimal(self) -> bool: ...
    @hexadecimal.setter
    def hexadecimal(self, newval: bool) -> None: ...
    @property
    def hex_char(self) -> Literal["x", "X"]: ...
    @hex_char.setter
    def hex_char(self, newval: Literal["x", "X"]) -> None: ...
    def normalize(self) -> str: ...
