---
title: "ANSI - Formats - Picharsso"
description: "The ANSI format"
---

# ANSI

This format supports [ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code){target=_blank}.

!!! info "Default"
    Since it can be used to create **plain text documents**,
    this format is chosen as the **default**.

## Procedure

This format is implemented by the [`AnsiFormatter`][picharsso.format.ansi.AnsiFormatter].

!!! question "Formatting"
    Refer to the [procedure](./index.md#procedure) outlined in the Formats documentation
    for an overview of the **steps common to all formats**.

### Translation

This format doesn't require any translation.

??? abstract "Source"
    Refer to the [`translate` function][picharsso.format.ansi.AnsiFormatter.translate]
    for more information.

### Colorization

Using the [`sty` Python library](https://sty.mewo.dev/){target=_blank},
color is applied to the elements of the `text_matrix`.

??? abstract "Source"
    Refer to the [`color` function][picharsso.format.ansi.AnsiFormatter.color]
    for more information.

### Unification

Elements of each row of the `text_matrix` are joined to form
lines, which are further joined to form one huge string of text.

??? abstract "Source"
    Refer to the [`unify` function][picharsso.format.ansi.AnsiFormatter.unify]
    for more information.
