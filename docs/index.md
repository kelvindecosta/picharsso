# Picharsso

<div align="center">
    <p>
        <img alt="Picharsso" src="/assets/images/logo.webp">
    </p>

    <em>A utility for converting images to text art.</em>
</div>

## Installation

Run the following command:

```bash
pip install picharsso
```

This will:

* download and install the [`picharsso` Python package](https://pypi.org/project/picharsso/)
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

--8<-- "docs/snippets/embed/subjects/apple.html"

To convert an image to text art, run:

=== "Braille"
    ```bash
    picharsso draw -c -H 32 <path/to/image> braille
    ```

    Here's what it should look like:

    --8<-- "docs/snippets/embed/outputs/demo/apple-braille.html"

    !!! abstract "Breakdown"
        | Argument  | Effect                                                   |
        | :-------: | :------------------------------------------------------- |
        |   `-c`    | Apply **image colors** to the output text.               |
        |  `-H 32`  | Sets the **number of lines** of the output text to `32`. |
        | `braille` | Use the [Braille style](/styles/braille/).               |

=== "Gradient"
    ```bash
    picharsso draw -c -H 32 <path/to/image> gradient
    ```

    Here's what it should look like:

    --8<-- "docs/snippets/embed/outputs/demo/apple-gradient.html"

    !!! abstract "Breakdown"
        |  Argument  | Effect                                                   |
        | :--------: | :------------------------------------------------------- |
        |    `-c`    | Apply **image colors** to the output text.               |
        |  `-H 32`   | Sets the **number of lines** of the output text to `32`. |
        | `gradient` | Use the [gradient style](/styles/gradient/).             |

!!! warning
    Don't forget to replace `<path/to/image>`.

--8<-- "docs/snippets/references/cli.md"

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
    Picharsso integrates well with [Pillow](https://python-pillow.org/),
    the friendly PIL fork.

--8<-- "docs/snippets/references/styles.md"

Now consider this animated GIF:

--8<-- "docs/snippets/embed/subjects/nyan.html"

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

    --8<-- "docs/snippets/embed/outputs/examples/02-gif/nyan-braille.html"

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

    --8<-- "docs/snippets/embed/outputs/examples/02-gif/nyan-gradient.html"

--8<-- "docs/snippets/references/api.md"

--8<-- "docs/snippets/references/examples.md"
