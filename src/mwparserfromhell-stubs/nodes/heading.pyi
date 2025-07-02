from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node

class Heading(Node):
    def __init__(self, title: _Parseable, level: int) -> None: ...
    @property  # type: ignore[override]
    def title(self) -> Wikicode: ...
    @title.setter
    def title(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        value: _Parseable,
    ) -> None: ...
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int) -> None: ...
