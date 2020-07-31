"""
This package defines drawers for different styles of text art.

!!! question "Styles"
    Refer to the [Styles documentation](../../styles/index.md)
    for an in-depth guide to the **image processing behind Picharsso**.
"""

from .gradient import GradientDrawer
from .base import BaseDrawer, RESAMPLING_FILTERS, DEFAULT_RESAMPLING
from .braille import BrailleDrawer

DRAWERS: dict = {"gradient": GradientDrawer, "braille": BrailleDrawer}
"""The collection of drawers."""


def new_drawer(style, **kwargs):
    """Creates a new drawer instance.

    Args:
        style (str): The style of the text art.
        **kwargs (dict): Appropriate keyword arguments.
                        See [`BaseDrawer`][picharsso.draw.base.BaseDrawer]
                        and others.

    Returns:
        Type[picharsso.draw.BaseDrawer]: The new drawer instance.
    """
    return DRAWERS[style](**kwargs)
