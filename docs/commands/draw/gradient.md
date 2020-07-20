---
title: "picharsso draw gradient - CLI - Picharsso"
description: "Use the gradient style."
---

# `picharsso draw gradient`

*Use the [gradient style](/styles/gradient/).*

--8<-- "docs/snippets/chunks/draw/styles/gradient/example.md"

## Usage

```bash
picharsso draw gradient [options]
```

## Options:

###  `-s`, `--charset` `TEXT`
:   *Character set ordered by increasing 'brightness'. [default:  :!?PG@]*

    ??? example
        Consider the following image:

        --8<-- "docs/snippets/embed/subjects/slack.html"

        ```bash
        picharsso draw -c -H 32 docs/assets/images/subjects/slack.webp gradient -s <charset>
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/chunks/draw/styles/gradient/charset.md"

###  `-n`, `--negative`
:   Whether to invert output text brightness.

    ??? example
        Consider the following image:

        --8<-- "docs/snippets/embed/subjects/github.html"

        ```bash
        picharsso draw -H 32 docs/assets/images/subjects/github.webp gradient [-n]
        ```

        Here's what it should look like:

        --8<-- "docs/snippets/chunks/draw/styles/gradient/negative.md"

###  `-h`, `--help`
:   *Show this message and exit.*

    ??? abstract "Message"
        ```
        --8<-- "docs/snippets/cli/draw/gradient/help.txt"
        ```
