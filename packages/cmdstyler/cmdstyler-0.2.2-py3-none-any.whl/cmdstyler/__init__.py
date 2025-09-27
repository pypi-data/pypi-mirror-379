from .core import (
    beautify,
    header,
    empty,
    color,
    backgroundcolor as background,
    allcolor as bothcolors,
    realrgbcolor as rgbcolor,  # shorter, user-friendly name
    center,
    divider
)

from . import cursor
from . import text
__all__ = ["beautify", "header", "empty", "color", "background", "bothcolors", "rgbcolor", "cursor", "center", "divider", "bold", "text"]
