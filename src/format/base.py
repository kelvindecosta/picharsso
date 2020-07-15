"""
This module defines an abstract base formatter.

--8<-- "docs/snippets/references/formats.md"
"""

from abc import ABC, abstractmethod

import numpy as np
from numpy.lib.recfunctions import unstructured_to_structured


class BaseFormatter(ABC):
    """
    An abstract base formatter.

    Attributes:
        colorize (bool): Whether to color the text.
        vcolor (Callable): The vectorized implementation of the `color` method.

    Note:
        The following methods must be overwritten:

        - [`color`][picharsso.format.base.BaseFormatter.color]
        - [`translate`][picharsso.format.base.BaseFormatter.translate]
        - [`unify`][picharsso.format.base.BaseFormatter.unify]
    """

    def __init__(self, colorize=False):
        """Initialization method.

        Args:
            colorize (Option[bool]): Whether to color the text.
        """
        self.colorize = None
        BaseFormatter.set(self, colorize=colorize)

        self.vcolor = np.vectorize(self.color)

    def __call__(self, text_matrix, image, resample):
        """Applies formatting and colorization on the `text_matrix`
        and returns a single string.

        Args:
            text_matrix (numpy.ndarray): The subject text matrix,
                                        with `shape = (<height>, <width>)`,
                                        and `dtype = str`.
            image (PIL.Image.Image): The subject image.
            resample (int): The resampling filter.

        Returns:
            str: The formatted string of text with color (if specified).
        """

        text_size = text_matrix.shape

        # Apply any translations.
        text_matrix = self.translate(text_matrix)

        # Colorize if necessary
        if self.colorize:
            # Pool the colors from the original image by resizing it to the size of the text output.
            # Using the vectorized `color` method, color each element in the `text_martix`.
            # The vectorized operation takes a `str` from `text_matrix`
            # and a `List[int, int, int]` from the pooled colors.
            text_matrix = self.vcolor(
                text_matrix,
                unstructured_to_structured(
                    np.array(image.resize(text_size[::-1], resample=resample)).astype(
                        np.uint8
                    )
                ).astype("O"),
            )

        return self.unify(text_matrix)

    @staticmethod
    @abstractmethod
    def color(text, color):
        """Applies `color` to a string of `text`.

        Args:
            text (str): The subject text.
            color (Tuple[int, int, int]): The `RGB` value for the color.

        Returns:
            str: The colored text.
        """

    @staticmethod
    @abstractmethod
    def translate(text_matrix):
        """Applies translatations to `text_matrix`.

        Args:
            text_matrix (numpy.ndarray): The subject text matrix,
                                        with `shape = (<height>, <width>)`,
                                        and `dtype = str`.

        Returns:
            numpy.ndarray: The translated text_matrix.
        """

    @staticmethod
    @abstractmethod
    def unify(text_matrix):
        """Formats a `text_matrix` into a single string.

        Args:
            text_matrix (numpy.ndarray): The subject text matrix,
                                        with `shape = (<height>, <width>)`,
                                        and `dtype = str`.

        Returns:
            str: The formatted string of text art.
        """

    def set(self, colorize=None):
        """Sets attributes of the formatter instance.

        Args:
            colorize (Optional[bool]): Sets `colorize`.
        """
        if colorize is not None:
            self.colorize = colorize


__all__ = ["BaseFormatter"]
