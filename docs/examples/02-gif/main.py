#!/usr/bin/env python
# -*- coding: utf-8 name> -*-

"""This script animates a GIF image in text art."""

from pathlib import Path
import time

from PIL import Image
from picharsso import new_drawer
from picharsso.utils import clear_screen, terminal_size


if __name__ == "__main__":
    # Choose image
    # image_path = "<path/to/image>"
    image_path = Path(__file__).parent / ("nyan.webp")

    # Open image
    image = Image.open(image_path)

    # Get terminal height
    height, _ = terminal_size()

    # Choose an art style
    style = "gradient"  # or "braille"

    # Define drawer
    drawer = new_drawer(style, height=height, colorize=True)

    # Iterate over frames
    texts = []
    for frame_id in range(image.n_frames):
        # Select frame
        image.seek(frame_id)

        # Save output for frame
        texts.append(drawer(image))

    # Iterate over saved outputs in a circular manner
    num_frames = len(texts)
    counter = 0
    while True:
        # Refresh
        clear_screen()

        # Print output
        print(texts[counter])

        # Set a delay between frames
        time.sleep(1 / num_frames)

        # Circular increment
        counter = (counter + 1) % num_frames
