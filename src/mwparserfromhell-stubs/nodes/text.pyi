from ._base import Node

__all__ = ["Text"]

class Text(Node):
    def __init__(self, value: object) -> None: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, newval: object) -> None: ...
