---
title: "Gradient - Styles - Picharsso"
description: "The gradient based text art style"
---

# Gradient

This style uses [Unicode characters](https://en.wikipedia.org/wiki/Unicode){target=_blank}.

??? example "Example"
    Consider the following image:

    <div align="center">
        <p>
            <img alt="Apple logo" src="../../assets/images/subjects/apple.webp" />
        </p>
        <p>
            <em>Apple Computer [Rob Janoff, 1977]</em>
        </p>
    </div>

    Here's what it should look like:

    <div align="center">
        <img
            alt="Apple logo in text (gradient style)"
            src="../../assets/images/outputs/demo/apple-gradient.webp"
        />
    </div>

## Procedure

This style is implemented using the [`GradientDrawer`][picharsso.draw.gradient.GradientDrawer].

!!! question "Styling"
    Refer to the [procedure](./index.md#procedure) outlined in the Styles documentation
    for an overview of the **steps common to all styles**.

### Initialization

#### Charset

The `charset` parameter is a string containing characters **ordered by their
perceived brightness**.

Consider the following image:

<div align="center">
    <p>
        <img alt="Slack logo" src="../../assets/images/subjects/slack.webp" />
    </p>
    <p>
        <em>Slack</em>
    </p>
</div>

Here's what it should look like:

=== "charset = ' :!?PG@' (default)"
    <div align="center">
        <img
            alt="Slack logo in text (default charset)"
            src="../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-default.webp"
        />
    </div>

=== "'.'"
    <div align="center">
        <img
            alt="Slack logo in text (dot charset)"
            src="../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-dot.webp"
        />
    </div>

=== "'#'"
    <div align="center">
        <img
            alt="Slack logo in text (hash charset)"
            src="../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-hash.webp"
        />
    </div>

=== "'█'"
    <div align="center">
        <img
            alt="Slack logo in text (block charset)"
            src="../../assets/images/outputs/draw/styles/gradient/charset/slack-gradient-charset-block.webp"
        />
    </div>

#### Negative

The `negative` parameter controls whether the `charset` must be **reversed**.

Consider the following image:

<div align="center">
    <p>
        <img alt="GitHub logo" src="../../assets/images/subjects/github.webp" />
    </p>
    <p>
        <em>GitHub</em>
    </p>
</div>

Here's what it should look like:

=== "negative = False"
    <div align="center">
        <img
            alt="GitHub logo in text"
            src="../../assets/images/outputs/draw/styles/gradient/negative/github-gradient-normal.webp"
        />
    </div>

=== "True"
    <div align="center">
        <img
            alt="GitHub logo in text (negative)"
            src="../../assets/images/outputs/draw/styles/gradient/negative/github-gradient-negative.webp"
        />
    </div>

#### Matrices

The `charset_array` attribute holds a NumPy [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html){target=_blank}
containing all the characters in the `charset`.

### Conversion

#### Resizing

Assuming the output text should have the dimensions `text_height` and `text_width`,
the image must be resized according to the following criteria:

*   `image_height = text_height`.
*   `image_width = text_width`.
*   If either `image_height` or `image_width` is `0`,
    it is derived from the other by preserving the aspect ratio of the original image.

Following the above algorithm, **each pixel** of the resized `image`
will be assigned to **one character** in the output text.

??? abstract "Source"
    Refer to the [`calculate_size` function][picharsso.draw.gradient.GradientDrawer.calculate_size]
    for more information.

#### Processing

1. The resized `image` is first converted to its grayscale.
2. The image matrix is normalized such that the grayscale range shifts from `(0, 255)` to `(0, len(charset))`.
3. The `charset_array` is indexed with the resultant "indices" matrix,
    giving the final `text_matrix`.

<div align="center">
    <img alt="Processing an image into a text matrix (gradient style)" src="../../assets/images/diagrams/styles/gradient/processing.webp">
</div>

??? abstract "Source"
    Refer to the [`process` function][picharsso.draw.gradient.GradientDrawer.process]
    for more information.
