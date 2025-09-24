# img2ico

<!-- badges -->
[![CI](https://github.com/yu9824/img2ico/actions/workflows/CI.yml/badge.svg)](https://github.com/yu9824/img2ico/actions/workflows/CI.yml)
[![docs](https://github.com/yu9824/img2ico/actions/workflows/docs.yml/badge.svg)](https://github.com/yu9824/img2ico/actions/workflows/docs.yml)
[![release-pypi](https://github.com/yu9824/img2ico/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/yu9824/img2ico/actions/workflows/release-pypi.yml)

<!--
[![python_badge](https://img.shields.io/pypi/pyversions/img2ico)](https://pypi.org/project/img2ico/)
[![license_badge](https://img.shields.io/pypi/l/img2ico)](https://pypi.org/project/img2ico/)
[![PyPI version](https://badge.fury.io/py/img2ico.svg)](https://pypi.org/project/img2ico/)
[![Downloads](https://static.pepy.tech/badge/img2ico)](https://pepy.tech/project/img2ico)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/img2ico.svg)](https://anaconda.org/conda-forge/img2ico)
[![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/img2ico.svg)](https://anaconda.org/conda-forge/img2ico)
-->

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://github.com/python/mypy)
<!-- /badges -->

A simple CLI tool and Python library to convert images into multi-resolution favicon (`.ico`) files.

## Features

- Convert **PNG**, **JPG**, **WEBP**, **BMP** to ICO
- Optional **SVG** support (requires `cairosvg`)
- Embed multiple icon sizes in one `.ico` file (`16x16`, `32x32`, `48x48` by default)
- Easy to use **CLI** and **Python API**

## Installation

```bash
pip install pillow
# Optional: for SVG input support
pip install cairosvg
````

Or if you publish this as a package:

```bash
pip install img2ico
# with SVG support
pip install img2ico[svg]
```

## Usage

### CLI

```bash
img2ico input.png -o favicon.ico -s 16 32 48
```

**Options:**

| Option          | Description                                                      |
| --------------- | ---------------------------------------------------------------- |
| `-o, --output`  | Output file name (default: same as input, with `.ico` extension) |
| `-s, --sizes`   | Icon sizes to embed (space-separated). Default: `16 32 48`       |
| `-v, --version` | Show current version                                             |

### Python API

```python
from pathlib import Path
from img2ico import convert_to_ico

convert_to_ico(
    input_path=Path("logo.png"),
    output_path=Path("favicon.ico"),
    sizes=[(16, 16), (32, 32), (48, 48)],
)
```

## Recommended Sizes

For favicon usage, it is recommended to include:

* `16x16` – browser tab, old browsers
* `32x32` – high DPI displays
* `48x48` – Windows desktop icons

You can also add `64x64` or larger if you want to future-proof, but it is not strictly necessary.

## Development

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourname/img2ico.git
cd img2ico
pip install -e ".[svg]"
```

Run tests or try the CLI:

```bash
python -m img2ico input.png
```

## License

MIT


