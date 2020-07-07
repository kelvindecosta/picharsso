import shutil

import numpy as np
from PIL import Image
from sty import ef, rs


def embolden(text):
    return f"{ef.bold}{text}{rs.bold_dim}"


def ensure_rgb(image):
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
    return f"{ef.italic}{text}{rs.italic}"


def submatrices(matrix, shape):
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
    return shutil.get_terminal_size()[::-1]
