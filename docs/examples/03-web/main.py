#!/usr/bin/env python
# -*- coding: utf-8 name> -*-

"""This script animates a GIF image, from the web, in text art."""

from io import BytesIO
import time

from PIL import Image
from picharsso import new_drawer
from picharsso.utils import clear_screen, terminal_size

import requests


if __name__ == "__main__":
    # Set URL of image
    image_url = "https://bit.ly/3hs2Vxr"

    # Open Image from respose content
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

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
