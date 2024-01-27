from collections.abc import Generator

from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node

__all__ = ["Heading"]

class Heading(Node):
    def __init__(self, title: _Parseable, level: int) -> None: ...
    def __children__(self) -> Generator[Wikicode, None, None]: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str | None: ...
    @property
    def title(self) -> Wikicode: ...
    @title.setter
    def title(self, value: _Parseable) -> None: ...
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int) -> None: ...
