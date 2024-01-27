from ._base import Node

__all__ = ["Comment"]

class Comment(Node):
    def __init__(self, contents: object) -> None: ...
    def __strip__(
        self,
        *,
        normalize: bool = ...,
        collapse: bool = ...,
        keep_template_params: bool = ...,
    ) -> None: ...
    @property
    def contents(self) -> str: ...
    @contents.setter
    def contents(self, value: object) -> None: ...
