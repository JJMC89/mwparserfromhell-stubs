from collections.abc import Generator

from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node

__all__ = ["Wikilink"]

class Wikilink(Node):
    def __init__(self, title: _Parseable, text: _Parseable = ...) -> None: ...
    def __children__(self) -> Generator[Wikicode, None, None]: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str: ...
    @property
    def title(self) -> Wikicode: ...
    @title.setter
    def title(self, value: _Parseable) -> None: ...
    @property
    def text(self) -> Wikicode: ...
    @text.setter
    def text(self, value: _Parseable) -> None: ...
