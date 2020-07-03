from .gradient import GradientDrawer
from .base import BaseDrawer, RESAMPLING_FILTERS, DEFAULT_RESAMPLING
from .braille import BrailleDrawer

DRAWERS: dict = {"gradient": GradientDrawer, "braille": BrailleDrawer}


def new_drawer(style, **kwargs):
    return DRAWERS[style](**kwargs)
