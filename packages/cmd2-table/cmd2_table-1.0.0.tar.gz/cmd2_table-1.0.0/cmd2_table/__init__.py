"""Import certain things for backwards compatibility."""

from .ansi import (
    Bg,
    EightBitBg,
    EightBitFg,
    Fg,
    RgbBg,
    RgbFg,
    TextStyle,
    style,
)
from .table_creator import (
    AlternatingTable,
    BorderedTable,
    Column,
    HorizontalAlignment,
    SimpleTable,
    TableCreator,
    VerticalAlignment,
)

__all__: list[str] = [  # noqa: RUF022
    # ANSI Exports
    'Bg',
    'Fg',
    'EightBitBg',
    'EightBitFg',
    'RgbBg',
    'RgbFg',
    'TextStyle',
    'style',
    # Table Exports
    'AlternatingTable',
    'BorderedTable',
    'Column',
    'HorizontalAlignment',
    'SimpleTable',
    'TableCreator',
    'VerticalAlignment',
]
