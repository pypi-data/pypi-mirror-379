"""Visuscript is a vector-graphics-based Animation library for Python.

The core class that drives Visuscript's functionality is :class:`~visuscript.Scene`.
Refer to the documentation for :class:`~visuscript.Scene` to see how to create Python scripts from which Visuscript can generate a movie.

To create an video with Visuscript, use the command-line utility, :mod:`~visuscript.cli.visuscript_cli`.
If Visuscript was installed using pip,
this utility should have been added to the environment's PATH with the name :code:`visuscript`.
Thus, after having created a Python script, use the following to generate a movie and output it as `output.mp4`:

.. code-block:: bash

    visuscript path/to/script.py

If the utility is not added to your PATH, the following works as well:

.. code-block:: bash

    python3 -m visuscript path/to/script.py

"""

from .drawable import Circle, Rect, Image, Pivot, Drawing, connector
from .primatives import Transform, Vec2, Rgb
from .drawable.scene import Scene
from .organizer import GridOrganizer
from .drawable.text import Text
from .segment import Path
from .constants import (
    Anchor,
    OutputFormat,
    UP,
    RIGHT,
    DOWN,
    LEFT,
)
from .updater import UpdaterBundle, TranslationUpdater, FunctionUpdater, run_updater
from .animation import (
    animate_translation,
    animate_scale,
    animate_rotation,
    animate_transform,
    animate_rgb,
    animate_opacity,
    animate_path,
    sequence,
    bundle,
    run,
    wait,
)

from .mixins import Color

from . import animation, config, drawable, mixins, organizer
from .animation import easing

__all__ = [
    "Scene",
    "Circle",
    "Rect",
    "Image",
    "Pivot",
    "Drawing",
    "Text",
    "Transform",
    "Vec2",
    "Rgb",
    "Color",
    "Path",
    "GridOrganizer",
    "UpdaterBundle",
    "TranslationUpdater",
    "FunctionUpdater",
    "run_updater",
    "Anchor",
    "OutputFormat",
    "UP",
    "RIGHT",
    "DOWN",
    "LEFT",
    "animate_translation",
    "animate_scale",
    "animate_rotation",
    "animate_transform",
    "animate_rgb",
    "animate_opacity",
    "animate_path",
    "sequence",
    "bundle",
    "run",
    "wait",
    "animation",
    "drawable",
    "config",
    "connector",
    "easing",
    "mixins",
    "organizer",
]
