from ..wikicode import Wikicode
from .errors import ParserError as ParserError

__all__ = ["use_c", "Parser", "ParserError"]

use_c: bool

class Parser:
    def __init__(self) -> None: ...
    def parse(
        self,
        text: str,
        context: int = ...,
        skip_style_tags: bool = ...,
    ) -> Wikicode: ...
