from contextlib import contextmanager
from ctypes import WinDLL, byref
from ctypes.wintypes import DWORD
from msvcrt import get_osfhandle
from os import get_terminal_size, read
from sys import __stdin__, __stdout__, stdin
from typing import Iterator

from py_termio._consts import CSI as _CSI
from py_termio._utils._utils import _GetTermResponse, _GetTermResponseFn
from py_termio.exceptions import TermError
from py_termio.types import TermSize

WAIT_TIMEOUT = 0x00000102
ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200

CSI = _CSI.decode()
TERM_SIZE_PIXELS = CSI + "14t"

KERNEL32 = WinDLL("kernel32")


def _wait_for_object(fd: int, timeout: float) -> None:
    handle = get_osfhandle(fd)
    return_code: int = KERNEL32.WaitForSingleObject(handle, DWORD(int(timeout * 1000)))
    if return_code == WAIT_TIMEOUT:
        raise TimeoutError("Timeout waiting for data")


def _get_console_mode(fd: int) -> int:
    handle = get_osfhandle(fd)
    mode = DWORD()
    KERNEL32.GetConsoleMode(handle, byref(mode))
    return mode.value


def _set_console_mode(fd: int, mode: int) -> None:
    handle = get_osfhandle(fd)
    KERNEL32.SetConsoleMode(handle, mode)


def _flush(fd: int) -> None:
    handle = get_osfhandle(fd)
    KERNEL32.FlushConsoleInputBuffer(handle)


def read_term(fd: int, length: int, timeout: float | None = None) -> str:
    if timeout is not None:
        _wait_for_object(fd=fd, timeout=timeout)
    return read(fd, length).decode()


@contextmanager
def capture_mode() -> Iterator[None]:
    if __stdin__ is None:
        raise TermError("stdin is closed")

    fd = stdin.buffer.fileno()

    original_mode = _get_console_mode(fd=fd)
    _set_console_mode(fd=fd, mode=ENABLE_VIRTUAL_TERMINAL_INPUT)

    try:
        _flush(fd=fd)
        yield
    finally:
        _set_console_mode(fd=fd, mode=original_mode)


get_term_response: _GetTermResponse = _GetTermResponseFn(
    read_term=read_term, capture_mode=capture_mode
)


def get_termsize() -> TermSize:
    if __stdin__.isatty():
        try:
            with get_term_response(start=CSI, end="t", timeout=0.1) as response:
                __stdout__.write(TERM_SIZE_PIXELS)
                __stdout__.flush()

            sequence = response.sequence[len(CSI) : -len("t")]
            _, height, width = [int(v) for v in sequence.split(";")]
        except (TermError, TimeoutError) as e:
            e.add_note("Failed to read terminal response")
            raise e
    columns, rows = get_terminal_size()
    return TermSize(rows=rows, columns=columns, width=width, height=height)


__all__ = ["get_termsize", "read_term", "capture_mode", "get_term_response"]
