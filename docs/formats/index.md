---
title: "Formats - Picharsso"
description: "An overview of the output formats of Picharsso"
---

# Formats

After an `image` is coverted to a `text_matrix`,
it must be formatted before it can be output.

## Procedure

There are steps involved in this process that are common to
all `formatters`.
Picharsso defines a [`BaseFormatter`][picharsso.format.base.BaseFormatter]
that abstracts this general procedure.

### Initialization

This step assigns values to the parameters for the algorithms.

#### Color

The `colorize` parameter controls whether the output text must include the colors from the image.

Consider the following image:

--8<-- "docs/snippets/embed/subjects/instagram.html"

Here's what it should look like:

--8<-- "docs/snippets/chunks/format/colorize.md"

#### Vectorization

The `vcolor` attribute is a vectorized version of the `color` method.

### Translation

The elements of the `text_matrix` are encoded in the Unicode standard.

Depending on the output format, these characters must be translated accordingly.

??? abstract "Source"
    Refer to the [`translate` function][picharsso.format.base.BaseFormatter.translate] for more information.

### Colorization

Colors are pooled from the original `image` by resizing it to the dimensions of the output text.
This ensures that each character has a unique pixel, and thus, a unique color.

With the vectorized `color` method, `vcolor`, the elements of the `text_matrix`
are transformed into strings of text that represent
the original character as well as its color.

<div align="center">
    <img alt="Text matrix colorization" src="/assets/images/diagrams/formats/overview/colorization.webp">
</div>

??? abstract "Source"
    Refer to the [`color` function][picharsso.format.base.BaseFormatter.color] for more information.

### Unification

Finally, the `text_matrix` is unified into a single string of text.
This text, when viewed through a means supporting the particular format,
should look like the original image.

??? abstract "Source"
    Refer to the [`unify` function][picharsso.format.base.BaseFormatter.unify] for more information.

## Varities

All the following formats are implemented by a `formatter` 
which inherits from the [`BaseFormatter`][picharsso.format.base.BaseFormatter].

### ANSI
:   The [ANSI format](/formats/ansi/) is implemented by the [`AnsiFormater`][picharsso.format.ansi.AnsiFormatter].

### HTML
:   The [HTML format](/formats/html/) is implemented by the [`HtmlFormater`][picharsso.format.html.HtmlFormatter].
