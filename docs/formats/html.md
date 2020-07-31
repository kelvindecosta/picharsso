---
title: "HTML - Formats - Picharsso"
description: "The HTML format"
---

# HTML

This format supports [HTML](https://en.wikipedia.org/wiki/HTML){target=_blank}.

## Procedure

This format is implemented by the [`HtmlFormatter`][picharsso.format.html.HtmlFormatter].

!!! question "Formatting"
    Refer to the [procedure](./index.md#procedure) outlined in the Formats documentation
    for an overview of the **steps common to all formats**.

### Translation

This format requires some characters to be translated
to their equivalent [HTML character entities](https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references){target=_blank}.

??? abstract "Source"
    Refer to the [`translate` function][picharsso.format.html.HtmlFormatter.translate]
    for more information.

### Colorization

Color is applied to each element in the `text_matrix` by
wrapping it in a styled `<span>` element.

??? abstract "Source"
    Refer to the [`color` function][picharsso.format.html.HtmlFormatter.color]
    for more information.

### Unification

Elements of each row of the `text_matrix` are joined to form
lines.
All lines are wrapped in a `<div>` elemen each.
The entire text output is wrapped in a `<div>` element.

??? abstract "Source"
    Refer to the [`unify` function][picharsso.format.html.HtmlFormatter.unify]
    for more information.
