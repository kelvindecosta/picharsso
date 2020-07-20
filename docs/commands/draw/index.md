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

        --8<-- "docs/snippets/embed/subjects/instagram.html"

        ```bash
        picharsso draw [-c] -H 32 docs/assets/images/subjects/instagram.webp gradient
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/chunks/format/colorize.md"

### `-m`, `--mode` [`ansi`|`html`]
:   *Format mode for output text.  [default: ansi]*

    --8<-- "docs/snippets/references/formats.md"

### `-r`, `--resample` [`nearest`|`box`|`bilinear`|`hamming`|`bicubic`|`lanczos`]
:   *Resampling filter.  [default: nearest]*

    ??? example
        Consider the following image:

        --8<-- "docs/snippets/embed/subjects/starry-night.html"

        ```bash
        picharsso draw -c -term-h -r <resample> docs/assets/images/subjects/starry-night.webp gradient -s "█"
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/chunks/draw/resample.md"

### `-H`, `--height` `INTEGER`
:   *Height of output text in characters.*
    *If 0, derives from width.  [default: 0]*

    !!! info "Lines"
        `height` is the number of lines in the text output.

    ??? example
        Consider the following image:
        
        --8<-- "docs/snippets/embed/subjects/zima.html"
        
        ```bash
        picharsso draw -c -H 32 docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/embed/outputs/draw/dimensions/zima-h32.html"

### `-W`, `--width` `INTEGER`
:   *Width of output text in characters.*
    *If 0, derives from height.  [default: 0]*

    !!! info "Characters per line"
        `width` is the number of characters (including whitespace) per line in the text output.

    ??? example
        Consider the following image:
        
        --8<-- "docs/snippets/embed/subjects/zima.html"

        ```bash
        picharsso draw -c -W 32 docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/embed/outputs/draw/dimensions/zima-w32.html"

### `-term-h`, `--terminal-height`
:   *Sets height to terminal height.*

    ??? example
        Consider the following image:
        
        --8<-- "docs/snippets/embed/subjects/zima.html"

        ```bash
        picharsso draw -c -term-h docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/embed/outputs/draw/dimensions/zima-term-h.html"

    ??? bug
        When used while [piping](https://en.wikipedia.org/wiki/Pipeline_(Unix)),
        `height` is set to the default terminal height,
        which is usually `24`.
      
### `-term-w`, `--terminal-width`
:   *Sets width to terminal width.*

    ??? example
        Consider the following image:
        
        --8<-- "docs/snippets/embed/subjects/zima.html"

        ```bash
        picharsso draw -c -term-w docs/assets/images/subjects/zima.webp gradient
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/embed/outputs/draw/dimensions/zima-term-w.html"

    ??? bug
        When used while [piping](https://en.wikipedia.org/wiki/Pipeline_(Unix)),
        `width` is set to the default terminal width,
        which is usually `80`.

### `-h`, `--help`
:   *Show this message and exit.*

    ??? abstract "Message"
        ```
        --8<-- "docs/snippets/cli/draw/help.txt"
        ```

## Subcommands

--8<-- "docs/snippets/references/styles.md"

### [`braille`](/commands/draw/braille/)
:   Use the [Braille style](/styles/braille/).

### [`gradient`](/commands/draw/gradient/)
:   Use the [gradient style](/styles/gradient/).

