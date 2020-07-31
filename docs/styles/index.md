---
title: "Styles - Picharsso"
description: "An overview of the styles of Picharsso"
---

# Styles

Styles refer to the different image processing algorithms
that are performed on input images.
**They affect how images look when viewed in the text form**.

## Procedure

Although the different styles use algorithms that produce different results,
there are many *common*, yet fundamental, steps involved in the entire process.
Picharsso defines a [`BaseDrawer`][picharsso.draw.base.BaseDrawer]
that abstracts this general procedure.

### Initialization

This step **assigns values to the parameters** for the algorithms.

#### Dimensions

Picharsso provides control over the **dimensions of the output text**
with the `height` and `width` parameters.

Consider the following image:

<div align="center">
    <p>
        <img alt="Zima Blue" src="../assets/images/subjects/zima.webp" />
    </p>
    <p>
        <em>Zima Blue [Zima]</em>
    </p>
</div>

Here's what it should look like:

=== "height = 32"
    <div align="center">
        <img
            alt="Zima Blue (with height = 32)"
            src="../assets/images/outputs/draw/dimensions/zima-h32.webp"
        />
    </div>

=== "terminal height"
    <div align="center">
        <img
            alt="Zima Blue (with terminal height)"
            src="../assets/images/outputs/draw/dimensions/zima-term-h.webp"
        />
    </div>

=== "width = 32"
    <div align="center">
        <img
            alt="Zima Blue (with width = 32)"
            src="../assets/images/outputs/draw/dimensions/zima-w32.webp"
        />
    </div>

=== "terminal width"
    <div align="center">
        <img
            alt="Zima Blue (with terminal width)"
            src="../assets/images/outputs/draw/dimensions/zima-term-w.webp"
        />
    </div>

!!! info "Preserving Aspect Ratio"
    The relationship between `height` and `width` preserves the aspect ratio of the input image.

    *When either one of the dimensions is set as `0`, it derives its value from the other.*

??? error
    Assigning `0` to both `height` and `width` raises an error.
    Atleast one of the dimensions must be assigned a non-zero positive integer.

#### Resampling Filter

There are instances when an input image must be **scaled to an appropriate size**
before it can be used as input for an algorithm.
During this resizing process, pixels must sampled/ resampled
to generate the new, resized, image.

Picharsso uses the [resampling filters that come with Pillow](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#filters){target=_blank}.
The choice of the resampling filter is defined by the `resample` parameter.

Consider the following image:

<div align="center">
    <p>
        <img alt="Starry Night" src="../assets/images/subjects/starry-night.webp" />
    </p>
    <p>
        <em>Starry Night [Vincent van Gogh, 1889]</em>
    </p>
</div>

Here's what it should look like:

=== "resample = 'nearest'"
    <div align="center">
        <img
            alt="Starry Night (nearest resampling)"
            src="../assets/images/outputs/draw/resample/starry-night-resample-nearest.webp"
        />
    </div>

=== "'box'"
    <div align="center">
        <img
            alt="Starry Night (box resampling)"
            src="../assets/images/outputs/draw/resample/starry-night-resample-box.webp"
        />
    </div>

=== "'bilinear'"
    <div align="center">
        <img
            alt="Starry Night (bilinear resampling)"
            src="../assets/images/outputs/draw/resample/starry-night-resample-bilinear.webp"
        />
    </div>

=== "'hamming'"
    <div align="center">
        <img
            alt="Starry Night (hamming resampling)"
            src="../assets/images/outputs/draw/resample/starry-night-resample-hamming.webp"
        />
    </div>

=== "'bicubic'"
    <div align="center">
        <img
            alt="Starry Night (bicubic resampling)"
            src="../assets/images/outputs/draw/resample/starry-night-resample-bicubic.webp"
        />
    </div>

=== "'lanczos'"
    <div align="center">
        <img
            alt="Starry Night (lanczos resampling)"
            src="../assets/images/outputs/draw/resample/starry-night-resample-lanczos.webp"
        />
    </div>

!!! note
    All resizing operations use the same filter that is set by `resample`.

### Normalization

Pillow supports multiple [image modes](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes){target=_blank}.
For simplicity, the algorithms were designed to work on the `RGB` image mode.
Hence, images must be converted appropriately.

!!! info "White Background"
    A white background is applied to images with the `P` and `RGBA` modes.

??? abstract "Source"
    Refer to the [`ensure_rgb` function][picharsso.utils.ensure_rgb] for more information.

### Conversion

This step lies at the heart of each style.

#### Resizing

Before the `image` can be processed, it must be resized appropriately.
The **scale** of the resizing **depends on the processing algorithm**.

<div align="center">
    <img alt="Image resizing" src="../assets/images/diagrams/styles/overview/resizing.webp">
</div>

??? abstract "Source"
    Refer to the [`calculate_size` function][picharsso.draw.base.BaseDrawer.calculate_size]
    for more information.

#### Processing

The resized `image` is processed into a `text_matrix`.

<div align="center">
    <img alt="Processing an image into a text matrix" src="../assets/images/diagrams/styles/overview/processing.webp">
</div>

??? abstract "Source"
    Refer to the [`process` function][picharsso.draw.base.BaseDrawer.process]
    for more information.

### Formatting

Before it can be displayed, the `text_matrix` must be **formatted into a single string**.
The type of `formatter` used is defined by the `mode` parameter.

!!! info "Colorization"
    The `formatter` requires the original `image` and the choice of `resample` filter
    for pooling colors.
    
    Refer to the [colorization step](../formats/index.md#colorization)
    for more information.

!!! question "Formats"
    Refer to the [Formats documentation](../formats/index.md)
    to learn about the supported output formats.

## Varieties

All the following styles are implemented using a `drawer`
which inherits from the [`BaseDrawer`][picharsso.draw.base.BaseDrawer].

Consider the following image:

<div align="center">
    <p>
        <img alt="Apple logo" src="../assets/images/subjects/apple.webp" />
    </p>
    <p>
        <em>Apple Computer [Rob Janoff, 1977]</em>
    </p>
</div>

Here's what it should look like:

### Braille
:   The [Braille style](braille.md) is implemented using the
    [`BrailleDrawer`][picharsso.draw.braille.BrailleDrawer].

    <div align="center">
        <img
            alt="Apple logo in text (Braille style)"
            src="../assets/images/outputs/demo/apple-braille.webp"
        />
    </div>

### Gradient
:   The [gradient style](gradient.md) is implemented using the
    [`GradientDrawer`][picharsso.draw.gradient.GradientDrawer].

    <div align="center">
        <img
            alt="Apple logo in text (gradient style)"
            src="../assets/images/outputs/demo/apple-gradient.webp"
        />
    </div>