from collections.abc import Callable, Generator, Iterable
from re import RegexFlag
from typing import TypeVar, overload

from .nodes import (
    Argument,
    Comment,
    ExternalLink,
    Heading,
    HTMLEntity,
    Node,
    Tag,
    Template,
    Text,
    Wikilink,
)
from .smart_list import SmartList
from .string_mixin import StringMixIn
from .utils import _Parseable

__all__ = ["Wikicode"]

_NodeT = TypeVar("_NodeT", bound=Node)

class Wikicode(StringMixIn):
    RECURSE_OTHERS: int = 2
    def __init__(self, nodes: list[Node]) -> None: ...
    @property
    def nodes(self) -> SmartList[Node]: ...
    @nodes.setter
    def nodes(self, value: _Parseable) -> None: ...
    def get(self, index: int) -> Node: ...
    def set(self, index: int, value: _Parseable) -> None: ...
    def contains(self, obj: object) -> bool: ...
    def index(self, obj: object, recursive: bool = ...) -> int: ...
    def get_ancestors(self, obj: Node | Wikicode) -> list[Node]: ...
    def get_parent(self, obj: Node | Wikicode) -> Node | None: ...
    def insert(self, index: int, value: _Parseable) -> None: ...
    def insert_before(
        self,
        obj: str | Node | Wikicode,
        value: _Parseable,
        recursive: bool = ...,
    ) -> None: ...
    def insert_after(
        self,
        obj: str | Node | Wikicode,
        value: _Parseable,
        recursive: bool = ...,
    ) -> None: ...
    def replace(
        self,
        obj: str | Node | Wikicode,
        value: _Parseable,
        recursive: bool = ...,
    ) -> None: ...
    def append(self, value: _Parseable) -> None: ...
    def remove(self, obj: str | Node | Wikicode, recursive: bool = ...) -> None: ...
    def matches(
        self,
        other: bytes | str | Node | Wikicode | Iterable[bytes | str | Node | Wikicode],
    ) -> bool: ...
    @overload
    def ifilter(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[_NodeT], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: type[_NodeT],
    ) -> Generator[_NodeT, None, None]: ...
    @overload  # pyright only
    def ifilter(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[_NodeT], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: tuple[type[_NodeT], ...],
    ) -> Generator[_NodeT, None, None]: ...
    @overload
    def ifilter(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        forcetype: None = ...,
    ) -> Generator[Node, None, None]: ...
    @overload
    def filter(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: type[_NodeT],
    ) -> list[_NodeT]: ...
    @overload  # pyright only
    def filter(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[_NodeT], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: tuple[type[_NodeT], ...],
    ) -> list[_NodeT]: ...
    @overload
    def filter(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        forcetype: None = ...,
    ) -> list[Node]: ...
    def ifilter_arguments(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Argument], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Argument, None, None]: ...
    def filter_arguments(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Argument], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Argument]: ...
    def ifilter_comments(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Comment], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Comment, None, None]: ...
    def filter_comments(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Comment], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Comment]: ...
    def ifilter_external_links(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[ExternalLink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[ExternalLink, None, None]: ...
    def filter_external_links(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[ExternalLink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[ExternalLink]: ...
    def ifilter_headings(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Heading], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Heading, None, None]: ...
    def filter_headings(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Heading], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Heading]: ...
    def ifilter_html_entities(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[HTMLEntity], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[HTMLEntity, None, None]: ...
    def filter_html_entities(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[HTMLEntity], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[HTMLEntity]: ...
    def ifilter_tags(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Tag], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Tag, None, None]: ...
    def filter_tags(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Tag], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Tag]: ...
    def ifilter_templates(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Template], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Template, None, None]: ...
    def filter_templates(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Template], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Template]: ...
    def ifilter_text(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Text], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Text, None, None]: ...
    def filter_text(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Text], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Text]: ...
    def ifilter_wikilinks(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Wikilink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Wikilink, None, None]: ...
    def filter_wikilinks(
        self,
        recursive: bool | int = ...,
        matches: str | Callable[[Wikilink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Wikilink]: ...
    def get_sections(
        self,
        levels: Iterable[int] | None = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        flat: bool = ...,
        include_lead: bool | None = ...,
        include_headings: bool = ...,
    ) -> list[Wikicode]: ...
    def strip_code(
        self,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str: ...
    def get_tree(self) -> str: ...
