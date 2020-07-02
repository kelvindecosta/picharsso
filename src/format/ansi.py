from sty import fg

from .base import BaseFormatter


class AnsiFormatter(BaseFormatter):
    @staticmethod
    def color(text, color):
        return f"{fg(*color)}{text}{fg.rs}"

    @staticmethod
    def translate(text_matrix):
        return text_matrix

    @staticmethod
    def unify(text_matrix):
        return "\n".join(["".join(row) for row in text_matrix])
