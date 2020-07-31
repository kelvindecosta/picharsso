---
title: "picharsso draw gradient - CLI - Picharsso"
description: "Use the gradient style."
---

# `picharsso draw gradient`

*Use the [gradient style](../../styles/gradient.md).*

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
            alt="Apple logo in text (gradient style)"
            src="../../../assets/images/outputs/demo/apple-gradient.webp"
        />
    </div>

## Usage

```bash
picharsso draw gradient [options]
```

## Options:

###  `-s`, `--charset` `TEXT`
:   *Character set ordered by increasing 'brightness'. [default:  :!?PG@]*

    ??? example
        Consider the following image:

        <div align="center">
            <p>
                <img alt="Slack logo" src="../../../assets/images/subjects/slack.webp" />
            </p>
            <p>
                <em>Slack</em>
            </p>
        </div>

        ```bash
        picharsso draw -c -H 32 docs/assets/images/subjects/slack.webp gradient -s <charset>
        ```

        Here's what it should look like:

        === "charset = ' :!?PG@' (default)"
            <div align="center">
                <img
                    alt="Slack logo in text (default charset)"
                    src="../../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-default.webp"
                />
            </div>

        === "'.'"
            <div align="center">
                <img
                    alt="Slack logo in text (dot charset)"
                    src="../../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-dot.webp"
                />
            </div>

        === "'#'"
            <div align="center">
                <img
                    alt="Slack logo in text (hash charset)"
                    src="../../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-hash.webp"
                />
            </div>

        === "'█'"
            <div align="center">
                <img
                    alt="Slack logo in text (block charset)"
                    src="../../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-block.webp"
                />
            </div>

###  `-n`, `--negative`
:   Whether to invert output text brightness.

    ??? example
        Consider the following image:

        <div align="center">
            <p>
                <img alt="GitHub logo" src="../../../assets/images/subjects/github.webp" />
            </p>
            <p>
                <em>GitHub</em>
            </p>
        </div>

        ```bash
        picharsso draw -H 32 docs/assets/images/subjects/github.webp gradient [-n]
        ```

        Here's what it should look like:

        === "negative = False"
            <div align="center">
                <img
                    alt="GitHub logo in text"
                    src="../../../assets/images/outputs/draw/styles/gradient/negative/github-gradient-normal.webp"
                />
            </div>

        === "True"
            <div align="center">
                <img
                    alt="GitHub logo in text (negative)"
                    src="../../../assets/images/outputs/draw/styles/gradient/negative/github-gradient-negative.webp"
                />
            </div>

###  `-h`, `--help`
:   *Show this message and exit.*

    ??? abstract "Message"
        ```
        --8<-- "docs/snippets/cli/draw/gradient/help.txt"
        ```
