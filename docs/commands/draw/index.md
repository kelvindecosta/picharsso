---
title: "picharsso draw - CLI - Picharsso"
description: "Generate text art from an image."
---

# `picharsso draw`

*Generate text art from an image.*

## Usage

```
picharsso draw [options] <path> <command> [args]
```

## Arguments

### `<path>`
:   *Path to the image file.*

## Options

### `-c`, `--colorize`
:   *Apply image colors to output text.*

    ??? example
        Consider the following image:

        <div align="center">
            <p>
                <img alt="Instagram logo" src="../../assets/images/subjects/instagram.webp" />
            </p>
            <p>
                <em>Instagram</em>
            </p>
        </div>

        ```bash
        picharsso draw [-c] -H 32 docs/assets/images/subjects/instagram.webp gradient
        ```

        Here's what it should look like:

        === "colorize = False"
            <div align="center">
                <img
                    alt="Instagram logo in text (without color)"
                    src="../../assets/images/outputs/format/colorize/instagram-gray.webp"
                />
            </div>

        === "True"
            <div align="center">
                <img
                    alt="Instagram logo in text (with color)"
                    src="../../assets/images/outputs/format/colorize/instagram-color.webp"
                />
            </div>

### `-m`, `--mode` [`ansi`|`html`]
:   *Format mode for output text.  [default: ansi]*

    !!! question "Formats"
        Refer to the [Formats documentation](../../formats/index.md)
        to learn about the supported output formats.

### `-r`, `--resample` [`nearest`|`box`|`bilinear`|`hamming`|`bicubic`|`lanczos`]
:   *Resampling filter.  [default: nearest]*

    ??? example
        Consider the following image:

        <div align="center">
            <p>
                <img alt="Starry Night" src="../../assets/images/subjects/starry-night.webp" />
            </p>
            <p>
                <em>Starry Night [Vincent van Gogh, 1889]</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -term-h -r <resample> docs/assets/images/subjects/starry-night.webp gradient -s "█"
        ```

        Here's what it should look like:

        === "resample = 'nearest'"
            <div align="center">
                <img
                    alt="Starry Night (nearest resampling)"
                    src="../../assets/images/outputs/draw/resample/starry-night-resample-nearest.webp"
                />
            </div>

        === "'box'"
            <div align="center">
                <img
                    alt="Starry Night (box resampling)"
                    src="../../assets/images/outputs/draw/resample/starry-night-resample-box.webp"
                />
            </div>

        === "'bilinear'"
            <div align="center">
                <img
                    alt="Starry Night (bilinear resampling)"
                    src="../../assets/images/outputs/draw/resample/starry-night-resample-bilinear.webp"
                />
            </div>

        === "'hamming'"
            <div align="center">
                <img
                    alt="Starry Night (hamming resampling)"
                    src="../../assets/images/outputs/draw/resample/starry-night-resample-hamming.webp"
                />
            </div>

        === "'bicubic'"
            <div align="center">
                <img
                    alt="Starry Night (bicubic resampling)"
                    src="../../assets/images/outputs/draw/resample/starry-night-resample-bicubic.webp"
                />
            </div>

        === "'lanczos'"
            <div align="center">
                <img
                    alt="Starry Night (lanczos resampling)"
                    src="../../assets/images/outputs/draw/resample/starry-night-resample-lanczos.webp"
                />
            </div>

### `-H`, `--height` `INTEGER`
:   *Height of output text in characters.*
    *If 0, derives from width.  [default: 0]*

    !!! info "Lines"
        `height` is the number of lines in the text output.

    ??? example
        Consider the following image:
        
        <div align="center">
            <p>
                <img alt="Zima Blue" src="../../assets/images/subjects/zima.webp" />
            </p>
            <p>
                <em>Zima Blue [Zima]</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -H 32 docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        <div align="center">
            <img
                alt="Zima Blue (with height = 32)"
                src="../../assets/images/outputs/draw/dimensions/zima-h32.webp"
            />
        </div>

### `-W`, `--width` `INTEGER`
:   *Width of output text in characters.*
    *If 0, derives from height.  [default: 0]*

    !!! info "Characters per line"
        `width` is the number of characters (including whitespace) per line in the text output.

    ??? example
        Consider the following image:
        
        <div align="center">
            <p>
                <img alt="Zima Blue" src="../../assets/images/subjects/zima.webp" />
            </p>
            <p>
                <em>Zima Blue [Zima]</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -W 32 docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        <div align="center">
            <img
                alt="Zima Blue (with width = 32)"
                src="../../assets/images/outputs/draw/dimensions/zima-w32.webp"
            />
        </div>

### `-term-h`, `--terminal-height`
:   *Sets height to terminal height.*

    ??? example
        Consider the following image:
        
        <div align="center">
            <p>
                <img alt="Zima Blue" src="../../assets/images/subjects/zima.webp" />
            </p>
            <p>
                <em>Zima Blue [Zima]</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -term-h docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        <div align="center">
            <img
                alt="Zima Blue (with terminal height)"
                src="../../assets/images/outputs/draw/dimensions/zima-term-h.webp"
            />
        </div>

    ??? bug
        When used while [piping](https://en.wikipedia.org/wiki/Pipeline_(Unix)){target=_blank},
        `height` is set to the default terminal height,
        which is usually `24`.
      
### `-term-w`, `--terminal-width`
:   *Sets width to terminal width.*

    ??? example
        Consider the following image:
        
        <div align="center">
            <p>
                <img alt="Zima Blue" src="../../assets/images/subjects/zima.webp" />
            </p>
            <p>
                <em>Zima Blue [Zima]</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -term-w docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        <div align="center">
            <img
                alt="Zima Blue (with terminal width)"
                src="../../assets/images/outputs/draw/dimensions/zima-term-w.webp"
            />
        </div>

    ??? bug
        When used while [piping](https://en.wikipedia.org/wiki/Pipeline_(Unix)){target=_blank},
        `width` is set to the default terminal width,
        which is usually `80`.

### `-h`, `--help`
:   *Show this message and exit.*

    ??? abstract "Message"
        ```
        --8<-- "docs/snippets/cli/draw/help.txt"
        ```

## Subcommands

!!! question "Styles"
    Refer to the [Styles documentation](../../styles/index.md)
    for an in-depth guide to the **image processing behind Picharsso**.

### [`braille`](braille.md)
:   Use the [Braille style](../../styles/braille.md).

### [`gradient`](gradient.md)
:   Use the [gradient style](../../styles/gradient.md).

