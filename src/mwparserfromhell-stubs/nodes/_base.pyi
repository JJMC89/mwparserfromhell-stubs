from collections.abc import Callable, Generator

from ..string_mixin import StringMixIn
from ..wikicode import Wikicode

__all__ = ["Node"]

class Node(StringMixIn):
    def __children__(self) -> Generator[Wikicode]: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> str | None: ...
    def __showtree__(
        self,
        write: Callable[[*tuple[str, ...]], None],
        get: Callable[[Wikicode], list[str]],
        mark: Callable[[], None],
    ) -> None: ...
