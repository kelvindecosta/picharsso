---
title: "picharsso draw braille - CLI - Picharsso"
description: "Use the Braille style."
---

# `picharsso draw braille`

*Use the [Braille style](../../styles/braille.md).*

??? example "Example"
    Consider the following image:

    <div align="center">
        <p>
            <img alt="Apple logo" src="../../../assets/images/subjects/apple.webp" />
        </p>
        <p>
            <em>Apple Computer [Rob Janoff, 1977]</em>
        </p>
    </div>

    Here's what it should look like:

    <div align="center">
        <img
            alt="Apple logo in text (Braille style)"
            src="../../../assets/images/outputs/demo/apple-braille.webp"
        />
    </div>

## Usage

```bash
picharsso draw braille [options]
```

## Options

### `-t`, `--threshold` `INTEGER` `RANGE`
:   *Threshold pixel luminance (from grayscale). [default: 64]*

    ??? example
        Consider the following image:

        <div align="center">
            <p>
                <img alt="Contributions" src="../../../assets/images/subjects/contributions.webp" />
            </p>
            <p>
                <em>Tiles ressembling GitHub contributions</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -H 32 docs/assets/images/subjects/contributions.webp braille -t <threshold>
        ```

        Here's what it should look like:

        === "threshold = 0"
            <div align="center">
                <img
                    alt="Contributions in text (Braille Threshold 0)"
                    src="../../../assets/images/outputs/draw/styles/braille/threshold/contributions-braille-t0.webp"
                />
            </div>

        === "70"
            <div align="center">
                <img
                    alt="Contributions in text (Braille Threshold 70)"
                    src="../../../assets/images/outputs/draw/styles/braille/threshold/contributions-braille-t70.webp"
                />
            </div>

        === "108"
            <div align="center">
                <img
                    alt="Contributions in text (Braille Threshold 108)"
                    src="../../../assets/images/outputs/draw/styles/braille/threshold/contributions-braille-t108.webp"
                />
            </div>

        === "168"
            <div align="center">
                <img
                    alt="Contributions in text (Braille Threshold 168)"
                    src="../../../assets/images/outputs/draw/styles/braille/threshold/contributions-braille-t168.webp"
                />
            </div>

        === "210"
            <div align="center">
                <img
                    alt="Contributions in text (Braille Threshold 210)"
                    src="../../../assets/images/outputs/draw/styles/braille/threshold/contributions-braille-t210.webp"
                />
            </div>

### `-h`, `--help`
:   *Show this message and exit.*

    ??? abstract "Message"
        ```
        --8<-- "docs/snippets/cli/draw/braille/help.txt"
        ```
