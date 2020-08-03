#!/usr/bin/env python
# -*- coding: utf-8 name> -*-

"""This script converts an image to text art."""

from pathlib import Path

from PIL import Image
from picharsso import new_drawer
from picharsso.utils import terminal_size

if __name__ == "__main__":
    # Choose image
    # image_path = "<path/to/image>"
    image_path = Path(__file__).parent / "hackerman.webp"

    # Open image
    image = Image.open(image_path)

    # Choose an art style
    style = "gradient"  # or "braille"

    # Set height
    height, _ = terminal_size()

    # Define drawer
    drawer = new_drawer(style, height=height, colorize=True)

    # Print drawer output
    print(drawer(image))
