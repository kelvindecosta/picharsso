# Picharsso

<p align=center>

  <img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/docs/assets/images/logo.webp" height="200px"/>

  <br>
  <span>A utility for converting images to text art.</span>
  <br>
  <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/picharsso">
  <a target="_blank" href="https://pypi.python.org/pypi/picharsso/"><img alt="pypi package" src="https://img.shields.io/pypi/v/picharsso?color=light%20green"></a>
  <a target="_blank" href="https://github.com/kelvindecosta/picharsso/blob/master/LICENSE" title="License: MIT"><img alt="GitHub" src="https://img.shields.io/github/license/kelvindecosta/picharsso?color=blue"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://kelvindecosta.github.io/picharsso/">Documentation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://kelvindecosta.github.io/picharsso/examples/01-image/">Examples</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/kelvindecosta/picharsso/blob/master/CONTRIBUTING.md">Contributing</a>
</p>

## Installation

Run the following command:

```bash
pip install picharsso
```

This will:

- download and install the [`picharsso` Python package](https://pypi.org/project/picharsso/)
  (along with its dependencies).
- create an executable, `picharsso`, for the CLI (command line interface).

> **Verification**
>
> To verify that Picharsso is installed, run:
>
> ```bash
> python -c "import picharsso"
> ```

## Commands

Picharsso ships with a CLI that provides some basic functionality from the terminal.

> **Usage**
>
> Run the following command to display a helpful message:
>
> ```bash
> picharsso -h
> ```
>
> ```
> Usage: picharsso [options] <command> [args]
>
>   A utility for converting images to text art.
>
> Options:
>   -h, --help  Show this message and exit.
>
> Commands:
>   draw  Generate text art from an image.
>   info  Displays package information.
> ```

Consider the following image:

<div align="center">
  <p>
    <img alt="Apple logo" src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/docs/assets/images/subjects/apple.webp" />
  </p>
  <em>Apple Computer [Rob Janoff, 1977]</em>
</div>

To convert an image to text art, run:

```bash
picharsso draw -c -H 32 <path/to/image> gradient
```

Here's what it should look like:

<div align="center">
  <img
    alt="Apple logo in text (gradient style)"
    src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/docs/assets/images/outputs/demo/apple-gradient.webp"
  />
</div>

> **Breakdown**
>
> |  Argument  | Effect                                                                                |
> | :--------: | :------------------------------------------------------------------------------------ |
> |    `-c`    | Apply **image colors** to the output text.                                            |
> |  `-H 32`   | Sets the **number of lines** of the output text to `32`.                              |
> | `gradient` | Use the [gradient style](https://kelvindecosta.github.io/picharsso/styles/gradient/). |
>
> Don't forget to replace `<path/to/image>`.

Refer to the [CLI documentation](https://kelvindecosta.github.io/picharsso/commands/) to learn about the various **commands** and **arguments**.

## Library

The example from the previous section can be implemented in just a few lines of Python:

```python
from PIL import Image
from picharsso import new_drawer

if __name__ == "__main__":
    # Open image
    image = Image.open("<path/to/image>")

    # Define drawer
    drawer = new_drawer("braille", height=32, colorize=True)

    # Print drawer output
    print(drawer(image))
```

Here's what it should look like:

<div align="center">
  <img
    alt="Apple logo in text (Braille style)"
    src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/docs/assets/images/outputs/demo/apple-braille.webp"
  />
</div>

> **Styles**
>
> Refer to the [Styles documentation](https://kelvindecosta.github.io/picharsso/styles/) for an in-depth guide to the **image processing behind Picharsso**.

Now consider this animated GIF:

<div align="center">
  <p>
    <img alt="Nyan Cat" src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/docs/examples/02-gif/nyan.webp" />
  </p>
  <em>Nyan Cat</em>
</div>

With some more lines of code, you can animate GIFs in text!

```python
import time

from PIL import Image
from picharsso import new_drawer
from picharsso.utils import clear_screen, terminal_size


if __name__ == "__main__":
    # Open image
    image = Image.open("<path/to/image>")

    # Get terminal height
    height, _ = terminal_size()

    # Define drawer
    drawer = new_drawer("braille", height=height, colorize=True, threshold=0)

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
```

Here's what it should look like:

<div align="center">
  <img
    alt="Nyan Cat in text (Braille style)"
    src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/docs/assets/images/outputs/examples/02-gif/nyan-braille.webp"
  />
</div>

Refer to the [API documentation](https://kelvindecosta.github.io/picharsso/library/draw/) to learn about the various **classes** and **functions**.

> **Examples**
>
> Check out some more [examples](https://kelvindecosta.github.io/picharsso/examples/01-image/).
>
> You can use an image [directly from the web](https://kelvindecosta.github.io/picharsso/examples/03-web/) too!

## Contributing

Do you have a feature request, bug report, or patch? Great!
Check out the [contributing guidelines](https://github.com/kelvindecosta/picharsso/blob/master/CONTRIBUTING.md)!

## License

Copyright (c) 2019 Kelvin DeCosta.
Released under the MIT License.
See [LICENSE](https://github.com/kelvindecosta/picharsso/blob/master/LICENSE) for details.
