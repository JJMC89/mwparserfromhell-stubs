__all__ = ["ParserError"]

class ParserError(Exception):
    def __init__(self, extra: str) -> None: ...
