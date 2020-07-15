"""
This package defines formatters for different modes of text output.

--8<-- "docs/snippets/references/formats.md"
"""

from .ansi import AnsiFormatter
from .base import BaseFormatter
from .html import HtmlFormatter

FORMATTERS: dict = {"ansi": AnsiFormatter, "html": HtmlFormatter}
"""The collection of formatters."""

DEFAULT_FORMATTER: str = "ansi"
"""The default formatter."""


def new_formatter(mode=DEFAULT_FORMATTER, **kwargs):
    """Creates a new formatter instance.

    Args:
        mode (Option[str]): The mode of the output text.
                            Defaults to `DEFAULT_FORMATTER`.
        **kwargs (dict): Appropriate keyword arguments.
                        See [`BaseFormatter`][picharsso.format.base.BaseFormatter]
                        and others.

    Returns:
        Type[picharsso.format.BaseFormatter] : The new formatter instance.
    """
    return FORMATTERS[mode](**kwargs)
