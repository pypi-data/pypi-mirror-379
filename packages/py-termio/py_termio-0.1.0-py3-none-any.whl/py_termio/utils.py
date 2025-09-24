# ruff: noqa: F811
from types import SimpleNamespace
from typing import Iterator

from py_termio._consts import WINDOWS


def get_char() -> bytes:
    """Gets a single character from standard input. Does not echo to the screen."""
    ...


def get_keypress() -> bytes:
    """Gets a keypress from standard input. Does not echo to the screen."""
    ...


from py_termio._read import get_char, get_keypress


def get_term_response(
    start: str, end: str, timeout: float | None = None
) -> Iterator[SimpleNamespace]: ...


if WINDOWS:
    from py_termio._utils._win_utils import (
        capture_mode,
        get_term_response,
        get_termsize,
        read_term,
    )
else:
    from py_termio._utils._unix_utils import (
        capture_mode,
        get_term_response,
        get_termsize,
        read_term,
    )

__all__ = [
    "get_char",
    "get_keypress",
    "get_termsize",
    "read_term",
    "capture_mode",
    "get_term_response",
]
