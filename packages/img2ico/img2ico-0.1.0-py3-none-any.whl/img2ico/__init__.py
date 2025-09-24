"""
img2ico
=======

A simple CLI tool and Python library to convert images into multi-resolution
favicon (.ico) files.

Features
--------
- Convert PNG, JPG, WEBP, BMP to ICO
- Optional SVG support (requires cairosvg)
- Embed multiple icon sizes in one .ico file (16x16, 32x32, 48x48 by default)
- Command-line interface with argparse

Example
-------
Run from the command line:

    img2ico input.png -o favicon.ico -s 16 32 48

Or use as a Python module:

    from img2ico import convert_to_ico
    convert_to_ico("logo.png", "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

License
-------
MIT
"""

__version__ = "0.1.0"
__license__ = "MIT"
__author__ = "yu9824"
__copyright__ = "Copyright © 2025 yu9824"

from .__main__ import convert_to_ico

__all__ = ("convert_to_ico",)
