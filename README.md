# Noisy Image Generator

This script creates an image with subtle noise on a specified base color.

The noise is designed to be virtually indistinguishable to the human eye, making the image appear as a uniform color while containing diverse pixel variations.
But the amount of noise can be specified to be as large (and noticeable) as desired.

## Installation

To run this script, you need Python and Poetry for dependency management. If you haven't installed Poetry yet, please follow the instructions on [Poetry's official documentation](https://python-poetry.org/docs/).

### Setting Up

1. **Clone or download this repository** to your local machine.

2. **Open a terminal** and navigate to the directory where the script is located.

3. **Install dependencies** by running the following command:

```sh
poetry install
```

This will create a virtual environment and install the required packages, including PIL (Pillow), as defined in `pyproject.toml`.

## Usage

The script can be executed via the command line with arguments to customize the output image:

```sh
poetry run python main.py --base_color "#hexcolor" --width 800 --height 600 --variation 2 --output "path/to/your_image.png"
```

## Command Line Arguments

- `--base_color`: The base color of the image in hex format (e.g., #123ABC). Default is #ffffff.
- `--width`: The width of the image in pixels. Default is 1000.
- `--height`: The height of the image in pixels. Default is 1000.
- `--variation`: The range of variation for the noise added to each color channel (0-255). Default is 2.
- `--output`: The output path for the generated image. Default is noisy_image.png.

Example
Generate a 1024x768 image with a subtle blue (#0000FF) noise:

```sh
poetry run python main.py --base_color "#0000FF" --width 1024 --height 768 --variation 2 --output "blue_noisy_image.png"
```
