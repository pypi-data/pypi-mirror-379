from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

from PIL import Image

from img2ico import __version__
from img2ico.logging import get_child_logger
from img2ico.utils import is_installed

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

if HAS_CAIROSVG := is_installed("cairosvg"):
    import cairosvg  # type: ignore


_logger = get_child_logger(__name__)


def convert_to_ico(
    input_path: Path,
    output_path: Path,
    sizes: Sequence[tuple[int, int]],
) -> None:
    """
    Convert an image file to a multi-resolution ICO file.

    This function loads an image, converts it to RGBA (to preserve transparency),
    and saves it as an `.ico` file containing multiple icon resolutions.

    Parameters
    ----------
    input_path : Path
        Path to the source image file (PNG, JPG, WEBP, BMP, etc.).
    output_path : Path
        Path to the output `.ico` file.
    sizes : Sequence[tuple[int, int]]
        A sequence of (width, height) tuples specifying which icon sizes
        to embed in the resulting `.ico` file.
        Example: [(16, 16), (32, 32), (48, 48)]

    Returns
    -------
    None
        This function writes the `.ico` file to disk and prints a success message.

    Raises
    ------
    FileNotFoundError
        If the input image file does not exist.
    OSError
        If the image cannot be opened or saved.

    Example
    -------
    >>> from pathlib import Path
    >>> convert_to_ico(
    ...     input_path=Path("logo.png"),
    ...     output_path=Path("favicon.ico"),
    ...     sizes=[(16, 16), (32, 32), (48, 48)],
    ... )
    ✅ Conversiosn complete: favicon.ico
    """
    img = Image.open(input_path)
    img = img.convert("RGBA")
    img.save(output_path, format="ICO", sizes=sizes)
    _logger.info(f"✅ Conversion complete: {output_path}")


def main(cli_args: Sequence[str], prog: Optional[str] = None) -> None:
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Convert an image file to a favicon (.ico) file.",
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input image file (png, jpg, webp, bmp, svg, etc.)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output ICO file name (default: same name as input with .ico extension)",
    )
    parser.add_argument(
        "-s",
        "--sizes",
        nargs="+",
        default=["16", "32", "48"],
        help="Icon sizes to include (e.g., 16 32 48). Default: 16 32 48",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Show current version",
        version=f"%(prog)s: {__version__}",
    )

    args = parser.parse_args(cli_args)
    input_path = args.input
    output_path = args.output or input_path.with_suffix(".ico")
    sizes = [(int(s), int(s)) for s in args.sizes]

    # Handle SVG input
    if input_path.suffix.lower() == ".svg":
        if not HAS_CAIROSVG:
            raise RuntimeError(
                "To convert SVG, install cairosvg: pip install cairosvg"
            )
        tmp_png = input_path.with_suffix(".tmp.png")
        cairosvg.svg2png(url=str(input_path), write_to=str(tmp_png))
        convert_to_ico(tmp_png, output_path, sizes)
        tmp_png.unlink()  # remove temporary file
    else:
        convert_to_ico(input_path, output_path, sizes)


def entrypoint() -> None:
    main(sys.argv[1:], prog="img2ico")


if __name__ == "__main__":
    entrypoint()

__all__ = ("main", "entrypoint")
