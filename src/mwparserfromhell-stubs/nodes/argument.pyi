from collections.abc import Generator

from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node

__all__ = ["Argument"]

class Argument(Node):
    def __init__(self, name: _Parseable, default: _Parseable = ...) -> None: ...
    def __children__(self) -> Generator[Wikicode, None, None]: ...
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
    def default(self) -> Wikicode | None: ...
    @default.setter
    def default(self, default: _Parseable) -> None: ...
