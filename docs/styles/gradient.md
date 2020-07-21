---
title: "Gradient - Styles - Picharsso"
description: "The gradient based text art style"
---

# Gradient

This style uses [Unicode characters](https://en.wikipedia.org/wiki/Unicode).

--8<-- "docs/snippets/chunks/draw/styles/gradient/example.md"

## Procedure

This style is implemented using the [`GradientDrawer`][picharsso.draw.gradient.GradientDrawer].

--8<-- "docs/snippets/references/styling.md"

### Initialization

#### Charset

The `charset` parameter is a string containing characters **ordered by their
perceived brightness**.

Consider the following image:

--8<-- "docs/snippets/embed/subjects/slack.html"

Here's what it should look like:

--8<-- "docs/snippets/chunks/draw/styles/gradient/charset.md"

#### Negative

The `negative` parameter controls whether the `charset` must be **reversed**.

Consider the following image:

--8<-- "docs/snippets/embed/subjects/github.html"

Here's what it should look like:

--8<-- "docs/snippets/chunks/draw/styles/gradient/negative.md"

#### Matrices

The `charset_array` attribute holds a NumPy [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)
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
    <img alt="Processing an image into a text matrix (gradient style)" src="/assets/images/diagrams/styles/gradient/processing.webp">
</div>

??? abstract "Source"
    Refer to the [`process` function][picharsso.draw.gradient.GradientDrawer.process]
    for more information.
