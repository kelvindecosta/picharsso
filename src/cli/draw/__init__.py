"""This package defines the `picharsso draw` command.

Refer to https://kelvindecosta.github.io/picharsso/commands/draw/.
"""

import click
from PIL import Image

from ...draw import RESAMPLING_FILTERS, DEFAULT_RESAMPLING
from ...format import FORMATTERS, DEFAULT_FORMATTER
from ...utils import terminal_size

from .gradient import draw_gradient
from .braille import draw_braille


@click.group(options_metavar="[options]", subcommand_metavar="<command> [args]")
@click.argument("path", type=click.Path(exists=True), metavar="<path>")
@click.option(
    "-c", "--colorize", is_flag=True, help="Apply image colors to output text."
)
@click.option(
    "-m",
    "--mode",
    type=click.Choice(list(FORMATTERS.keys())),
    default=DEFAULT_FORMATTER,
    help="Format mode for output text.",
    show_default=True,
)
@click.option(
    "-r",
    "--resample",
    type=click.Choice(list(RESAMPLING_FILTERS.keys())),
    default=DEFAULT_RESAMPLING,
    help="Resampling filter.",
    show_default=True,
)
@click.option(
    "-H",
    "--height",
    type=int,
    default=0,
    help="Height of output text in characters.\n\nIf 0, derives from width.",
    show_default=True,
)
@click.option(
    "-W",
    "--width",
    type=int,
    default=0,
    help="Width of output text in characters.\n\nIf 0, derives from height.",
    show_default=True,
)
@click.option(
    "-term-h",
    "--terminal-height",
    is_flag=True,
    help="Sets height to terminal height.",
)
@click.option(
    "-term-w", "--terminal-width", is_flag=True, help="Sets width to terminal width.",
)
@click.pass_context
def draw(
    context,
    path,
    colorize,
    mode,
    resample,
    height,
    width,
    terminal_height,
    terminal_width,
):
    """Generate text art from an image.

        <path>                          Path to the image file.
    """
    image = Image.open(path)

    if terminal_width or terminal_height or height == 0 and width == 0:
        term_h, term_w = terminal_size()

        if terminal_height:
            height = term_h

        if terminal_width:
            width = term_w

        if height == 0 and width == 0:
            height = term_h
            width = term_w

    context.obj = {
        "image": image,
        "colorize": colorize,
        "mode": mode,
        "resample": resample,
        "height": height,
        "width": width,
    }


draw.add_command(draw_gradient)
draw.add_command(draw_braille)
