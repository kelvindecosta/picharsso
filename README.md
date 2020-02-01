# Picharsso

<p align=center>

  <img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/assets/readme/logo.png" height="200px"/>

  <br>
  <span>A command line utility to convert an image to text art.</span>
  <br>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
  <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a target="_blank" href="https://pypi.python.org/pypi/picharsso/"><img alt="pypi package" src="https://badge.fury.io/py/picharsso.svg"></a>
</p>

<p align="center">
  <a href="#examples">Examples</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/kelvindecosta/picharsso/wiki">Wiki</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#citation">Citation</a>

</p>

## Installation

```bash
pip install picharsso
```

## Usage

With the `-h` flag, the program outputs usage information.

```
usage: picharsso [-h] {config,art} ...

Picharsso

positional arguments:
  {config,art}
    config      show config path
    art         transform image to text art

optional arguments:
  -h, --help    show this help message and exit
```

For an in depth guide to the functionality of the program, navigate to the [Wiki](https://github.com/kelvindecosta/picharsso/wiki).

## Examples

Consider the following poster:

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/assets/readme/example.jpg" width="300"></p>

The following images are screenshots of the outputs of different runs on a terminal with a dark background.

### ASCII

#### Grayscale

```bash
picharsso art ascii assets/readme/example.jpg -H
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/assets/readme/ascii-gray.png" width="300"></p>

#### Color

```bash
picharsso art ascii assets/readme/example.jpg -H -c
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/assets/readme/ascii-color.png" width="300"></p>

### Braille

#### Grayscale

```bash
picharsso art braille assets/readme/example.jpg -H
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/assets/readme/braille-gray.png" width="300"></p>

#### Color

```bash
picharsso art braille assets/readme/example.jpg -H -c
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/picharsso/master/assets/readme/braille-color.png" width="300"></p>

## Citation

If you use this implementation in your work, please cite the following:

```
@misc{decosta2019picharsso,
    author = {Kelvin DeCosta},
    title = {Picharsso},
    year = {2019},
    howpublished = {\url{https://github.com/kelvindecosta/picharsso}},
}
```
