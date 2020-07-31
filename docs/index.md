# Picharsso

<div align="center">
    <p>
        <img alt="Picharsso" src="assets/images/logo.webp">
    </p>
    <p>
        <em>A utility for converting images to text art.</em>
    </p>
</div>

## Installation

Run the following command:

```bash
pip install picharsso
```

This will:

* download and install the [`picharsso` Python package](https://pypi.org/project/picharsso/){target=_blank}
  (along with its dependencies).
* create an executable, `picharsso`, for the CLI (command line interface).

??? success "Verification"
    To verify that Picharsso is installed, run:

    ```bash
    python -c "import picharsso"
    ```

## Commands (CLI)

Picharsso ships with a CLI that provides some basic functionality from the terminal.

??? question "Usage"
    Run the following command to display a helpful message:

    ```bash
    picharsso -h
    ```

    ```
    --8<-- "docs/snippets/cli/help.txt"
    ```

Consider the following image:

<div align="center">
    <p>
        <img alt="Apple logo" src="assets/images/subjects/apple.webp" />
    </p>
    <p>
        <em>Apple Computer [Rob Janoff, 1977]</em>
    </p>
</div>

To convert an image to text art, run:

=== "Braille"
    ```bash
    picharsso draw -c -H 32 <path/to/image> braille
    ```

    Here's what it should look like:

    <div align="center">
        <img
            alt="Apple logo in text (Braille style)"
            src="assets/images/outputs/demo/apple-braille.webp"
        />
    </div>

    !!! abstract "Breakdown"
        | Argument  | Effect                                                   |
        | :-------: | :------------------------------------------------------- |
        |   `-c`    | Apply **image colors** to the output text.               |
        |  `-H 32`  | Sets the **number of lines** of the output text to `32`. |
        | `braille` | Use the [Braille style](styles/braille.md).              |

=== "Gradient"
    ```bash
    picharsso draw -c -H 32 <path/to/image> gradient
    ```

    Here's what it should look like:

    <div align="center">
        <img
            alt="Apple logo in text (gradient style)"
            src="assets/images/outputs/demo/apple-gradient.webp"
        />
    </div>

    !!! abstract "Breakdown"
        |  Argument  | Effect                                                   |
        | :--------: | :------------------------------------------------------- |
        |    `-c`    | Apply **image colors** to the output text.               |
        |  `-H 32`   | Sets the **number of lines** of the output text to `32`. |
        | `gradient` | Use the [gradient style](styles/gradient.md).            |

!!! warning
    Don't forget to replace `<path/to/image>`.

!!! question "CLI"
    Refer to the [CLI documentation](commands/index.md)
    to learn about the various **commands** and **arguments**.

## Library (API)

The example from the previous section can be implemented in just a few lines of Python:

=== "Braille"
    ```python linenums="1" hl_lines="8-12"
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

=== "Gradient"
    ```python linenums="1" hl_lines="8-12"
    from PIL import Image
    from picharsso import new_drawer

    if __name__ == "__main__":
        # Open image
        image = Image.open("<path/to/image>")

        # Define drawer
        drawer = new_drawer("gradient", height=32, colorize=True)

        # Print drawer output
        print(drawer(image))
    ```

!!! info "Pillow"
    Picharsso integrates well with [Pillow](https://python-pillow.org/){target=_blank},
    the friendly PIL fork.

!!! question "Styles"
    Refer to the [Styles documentation](styles/index.md)
    for an in-depth guide to the **image processing behind Picharsso**.

Now consider this animated GIF:

<div align="center">
    <p>
        <img alt="Nyan Cat" src="examples/02-gif/nyan.webp" />
    </p>
    <p>
        <em>Nyan Cat</em>
    </p>
</div>

With some more lines of code, you can animate GIFs in text!

=== "Braille"
    ```python linenums="1" hl_lines="15-16 24-25"
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
            src="assets/images/outputs/examples/02-gif/nyan-braille.webp"
        />
    </div>

=== "Gradient"
    ```python linenums="1" hl_lines="15-16 24-25"
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
        drawer = new_drawer("gradient", height=height, colorize=True)

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
            alt="Nyan Cat in text (gradient style)"
            src="assets/images/outputs/examples/02-gif/nyan-gradient.webp"
        />
    </div>

!!! question "API"
    Refer to the [API documentation](library/draw/index.md)
    to learn about the various **classes** and **functions**.

!!! tip "Examples"
    Check out some more [examples](examples/01-image/index.md).

    You can use an image [directly from the web](examples/03-web/index.md) too!
    