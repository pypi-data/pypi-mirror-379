from array import array
from contextlib import contextmanager
from fcntl import ioctl
from os import read
from select import select
from sys import __stdin__, __stdout__
from termios import TCSANOW, TIOCGWINSZ, tcgetattr, tcsetattr
from tty import setcbreak
from typing import Iterator

from py_termio._utils._utils import _GetTermResponse, _GetTermResponseFn
from py_termio.exceptions import TermError
from py_termio.types import TermSize


def get_termsize() -> TermSize:
    if __stdout__ is None:
        raise TermError("stdout is closed")

    buf = array("H", [0, 0, 0, 0])
    ioctl(__stdout__, TIOCGWINSZ, buf)
    return TermSize(*buf)


def read_term(fd: int, length: int, timeout: float | None = None) -> str:
    readable, _, _ = select([fd], [], [], timeout)
    if not readable:
        raise TimeoutError("Timeout waiting for data")
    return read(fd, length).decode()


@contextmanager
def capture_mode() -> Iterator[None]:
    if __stdin__ is None:
        raise TermError("stdin is closed")

    stdin = __stdin__.buffer.fileno()
    original_mode = tcgetattr(stdin)
    setcbreak(stdin, TCSANOW)

    try:
        yield
    finally:
        tcsetattr(stdin, TCSANOW, original_mode)


get_term_response: _GetTermResponse = _GetTermResponseFn(
    read_term=read_term, capture_mode=capture_mode
)

__all__ = ["get_termsize", "read_term", "capture_mode", "get_term_response"]
