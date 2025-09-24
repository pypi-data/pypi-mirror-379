# typeL ignore[assignment]

from py_termio._consts import CSI, ESC, WINDOWS

if WINDOWS:
    from typing import Tuple

    class _KeyPress(Tuple[bytes, bytes]):
        def __eq__(self, other) -> bool:
            if isinstance(other, _KeyPress):
                return any([kp in self for kp in other])
            elif isinstance(other, bytes):
                return other in self
            raise TypeError

    def _make_sp_keypress(end: bytes) -> _KeyPress:
        return _KeyPress((b"\xe0" + end, b"\x00" + end))

    LEFT_ARROW = _make_sp_keypress(b"K")
    RIGHT_ARROW = _make_sp_keypress(b"M")
    UP_ARROW = _make_sp_keypress(b"H")
    DOWN_ARROW = _make_sp_keypress(b"P")

else:
    LEFT_ARROW = CSI + b"D"
    RIGHT_ARROW = CSI + b"C"
    UP_ARROW = CSI + b"A"
    DOWN_ARROW = CSI + b"B"

__all__ = [
    "WINDOWS",
    "ESC",
    "CSI",
    "LEFT_ARROW",
    "RIGHT_ARROW",
    "UP_ARROW",
    "DOWN_ARROW",
]
