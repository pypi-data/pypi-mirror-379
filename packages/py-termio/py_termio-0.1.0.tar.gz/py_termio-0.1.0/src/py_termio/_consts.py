from sys import platform

WINDOWS = platform == "win32"

ESC = b"\x1b"
CSI = ESC + b"["

__all__ = ["WINDOWS", "ESC", "CSI"]
