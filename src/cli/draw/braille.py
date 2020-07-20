"""This module defines the `picharsso draw braille` command.

Refer to https://kelvindecosta.github.io/picharsso/commands/draw/braille/.
"""


import click

from ...draw import new_drawer
from ...draw.braille import DEFAULT_THRESHOLD


@click.command("braille", options_metavar="[options]")
@click.option(
    "-t",
    "--threshold",
    type=click.IntRange(0, 255),
    help="Threshold pixel luminance (from grayscale).",
    default=DEFAULT_THRESHOLD,
    show_default=True,
)
@click.pass_context
def draw_braille(context, threshold):
    """Use the Braille style."""

    image = context.obj.pop("image")

    drawer = new_drawer("braille", threshold=threshold, **context.obj)
    print(drawer(image))
