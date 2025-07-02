from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node

__all__ = ["Wikilink"]

class Wikilink(Node):
    def __init__(self, title: _Parseable, text: _Parseable = ...) -> None: ...
    @property  # type: ignore[override]
    def title(self) -> Wikicode: ...
    @title.setter
    def title(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        value: _Parseable,
    ) -> None: ...
    @property
    def text(self) -> Wikicode | None: ...
    @text.setter
    def text(self, value: _Parseable) -> None: ...
