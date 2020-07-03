import numpy as np

from .base import BaseDrawer

DEFAULT_CHARSET: str = " :!?PG@"


class GradientDrawer(BaseDrawer):
    def __init__(self, charset=DEFAULT_CHARSET, negative=False, **kwargs):
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
        super().set(**kwargs)

        if charset is not None:
            self.charset = charset

        if negative is not None:
            self.negative = negative

        self.charset_array = np.array(
            list(self.charset if not self.negative else self.charset[::-1])
        )
