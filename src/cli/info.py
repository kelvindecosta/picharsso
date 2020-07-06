from pathlib import Path

import click

from .. import __file__ as root_module_path
from ..meta import NAME, VERSION, DESCRIPTION, REPO_URL, DOCS_URL, LICENSE, AUTHOR
from ..utils import embolden, italicize


@click.command(options_metavar="[options]")
def info():
    """Displays package information."""
    with open(Path(root_module_path).parent / "data" / "logo.txt", "r") as file_stream:
        logo_text = file_stream.read().strip()

    output = logo_text.split("\n")

    line = 3
    output[line] += f"    {embolden(NAME)}"

    line += 2
    output[line] += f"    {italicize(DESCRIPTION)}"

    line += 3
    output[line] += f"    {italicize('Version')} : {VERSION}"

    line += 1
    output[line] += f"    {italicize('License')} : {LICENSE}"

    line += 1
    output[line] += f"    {italicize('Author')}  : {AUTHOR}"

    line += 3
    output[line] += f"    {italicize('Source')}  : {REPO_URL}"

    line += 1
    output[line] += f"    {italicize('Docs')}    : {DOCS_URL}"

    print("\n".join(output[1:-1]))
