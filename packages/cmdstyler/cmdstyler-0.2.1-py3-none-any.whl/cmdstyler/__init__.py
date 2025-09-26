from .core import (
    beautify,
    header,
    empty,
    color,
    backgroundcolor as background,
    allcolor as bothcolors,
    realrgbcolor as rgbcolor,  # shorter, user-friendly name
    center,
    divider,
    bold
)

from . import cursor
__all__ = ["beautify", "header", "empty", "color", "background", "bothcolors", "rgbcolor", "cursor", "center", "divider", "bold"]
