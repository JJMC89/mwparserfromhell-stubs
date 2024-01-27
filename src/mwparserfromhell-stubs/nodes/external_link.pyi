from collections.abc import Generator

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
    def __children__(self) -> Generator[Wikicode, None, None]: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str | None: ...
    @property
    def url(self) -> Wikicode: ...
    @url.setter
    def url(self, value: _Parseable) -> None: ...
    @property
    def title(self) -> Wikicode | None: ...
    @title.setter
    def title(self, value: _Parseable) -> None: ...
    @property
    def brackets(self) -> bool: ...
    @brackets.setter
    def brackets(self, value: bool) -> None: ...
