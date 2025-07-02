from ..utils import _Parseable
from ..wikicode import Wikicode
from ._base import Node

__all__ = ["ExternalLink"]

class ExternalLink(Node):
    suppress_space: bool
    def __init__(
        self,
        url: _Parseable,
        title: _Parseable = ...,
        brackets: bool = ...,
        suppress_space: bool = ...,
    ) -> None: ...
    @property
    def url(self) -> Wikicode: ...
    @url.setter
    def url(self, value: _Parseable) -> None: ...
    @property  # type: ignore[override]
    def title(self) -> Wikicode | None: ...
    @title.setter
    def title(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        value: _Parseable,
    ) -> None: ...
    @property
    def brackets(self) -> bool: ...
    @brackets.setter
    def brackets(self, value: bool) -> None: ...
