from typing import Callable

from py_termio._consts import WINDOWS


class _GetChar:
    def __init__(self) -> None: ...
    def __call__(self) -> bytes: ...

    pass


class _GetKeyPress(_GetChar):
    pass


if WINDOWS:
    import msvcrt

    _SP_KEY = [b"\xe0", b"\x00"]

    class _GetChar:
        def __init__(self) -> None:
            pass

        def __call__(self) -> bytes:
            return msvcrt.getch()

    class _GetKeyPress(_GetChar):
        def __call__(self) -> bytes:
            ch = msvcrt.getch()
            if ch in _SP_KEY:
                ch += msvcrt.getch()
            return ch
else:
    from os import read
    from select import select
    from sys import stdin
    from termios import ECHO, ICANON, TCSADRAIN, TCSANOW, tcgetattr, tcsetattr

    ESC = b"\x1b"
    CSI = ESC + b"["

    class _GetChar:
        def __init__(self) -> None:
            pass

        def __call__(self) -> bytes:
            fd = stdin.fileno()
            old_settings = tcgetattr(fd)
            new_settings = old_settings[:]
            new_settings[3] &= ~(ICANON | ECHO)
            try:
                tcsetattr(fd, TCSANOW, new_settings)
                ch = read(fd, 1)
            finally:
                tcsetattr(fd, TCSADRAIN, old_settings)
            return ch

    class _GetKeyPress(_GetChar):
        def __call__(self) -> bytes:
            fd = stdin.fileno()
            old_settings = tcgetattr(fd)
            new_settings = old_settings[:]
            new_settings[3] &= ~(ICANON | ECHO)
            try:
                tcsetattr(fd, TCSANOW, new_settings)
                ch = read(fd, 1)
                if ch == ESC:
                    ready, _, _ = select([fd], [], [], 0.1)
                    if ready == [fd]:
                        ch += read(fd, 1)
                        if ch == CSI:
                            ready, _, _ = select([fd], [], [], 0.1)
                            if ready == [fd]:
                                ch += read(fd, 1)
            finally:
                tcsetattr(fd, TCSADRAIN, old_settings)
            return ch


get_char: Callable[[], bytes] = _GetChar()


get_keypress: Callable[[], bytes] = _GetKeyPress()

__all__ = ["get_char", "get_keypress"]
