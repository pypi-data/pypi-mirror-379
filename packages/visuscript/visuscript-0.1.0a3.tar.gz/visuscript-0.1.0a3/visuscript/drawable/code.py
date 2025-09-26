# type: ignore
from visuscript.mixins import HierarchicalDrawable, AnchorMixin
from visuscript.primatives import Vec2
from pygments import highlight
from pygments.lexers import PythonLexer as _PythonLexer
from pygments.formatters import SvgFormatter as _SvgFormatter
from pygments.styles import get_style_by_name as _get_style_by_name
import re


def get_all_code_blocks(filename: str) -> dict[int, str]:
    """Gets all marked codeblocks in a given file.

    A codeblock is any segment of a text file that begins with "##N",
    where "N" is a non-negative integer like "0", "49", or "103",
    and that ends with "##"

    :param filename: The file in which code blocks are found.
    :return: A dictionary mapping the id of each codeblock to the text thereof.

    .. Hint:: You can get code blocks from the current Python file by using __file__.
    """
    with open(filename, "r") as f:
        code = f.read()
    pattern = r"##(\d+)(.*?)##"
    matches = re.findall(pattern, code, re.DOTALL)

    segments_dict: dict[int, str] = {}
    for x_str, segment_content in matches:
        x = int(x_str)
        full_segment = f"{segment_content}"
        segments_dict[x] = full_segment.strip("\n")
    return segments_dict


class PythonText(HierarchicalDrawable, AnchorMixin):
    """Syntax highlighted Python code."""

    def __init__(self, text: str, *, font_size: float, style="monokai"):
        super().__init__()
        self._text = text
        self._font_size = font_size
        self._style = style

        self._max_len = 0
        self._n_lines = 0
        lines = self._text.split("\n")
        end = len(lines)
        if len(lines[-1]) == 0:
            end -= 1
        for line in lines[:end]:
            self._max_len = max(self._max_len, len(line))
            self._n_lines += 1

    @property
    def _spacing(self):
        return self._font_size * 1.357

    # TODO This width is slightly off: figure out what the problem is and fix it
    def calculate_width(self):
        return self._font_size * self._max_len / 2

    # TODO This height may be slightly off: figure out what the problem is and fix it
    def calculate_height(self):
        return self._spacing * (self._n_lines - 1) + self._font_size * 2

    def calculate_top_left(self):
        return Vec2(0, 0)

    def draw_self(self):
        x_offset, y_offset = self.anchor_offset
        code = highlight(
            self._text,
            _PythonLexer(),
            _SvgFormatter(
                style=_get_style_by_name(self._style),
                font_size=self._font_size,
                nowrap=True,
                xoffset=x_offset,
                yoffset=y_offset,
                hackspace=True,
            ),
        ).replace("\n", "")

        def line_counter():
            count = [-1]

            def line_number():
                count[0] += 1
                return count[0]

            return line_number

        line_number = line_counter()
        fix_y_coordinate = (
            lambda _: f'x="{x_offset}" y="{line_number() * (self._spacing) + self._font_size + y_offset}"'
        )
        code = re.sub(r'x="([-\d\.]+)" y="([-\d\.]+)"', fix_y_coordinate, code)

        element = f'<g font-family="monospace" font-size="{self._font_size}" transform="{self.global_transform.svg_transform}">{code}</g>'
        return element
