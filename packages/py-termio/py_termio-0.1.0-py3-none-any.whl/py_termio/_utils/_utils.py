from contextlib import contextmanager
from sys import __stdin__
from types import SimpleNamespace
from typing import Callable, Iterator, TypeAlias

from py_termio.exceptions import TermError

_ReadTerm: TypeAlias = Callable[[int, int, float | None], str]
_CaptureMode: TypeAlias = Callable[[], Iterator[None]]
_GetTermResponse: TypeAlias = Callable[
    [str, str, float | None], Iterator[SimpleNamespace]
]


class _GetTermResponseFn:
    read_term: _ReadTerm
    capture_mode: _CaptureMode

    def __int__(self, read_term: _ReadTerm, capture_mode: _CaptureMode) -> None:
        self.read_term = read_term
        self.capture_mode = capture_mode

    @contextmanager
    def __call__(
        self, start: str, end: str, timeout: float | None = None
    ) -> Iterator[SimpleNamespace]:
        if __stdin__ is None:
            raise TermError("stdin is closed")

        response = SimpleNamespace(sequence="")

        stdin = __stdin__.buffer.fileno()

        with self.capture_mode():
            yield response

            while not response.sequence.endswith(end):
                response.sequence += self.read_term(fd=stdin, length=1, timeout=timeout)

                if not response.sequence.startswith(start[: len(response.sequence)]):
                    raise TabError("Unexpected response from terminal")


__all__ = ["_GetTermResponse", "_GetTermResponseFn"]
