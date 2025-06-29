from enum import Enum
from re import Pattern

from .tokens import Token

__all__ = ["Tokenizer"]

class BadRoute(Exception):
    context: int
    def __init__(self, context: int = ...) -> None: ...

class Sentinel(Enum):
    START = 0
    END = 1

class Tokenizer:
    USES_C: bool
    MARKERS: list[str | Sentinel]
    URISCHEME: str
    MAX_DEPTH: int
    regex: Pattern[str]
    tag_splitter: Pattern[str]
    def __init__(self) -> None: ...
    def tokenize(
        self,
        text: str,
        context: int = ...,
        skip_style_tags: bool = ...,
    ) -> list[Token]: ...
