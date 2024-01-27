from re import Match

from ...string_mixin import StringMixIn
from ...utils import _Parseable
from ...wikicode import Wikicode

__all__ = ["Parameter"]

class Parameter(StringMixIn):
    def __init__(
        self,
        name: _Parseable,
        value: _Parseable,
        showkey: bool = ...,
    ) -> None: ...
    @staticmethod
    def can_hide_key(key: object) -> Match[str] | None: ...
    @property
    def name(self) -> Wikicode: ...
    @name.setter
    def name(self, newval: _Parseable) -> None: ...
    @property
    def value(self) -> Wikicode: ...
    @value.setter
    def value(self, newval: _Parseable) -> None: ...
    @property
    def showkey(self) -> bool: ...
    @showkey.setter
    def showkey(self, newval: bool) -> None: ...
