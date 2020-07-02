from .ansi import AnsiFormatter
from .base import BaseFormatter
from .html import HtmlFormatter

FORMATTERS: dict = {"ansi": AnsiFormatter, "html": HtmlFormatter}

DEFAULT_FORMATTER: str = "ansi"


def new_formatter(mode=DEFAULT_FORMATTER, **kwargs):
    return FORMATTERS[mode](**kwargs)
