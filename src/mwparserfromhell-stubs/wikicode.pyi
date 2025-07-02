from collections.abc import Callable, Generator, Iterable
from enum import Enum
from re import RegexFlag
from typing import Literal, TypeVar, overload

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

class Recurse(Enum):
    RECURSE_OTHERS = 2

class Wikicode(StringMixIn):
    RECURSE_OTHERS = Recurse.RECURSE_OTHERS
    def __init__(self, nodes: list[Node]) -> None: ...
    @property
    def nodes(self) -> SmartList[Node]: ...
    @nodes.setter
    def nodes(self, value: list[Node] | _Parseable) -> None: ...
    @overload
    def get(self, index: int) -> Node: ...
    @overload
    def get(self, index: slice) -> list[Node]: ...
    @overload
    def get(self, index: int | slice) -> Node | list[Node]: ...
    def set(self, index: int, value: _Parseable) -> None: ...
    def contains(self, obj: str | Node | Wikicode) -> bool: ...
    def index(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        obj: str | Node | Wikicode,
        recursive: bool = ...,
    ) -> int: ...
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
    def replace(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
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
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[_NodeT], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: type[_NodeT],
    ) -> Generator[_NodeT]: ...
    @overload
    def ifilter(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[_NodeT], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: tuple[type[_NodeT], ...],
    ) -> Generator[_NodeT]: ...
    @overload
    def ifilter(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        forcetype: None = ...,
    ) -> Generator[Node]: ...
    def ifilter_arguments(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Argument], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Argument]: ...
    def ifilter_comments(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Comment], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Comment]: ...
    def ifilter_external_links(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[ExternalLink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[ExternalLink]: ...
    def ifilter_headings(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Heading], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Heading]: ...
    def ifilter_html_entities(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[HTMLEntity], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[HTMLEntity]: ...
    def ifilter_tags(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Tag], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Tag]: ...
    def ifilter_templates(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Template], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Template]: ...
    def ifilter_text(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Text], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Text]: ...
    def ifilter_wikilinks(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Wikilink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> Generator[Wikilink]: ...
    @overload
    def filter(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: type[_NodeT],
    ) -> list[_NodeT]: ...
    @overload  # pyright only
    def filter(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[_NodeT], bool] | None = ...,
        flags: int | RegexFlag = ...,
        *,
        forcetype: tuple[type[_NodeT], ...],
    ) -> list[_NodeT]: ...
    @overload
    def filter(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Node], bool] | None = ...,
        flags: int | RegexFlag = ...,
        forcetype: None = ...,
    ) -> list[Node]: ...
    def filter_arguments(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Argument], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Argument]: ...
    def filter_comments(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Comment], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Comment]: ...
    def filter_external_links(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[ExternalLink], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[ExternalLink]: ...
    def filter_headings(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Heading], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Heading]: ...
    def filter_html_entities(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[HTMLEntity], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[HTMLEntity]: ...
    def filter_tags(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Tag], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Tag]: ...
    def filter_templates(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Template], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Template]: ...
    def filter_text(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
        matches: str | Callable[[Text], bool] | None = ...,
        flags: int | RegexFlag = ...,
    ) -> list[Text]: ...
    def filter_wikilinks(
        self,
        recursive: bool | Literal[Recurse.RECURSE_OTHERS] = ...,
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
