# ---------------------------------------------------------------------------- #
# paramorse.__init__
# ---------------------------------------------------------------------------- #

"""
Paramorse: ParaLinguistic Morse code, a human super language.

WIP public API:
- encode(...) -> str
- decode(...) -> str
- configure_logs(...) -> None

"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

# RE-EXPORT PUBLIC API

from paramorse.core.transform import encode, decode
from paramorse.utils.logging import configure_logs

try:
    __version__ = _pkg_version("paramorse")
except PackageNotFoundError:
    __version__ = "0.unknown"

__all__ = [
    "encode",
    "decode",
    "configure_logs",
    "__version__",
]
