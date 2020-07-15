"""This module defines utility functions that are used across the package."""

import shutil

import numpy as np
from PIL import Image
from sty import ef, rs


def embolden(text):
    """Modifies text to appear in a bold typeface,
    using [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

    Args:
        text (str): The subject text.

    Returns:
        str: The text in a bold typeface.
    """
    return f"{ef.bold}{text}{rs.bold_dim}"


def ensure_rgb(image):
    """Usually converts any [Pillow](https://python-pillow.org/)
    `image` to its equivalent in the `RGB` mode.

    Args:
        image (PIL.Image.Image): The subject image.

    Returns:
        PIL.Image.Image: The image in the `RGB` mode.
    """
    # If the image has a color palette,
    # convert to the `RGBA` mode.
    if image.mode == "P":
        image = image.convert("RGBA")

    # If the image is in `RGBA` mode,
    # create a white background.
    if image.mode == "RGBA":
        temp = Image.new("RGB", image.size, (255, 255, 255))
        temp.paste(image, mask=image.split()[3])
        image = temp

    # Convert to `RGB` mode
    return image.convert("RGB")


def italicize(text):
    """Modifies text to appear in italics,
    using [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

    Args:
        text (str): The subject text.

    Returns:
        str: The text in italics.
    """
    return f"{ef.italic}{text}{rs.italic}"


def submatrices(matrix, shape):
    """Returns a rolling window view of a `matrix`, without overlapping,
    given the `shape` of the window.

    Args:
        matrix (numpy.ndarray): The subject matrix.
        shape (Tuple[int, int]): The `<height>` and `<width>` of the window.

    Returns:
        numpy.ndarray: The rolling window view of the matrix.

    Note:
        This operation doesn't account for the loss of border elements.
    """
    # Extract strides and shapes for calculation.
    mat_hs, mat_ws = matrix.strides[:2]
    mat_h, mat_w = matrix.shape[:2]
    ker_h, ker_w = shape

    # View `matrix` according to new strides and shape.
    return np.lib.stride_tricks.as_strided(
        matrix,
        (1 + (mat_h - ker_h) // ker_h, 1 + (mat_w - ker_w) // ker_w, ker_h, ker_w)
        + matrix.shape[2:],
        strides=(ker_h * mat_hs, ker_w * mat_ws, mat_hs, mat_ws) + matrix.strides[2:],
    )


def terminal_size():
    """Returns the size of the terminal window.

    Returns:
        (Tuple[int, int]): The `<height>` and `<width>`
                            of the terminal window in characters.

    Note:
        When used while piping,
        this function usually returns the default terminal size, `(24, 80)`.
    """
    return shutil.get_terminal_size()[::-1]


__all__ = [
    "embolden",
    "ensure_rgb",
    "italicize",
    "submatrices",
    "terminal_size",
]
