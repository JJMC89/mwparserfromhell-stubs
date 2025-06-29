__all__ = [
    "get_html_tag",
    "is_parsable",
    "is_visible",
    "is_single",
    "is_single_only",
    "is_scheme",
]

URI_SCHEMES: dict[str, bool]
PARSER_BLACKLIST: list[str]
INVISIBLE_TAGS: list[str]
SINGLE_ONLY: list[str]
SINGLE: list[str]
MARKUP_TO_HTML: dict[str, str]

def get_html_tag(markup: str) -> str: ...
def is_parsable(tag: str) -> bool: ...
def is_visible(tag: str) -> bool: ...
def is_single(tag: str) -> bool: ...
def is_single_only(tag: str) -> bool: ...
def is_scheme(scheme: str, slashes: bool = ...) -> bool: ...
