import click

from ...draw import new_drawer
from ...draw.gradient import DEFAULT_CHARSET


@click.command("gradient", options_metavar="[options]")
@click.option(
    "-s",
    "--charset",
    type=str,
    help="Character set ordered by increasing 'brightness'.",
    default=DEFAULT_CHARSET,
    show_default=True,
)
@click.option(
    "-n", "--negative", is_flag=True, help="Whether to invert output text brightness."
)
@click.pass_context
def draw_gradient(context, charset, negative):
    """Use the gradient style."""

    image = context.obj.pop("image")

    drawer = new_drawer("gradient", charset=charset, negative=negative, **context.obj)
    print(drawer(image))
