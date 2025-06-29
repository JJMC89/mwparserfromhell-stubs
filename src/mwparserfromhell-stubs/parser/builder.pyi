from ..wikicode import Wikicode
from .tokens import Token

__all__ = ["Builder"]

class Builder:
    def __init__(self) -> None: ...
    def build(self, tokenlist: list[Token]) -> Wikicode: ...
