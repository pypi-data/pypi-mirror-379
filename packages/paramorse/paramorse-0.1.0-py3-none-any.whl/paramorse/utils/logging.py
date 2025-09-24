# ---------------------------------------------------------------------------- #
# paramorse.utils.logging
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import logging
import os
from typing import Optional


_DEFAULT_LOG_LEVEL = logging.DEBUG # 10
# _DEFAULT_LOG_LEVEL = logging.INFO # 20
# _DEFAULT_LOG_LEVEL = logging.WARNING # 30
# _DEFAULT_LOG_LEVEL = logging.ERROR # 40
# _DEFAULT_LOG_LEVEL = logging.CRITICAL # 50

_DEFAULT_LOG_ASCTIME = "%H:%M:%S"

class ParaMorseLogFormatter(logging.Formatter):

    # ANSI color codes
    GREY = "\x1b[38;20m" # "\x1b[38;21m"
    YELLOW = "\x1b[33;20m" # \x1b[33;21m"
    RED = "\x1b[31;20m" # "\x1b[31;21m"
    BOLD_RED = "\x1b[31;1m"
    CYAN = "\x1b[0;36m"
    PURPLE = "\x1b[38;2;182;90;190m"

    RESET = "\x1b[0m" 
    
    FORMAT_START = "| "
    FORMAT_MID = "%(levelname)s"

    # FORMAT_END = " |\n| %(pathname)s\n| %(module)s:%(lineno)d -- %(funcName)s --| %(message)s"
    FORMAT_END = " -- %(filename)s:%(lineno)d -- %(funcName)s --| %(message)s"
    # FORMAT_END = " -- %(asctime)s | %(filename)s:%(lineno)d -- %(funcName)s --| %(message)s"

    _PLAIN = FORMAT_START + FORMAT_MID + FORMAT_END

    FORMATS_COLORED = {
        logging.DEBUG: FORMAT_START + PURPLE + FORMAT_MID + RESET + FORMAT_END,
        logging.INFO: FORMAT_START + CYAN + FORMAT_MID + RESET + FORMAT_END,
        logging.WARNING: FORMAT_START + YELLOW + FORMAT_MID + RESET + FORMAT_END,
        logging.ERROR: FORMAT_START + RED + FORMAT_MID + RESET + FORMAT_END,
        logging.CRITICAL: FORMAT_START + BOLD_RED + FORMAT_MID + RESET + FORMAT_END
    }
    
    def __init__(self, *, datefmt: Optional[str] = _DEFAULT_LOG_ASCTIME, use_color: bool = True) -> None:
        super().__init__(datefmt=datefmt)
        self.datefmt = datefmt
        self.use_color = use_color
    
    def format(self, record: logging.LogRecord) -> str:
        if self.use_color:
            log_fmt = self.FORMATS_COLORED.get(record.levelno, self._PLAIN)
        else:
            log_fmt = self._PLAIN
        return logging.Formatter(log_fmt, datefmt=self.datefmt).format(record)



def configure_logs(
        level: int | None = _DEFAULT_LOG_LEVEL,
        *,
        datefmt: str = "%H:%M:%S",
        use_color: bool | None = None,
        force: bool = False,
        silence_numba: bool = True,
        numba_level: int = logging.WARNING,
    ) -> None:
    """
    Configure root logging with a colored formatter.
    If handlers already exist and force=False, do not replace them.
    Args:
        level:
            root level passed to the formatter
        datefmt:
            time format passed to the formatter
        use_color:
            force color on/off
        force:
            if True, replace existing handlers
        silence_numba & numba_level:
            if True, set numba logger level to `numba_level`.
    """
    root = logging.getLogger()

    if silence_numba:
        logging.getLogger("numba").setLevel(numba_level)

    # decide whether to change handlers
    if root.handlers and not force:
        # adjust level even if we keep existing handlers
        if level is not None:
            root.setLevel(level)
        return
    
    effective_level = logging.INFO if level is None else level

    handler = logging.StreamHandler()
    if use_color is None:
        use_color = _auto_use_color(handler.stream)
    handler.setFormatter(ParaMorseLogFormatter(datefmt=datefmt, use_color=use_color))

    logging.basicConfig(level=effective_level, handlers=[handler], force=force)


def _auto_use_color(stream) -> bool:
    # respect NO_COLOR (https://no-color.org/) and only color TTYs
    if os.environ.get("NO_COLOR"):
        return False
    try:
        return hasattr(stream, "isatty") and stream.isatty()
    except Exception:
        return False
