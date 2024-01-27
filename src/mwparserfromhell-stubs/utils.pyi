from collections.abc import Iterable

from _typeshed import SupportsRead
from typing_extensions import TypeAlias

from .nodes import Node
from .wikicode import Wikicode

__all__ = ["parse_anything"]

_Parseable: TypeAlias = (
    bytes
    | int
    | str
    | Node
    | Wikicode
    | SupportsRead[bytes | str]
    | Iterable[bytes | int | str | Node | Wikicode | SupportsRead[bytes | str] | None]
    | None
)

def parse_anything(
    value: _Parseable,
    context: int = ...,
    *,
    skip_style_tags: bool = ...,
) -> Wikicode: ...
