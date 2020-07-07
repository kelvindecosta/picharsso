import click

from .draw import draw
from .info import info
from ..meta import DESCRIPTION

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(
    help=DESCRIPTION,
    options_metavar="[options]",
    subcommand_metavar="<command> [args]",
    context_settings=CONTEXT_SETTINGS,
)
def main():
    """The main program."""


main.add_command(draw)
main.add_command(info)
