# Image to Text Art

A command line utility to convert an image to text art.

## Installation

```bash
pip install image-to-text-art
```

## Usage

With the `-h` flag, the program outputs usage information.

```
usage: img2txt [-h] {config,art} ...

Image to Text Art

positional arguments:
  {config,art}
    config      show config path
    art         transform image to text art

optional arguments:
  -h, --help    show this help message and exit
```

For an in depth guide to the functionality of the program, navigate to the [Wiki](https://github.com/kelvindecosta/image-to-text-art/wiki).

## Example

Consider the following poster:

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/image-to-text-art/master/assets/readme/example.jpg" width="300"></p>

The following images are screenshots of the outputs of different runs on a terminal with a dark background.

### ASCII

#### Grayscale

```bash
img2txt art ascii assets/readme/example.jpg -H
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/image-to-text-art/master/assets/readme/ascii-gray.png" width="300"></p>

#### Color

```bash
img2txt art ascii assets/readme/example.jpg -H -c
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/image-to-text-art/master/assets/readme/ascii-color.png" width="300"></p>

### Braille

#### Grayscale

```bash
img2txt art braille assets/readme/example.jpg -H
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/image-to-text-art/master/assets/readme/braille-gray.png" width="300"></p>

#### Color

```bash
img2txt art braille assets/readme/example.jpg -H -c
```

<p align="center"><img src="https://raw.githubusercontent.com/kelvindecosta/image-to-text-art/master/assets/readme/braille-color.png" width="300"></p>