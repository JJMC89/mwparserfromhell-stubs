from collections.abc import Generator
from typing import Literal, TypeVar, overload

from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node
from .extras import Parameter

__all__ = ["Template"]

_T = TypeVar("_T")

class Template(Node):
    def __init__(self, name: _Parseable, params: _Parseable = ...) -> None: ...
    def __children__(self) -> Generator[Wikicode, None, None]: ...
    @overload
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: Literal[True],
    ) -> str: ...
    @overload
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: Literal[False],
    ) -> None: ...
    @overload
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str | None: ...
    @property
    def name(self) -> Wikicode: ...
    @name.setter
    def name(self, value: _Parseable) -> None: ...
    @property
    def params(self) -> list[Parameter]: ...
    def has(self, name: object, ignore_empty: bool = ...) -> bool: ...
    has_param = has
    def get(self, name: object, default: _T = ...) -> Parameter | _T: ...
    def __getitem__(self, name: object) -> Parameter: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def add(
        self,
        name: _Parseable,
        value: _Parseable,
        showkey: bool | None = ...,
        before: Parameter | _Parseable = ...,
        preserve_spacing: bool = ...,
    ) -> Parameter: ...
    def __setitem__(self, name: _Parseable, value: _Parseable) -> None: ...
    def remove(self, param: Parameter | object, keep_field: bool = ...) -> None: ...
    def __delitem__(self, param: Parameter | object) -> None: ...
