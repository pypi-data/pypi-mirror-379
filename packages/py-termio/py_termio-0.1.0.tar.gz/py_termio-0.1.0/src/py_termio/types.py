from typing import NamedTuple


class CellSize(NamedTuple):
    width: int
    """The width of a cell in pixels"""
    height: int
    """The height of a cell in pixels"""


class TermSize(NamedTuple):
    rows: int
    """The height of the terminal in cells."""
    columns: int
    """The width of the terminal in cells."""
    width: int
    """The width of the terminal in pixels."""
    height: int
    """The height of the terminal in pixels."""

    @property
    def cellsize(self) -> CellSize:
        return CellSize(
            width=int(self.width / self.columns), height=int(self.height / self.rows)
        )


__all__ = ["CellSize", "TermSize"]
