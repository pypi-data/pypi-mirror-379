"""
This is the core Visuscript CLI utility, which creates a movie from a Python script.
See :class:`~visuscript.scene.Scene` for writing such a script.

Technically, this utility could create a movie from any Python script that outputs a stream of SVG elements
to :attr:`visuscript.config.config.scene_output_stream`;
however, this is automatically done by :class:`~visuscript.scene.Scene`.
"""

from argparse import ArgumentParser
import subprocess
import importlib.util
import sys
import os
from pathlib import Path

from visuscript.config import config
from visuscript import Color

THEME = ["dark", "light"]


def main():
    parser = ArgumentParser(__doc__)

    parser.add_argument(
        "input_script",
        type=Path,
        help="Python script that prints a stream of SVG elements to standard output.",
    )
    parser.add_argument(
        "--output",
        default="output.mp4",
        type=Path,
        help="Filename at which the output video will be stored.",
    )
    parser.add_argument(
        "--width", default=1920, type=int, help="Width in pixels of the output video."
    )
    parser.add_argument(
        "--height", default=1080, type=int, help="Height in pixels of the output video."
    )
    parser.add_argument(
        "--logical_width",
        default=480,
        type=int,
        help="Logical width of the output video.",
    )
    parser.add_argument(
        "--logical_height",
        default=270,
        type=int,
        help="Logical height of the output video.",
    )
    parser.add_argument(
        "--downscale",
        default=1,
        type=int,
        help="Both the output-video's dimensions are scaled down by this factor.",
    )
    parser.add_argument(
        "--fps",
        default=30,
        type=int,
        help="Frames Per Second of the output video file.",
    )
    parser.add_argument(
        "--slideshow",
        action="store_true",
        help="If set, outputs a slideshow metadata file in the same directory as the video file, with the same name but suffixed with .json",
    )

    parser.add_argument("--theme", default="dark", choices=THEME)

    args = parser.parse_args()

    input_filename: Path = args.input_script
    output_filename: Path = args.output

    width: int = int(args.width / args.downscale)
    height: int = int(args.height / args.downscale)
    logical_width: int = args.logical_width
    logical_height: int = args.logical_height

    fps: int = args.fps

    theme: str = args.theme

    slideshow: bool = args.slideshow

    if not os.path.exists(input_filename):
        print(
            f'visuscript error: File "{input_filename}" does not exists.',
            file=sys.stderr,
        )
        exit()

    dir_path = Path(__file__).parent.resolve()

    animate_proc = subprocess.Popen(
        [
            sys.executable,
            f"{dir_path / 'visuscript_animate.py'}",
            f"{fps}",
            f"{output_filename}",
        ],
        stdin=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )

    if theme == "dark":
        config.scene_color = Color("dark_slate", 1.0)
        config.text_fill = Color("off_white", 1)
        config.element_fill = Color("off_white", 0.0)
        config.element_stroke = Color("off_white", 1)
    elif theme == "light":
        config.scene_color = Color("off_white", 1.0)
        config.text_fill = Color("dark_slate", 1)
        config.element_fill = Color("dark_slate", 0.0)
        config.element_stroke = Color("dark_slate", 1)

    config.scene_width = width
    config.scene_height = height
    config.scene_logical_width = logical_width
    config.scene_logical_height = logical_height

    config.fps = fps

    config.scene_output_stream = animate_proc.stdin

    slideshow_file = None
    if slideshow:
        slideshow_file = open(
            output_filename.with_suffix(".slideshow-metadata.json"), "w"
        )
        config.slideshow_metadata_output_stream = slideshow_file

    try:
        spec = importlib.util.spec_from_file_location("script", input_filename)

        could_not_load_message = (
            f"Could not load '{input_filename}' as a Python script."
        )
        if spec is None:
            print(could_not_load_message, file=sys.stderr)
            exit()

        mod = importlib.util.module_from_spec(spec)

        if spec.loader is None:
            print(could_not_load_message, file=sys.stderr)
            exit()
        spec.loader.exec_module(mod)

        if hasattr(mod, "main"):
            mod.main()

        if animate_proc.stdin is None:
            print(
                "There was an internal problem communicating with the animation subprocess."
            )
            exit()

        animate_proc.stdin.flush()
        animate_proc.stdin.close()
        animate_proc.wait()

        if animate_proc.returncode == 0:
            print(f'Successfully created "{output_filename}"')
        else:
            print(
                f'visuscript error: There was at least one problem with attempting to create "{output_filename}"',
                file=sys.stderr,
            )
    finally:
        if slideshow_file:
            slideshow_file.close()


if __name__ == "__main__":
    main()
