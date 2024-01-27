from collections.abc import Callable, Generator

from typing_extensions import Self

from ..string_mixin import StringMixIn
from ..wikicode import Wikicode

__all__ = ["Node"]

class Node(StringMixIn):
    def __children__(self) -> Generator[Wikicode | None, None, None]: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str | Self | None: ...
    def __showtree__(
        self,
        write: Callable[..., None],
        get: Callable[[Wikicode], list[str]],
        mark: object,
    ) -> None: ...
