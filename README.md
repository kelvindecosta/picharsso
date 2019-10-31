# Image to Text Art

A command line utility to convert an image to text art.

## Installation

```bash
pip install image-to-text-art
```

## Usage

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

* `art`

  ```
  usage: img2txt art [-h] {ascii,braille} ...

  positional arguments:
    {ascii,braille}
      ascii          apply ASCII
      braille        apply Braille

  optional arguments:
    -h, --help       show this help message and exit
  ```

  * `ascii`
  
  ```
  usage: img2txt art ascii [-h] [-c] [-W [width]] [-H [height]] [-o {ansi,html}]
                         [-f OUTPUT_FILE] [-q] [-s {0,1}] [-n]
                         image

  positional arguments:
    image                 path to image

  optional arguments:
    -h, --help            show this help message and exit
    -c, --color           keep color
    -W [width], --width [width]
                          width of output in characters, flags to fit terminal
    -H [height], --height [height]
                          height of output in characters, flags to fit terminal
    -o {ansi,html}, --output-type {ansi,html}
                          type of output
    -f OUTPUT_FILE, --output-file OUTPUT_FILE
                          path to output file
    -q, --quiet           disable console output
    -s {0,1}, --charset {0,1}
                          choice of charset (options available in config)
    -n, --negative        reverse grayscale
  ```

  * `braille`

  ```
  usage: img2txt art braille [-h] [-c] [-W [width]] [-H [height]]
                           [-o {ansi,html}] [-f OUTPUT_FILE] [-q]
                           [-t threshold]
                           image

  positional arguments:
    image                 path to image

  optional arguments:
    -h, --help            show this help message and exit
    -c, --color           keep color
    -W [width], --width [width]
                          width of output in characters, flags to fit terminal
    -H [height], --height [height]
                          height of output in characters, flags to fit terminal
    -o {ansi,html}, --output-type {ansi,html}
                          type of output
    -f OUTPUT_FILE, --output-file OUTPUT_FILE
                          path to output file
    -q, --quiet           disable console output
    -t threshold, --threshold threshold
                          threshold pixel intensity
  ```

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