"""
This module defines a drawer for the [Braille style](../../styles/braille.md).

??? example "Example"
    Consider the following image:

    <div align="center">
        <p>
            <img alt="Apple logo" src="../../assets/images/subjects/apple.webp" />
        </p>
        <p>
            <em>Apple Computer [Rob Janoff, 1977]</em>
        </p>
    </div>

    Here's what it should look like:

    <div align="center">
        <img
            alt="Apple logo in text (Braille style)"
            src="../../assets/images/outputs/demo/apple-braille.webp"
        />
    </div>
"""

import numpy as np

from .base import BaseDrawer
from ..utils import submatrices

DEFAULT_THRESHOLD: int = 64
"""The default threshold grayscale intensity."""


class BrailleDrawer(BaseDrawer):
    """
    A drawer for the [Braille style](../../styles/braille.md).

    Inherits [`BaseDrawer`][picharsso.draw.base.BaseDrawer].

    Attributes:
        threshold (int): Threshold grayscale intensity for pixels to be considered.
        kernel (numpy.ndarray): A hard-coded matrix relating the intensity to
                             the Unicode values for Braille characters.
        charset_array (numpy.ndarray): A matrix of all Braille characters,
                                    indexed by their offsetted Unicode value.
    """

    def __init__(self, threshold=DEFAULT_THRESHOLD, **kwargs):
        """Initialization method.

        Args:
            threshold (Optional[int]): Threshold grayscale intensity
                                    for pixels to be considered.
        """

        super().__init__(**kwargs)
        self.threshold = None
        self.set(threshold=threshold)

        self.kernel = np.array([[1, 8], [2, 16], [4, 32], [64, 128]]).astype(np.uint8)
        self.charset_array = np.array([chr(ord("\u2800") + x) for x in range(256)])

    def calculate_size(self, image_size):
        # Possible dimensions
        new_h = self.height
        new_w = self.width

        new_h = new_h * 4
        new_w = new_w * 2

        # Image dimensions
        old_h, old_w = image_size

        # If height is not set, infer it from width
        if not new_h:
            new_h = int(round(old_h / old_w * new_w))

        # If width is not set, infer it from height
        if not new_w:
            new_w = int(round(old_w / old_h * new_h))

        return new_h, new_w

    def process(self, image):
        # Convert the image mode to grayscale.
        # Filter all pixels with intensity greater than or equal to the threshold.
        # Perform a convolution on this filtered image with the Braille kernel.
        # The resultant matrix has the offsetted Unicode values, i.e., indices
        # for the corresponding Braille characters that form the image.
        # Index the character set with the indices.
        return self.charset_array[
            np.einsum(
                "ij,klij->kl",
                self.kernel,
                submatrices(
                    (np.array(image.convert("L")) >= self.threshold).astype(np.uint8),
                    self.kernel.shape,
                ),
            )
        ]

    def set(self, threshold=None, **kwargs):
        """Sets attributes of the drawer instance.

        Args:
            threshold (Optional[int]): Sets `threshold`.
            **kwargs (dict): Appropriate keyword arguments.
                    See [`BaseDrawer.set`][picharsso.draw.base.BaseDrawer.set].
        """
        super().set(**kwargs)

        if threshold is not None:
            self.threshold = threshold


__all__ = ["BrailleDrawer"]
