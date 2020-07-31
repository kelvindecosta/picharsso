"""This module defines a formatter for [HTML](../../formats/html.md)."""

from html.entities import name2codepoint

import numpy as np

from .base import BaseFormatter

HTML_ENTITY_MAP: dict = {chr(value): key for (key, value) in name2codepoint.items()}
"""A dictionary mapping unicode characters to their equivalent HTML entities."""

HTML_ENTITY_MAP[" "] = "nbsp;"


class HtmlFormatter(BaseFormatter):
    """
    A formatter for [HTML](../../formats/html.md).

    Inherits [`BaseFormatter`][picharsso.format.base.BaseFormatter].
    """

    @staticmethod
    def color(text, color):
        return f'<span style="color : rgb{tuple(color)};">{text}</span>'

    @staticmethod
    def translate(text_matrix):
        unique_chars = np.unique(text_matrix)

        # Change datatype to accomodate strings of varying length
        text_matrix = text_matrix.astype(
            f"<U{len(max(name2codepoint.keys(), key=len))}"
        )

        # Change each character to its equivalent entity
        for char in unique_chars:
            if char in HTML_ENTITY_MAP:
                text_matrix[text_matrix == char] = f"&{HTML_ENTITY_MAP[char]}"

        return text_matrix

    @staticmethod
    def unify(text_matrix):
        return "<div>{}</div>".format(
            "\n".join([f"<div>{''.join(row)}</div>" for row in text_matrix])
        )


__all__ = ["HtmlFormatter", "HTML_ENTITY_MAP"]
