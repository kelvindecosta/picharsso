from abc import ABC, abstractmethod

import numpy as np
from numpy.lib.recfunctions import unstructured_to_structured


class BaseFormatter(ABC):
    def __init__(self, colorize=False):
        self.colorize = None
        BaseFormatter.set(self, colorize=colorize)

        self.vcolor = np.vectorize(self.color)

    def __call__(self, text_matrix, image, resample):
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

    @staticmethod
    @abstractmethod
    def translate(text_matrix):

    @staticmethod
    @abstractmethod
    def unify(text_matrix):

    def set(self, colorize=None):
        if colorize is not None:
            self.colorize = colorize
