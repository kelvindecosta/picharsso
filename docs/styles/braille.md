---
title: "Braille - Styles - Picharsso"
description: "The Braille based text art style"
---

# Braille

This style uses the characters of the [Braille writing system](https://en.wikipedia.org/wiki/Braille).

--8<-- "docs/snippets/chunks/draw/styles/braille/example.md"

!!! info "Encoding"
    Traditional Braille characters are made up of `6` dots (&#x283F;).
    Since each dot could be in one of `2` states (raised or lowered),
    there are a total of `64` unique combinations.

    In [Unicode](https://en.wikipedia.org/wiki/Unicode), braille is represented in a block,
    the [Braille Patterns](https://en.wikipedia.org/wiki/Braille_Patterns).
    There are `256` unique characters each in its own 8-dot cell (&#x28FF;).

## Procedure

This style is implemented using the [`BrailleDrawer`][picharsso.draw.braille.BrailleDrawer].

--8<-- "docs/snippets/references/styling.md"

### Initialization

#### Threshold

The `threshold` parameter **filters out pixels** of the input image
whose **grayscale intensities are lesser** than it.

Consider the following image:

--8<-- "docs/snippets/embed/subjects/contributions.html"

Here's what it should look like:

--8<-- "docs/snippets/chunks/draw/styles/braille/threshold.md"

#### Matrices

The `kernel` attribute holds a NumPy [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)
containing the following matrix:

$$
kernel = 
\begin{bmatrix}
1 & 8\\
2 & 16\\
4 & 32\\
64 & 128\end{bmatrix}
$$

The Unicode encoding of the 8-dot cell Braille system
is done by assigning each of the dots a power of `2`.
Each character in the Braille Patterns block has a unique Unicode value
that is obtained by summing these powers.

The `charset_array` attribute holds another NumPy [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)
containing all 256 Braille characters.

### Conversion

#### Resizing

Assuming the output text should have the dimensions `text_height` and `text_width`,
the image must be resized according to the following criteria:

*   `image_height = 4 * text_height`.
*   `image_width = 2 * text_width`.
*   If either `image_height` or `image_width` is `0`,
    it is derived from the other by preserving the aspect ratio of the original image.

Following the above algorithm, **each pixel** of the resized `image`
will be **assigned to one dot** (Braille character dot) in the output text.

??? abstract "Source"
    Refer to the [`calculate_size` function][picharsso.draw.braille.BrailleDrawer.calculate_size]
    for more information.

#### Processing

1. The resized `image` is first converted to its grayscale.
2. Each pixel is set to either `0` or `1` based on whether
    its grayscale intensity is below or above the `threshold`.
3. A convolution operation is performed on this filtered image
    using the `kernel` matrix.
    The resultant matrix has the ofsetted Unicode values for
    the corresponding Braille character.
4. The `charset_array` is indexed with the resultant "indices" matrix,
    giving the final `text_matrix`.

<div align="center">
    <img alt="Processing an image into a text matrix (Braille style)" src="/assets/images/diagrams/styles/braille/processing.webp">
</div>

??? abstract "Source"
    Refer to the [`process` function][picharsso.draw.braille.BrailleDrawer.process]
    for more information.
