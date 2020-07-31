"""
This module defines a drawer for the [gradient style](../../styles/gradient.md).

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
            alt="Apple logo in text (gradient style)"
            src="../../assets/images/outputs/demo/apple-gradient.webp"
        />
    </div>
"""

import numpy as np

from .base import BaseDrawer

DEFAULT_CHARSET: str = " :!?PG@"
"""The default character set."""


class GradientDrawer(BaseDrawer):
    """
    A drawer for the [gradient style](../../styles/gradient.md).

    Inherits [`BaseDrawer`][picharsso.draw.base.BaseDrawer].

    Attributes:
        charset (str): A set of characters ordered by the amount of area
                        their symbols occupy.
        negative (bool): Whether or not to reverse the `charset`.
        charset_array (numpy.ndarray): A vectorized version of the `charset`.
    """

    def __init__(self, charset=DEFAULT_CHARSET, negative=False, **kwargs):
        """Initialization method.

        Args:
            charset (Optional[str]): A set of characters ordered
                                    by the amount of area their symbols occupy.
                                    Defaults to `DEFAULT_CHARSET`
            negative (Optional[bool]): Whether or not to reverse the `charset`.
            **kwargs (dict): Appropriate keyword arguments.
                            See [`BaseDrawer`][picharsso.draw.base.BaseDrawer].
        """
        super().__init__(**kwargs)
        self.charset = None
        self.negative = None
        self.charset_array = None
        self.set(charset=charset, negative=negative)

    def calculate_size(self, image_size):
        # Possible dimensions
        new_h = self.height
        new_w = self.width

        # Image dimensions
        old_h, old_w = image_size

        # If height is not set, infer it from width
        if not new_h:
            new_h = int(round(old_h / old_w * new_w / 2.125))

        # If width is not set, infer it from height
        if not new_w:
            new_w = int(round(old_w / old_h * new_h * 2.125))

        return new_h, new_w

    def process(self, image):
        # Convert the image mode to grayscale.
        # Normalize the pixel values from a range of (0, 255) to (0, len(self.charset)-1),
        # to obtain indices for the character set.
        # Index the character set array with the indices.
        return self.charset_array[
            np.round(
                np.array(image.convert("L")) / 255 * (len(self.charset) - 1)
            ).astype(int)
        ]

    def set(self, charset=None, negative=None, **kwargs):
        """Sets attributes of the drawer instance.

        Args:
            charset (Optional[str]): Sets `charset`.
            negative (Optional[bool]): Sets `negative`.
            **kwargs (dict): Appropriate keyword arguments.
                    See [`BaseDrawer.set`][picharsso.draw.base.BaseDrawer.set].
        """
        super().set(**kwargs)

        if charset is not None:
            self.charset = charset

        if negative is not None:
            self.negative = negative

        self.charset_array = np.array(
            list(self.charset if not self.negative else self.charset[::-1])
        )


__all__ = ["GradientDrawer"]
