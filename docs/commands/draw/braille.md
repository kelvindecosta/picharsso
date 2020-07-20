---
title: "picharsso draw braille - CLI - Picharsso"
description: "Use the Braille style."
---

# `picharsso draw braille`

*Use the [Braille style](/styles/braille/).*

--8<-- "docs/snippets/chunks/draw/styles/braille/example.md"

## Usage

```bash
picharsso draw braille [options]
```

## Options

### `-t`, `--threshold` `INTEGER` `RANGE`
:   *Threshold pixel luminance (from grayscale). [default: 64]*

    ??? example
        Consider the following image:

        --8<-- "docs/snippets/embed/subjects/contributions.html"

        ```bash
        picharsso draw -c -H 32 docs/assets/images/subjects/contributions.webp braille -t <threshold>
        ```

        Here's what it should look like:
        
        --8<-- "docs/snippets/chunks/draw/styles/braille/threshold.md"


### `-h`, `--help`
:   *Show this message and exit.*

    ??? abstract "Message"
        ```
        --8<-- "docs/snippets/cli/draw/braille/help.txt"
        ```
