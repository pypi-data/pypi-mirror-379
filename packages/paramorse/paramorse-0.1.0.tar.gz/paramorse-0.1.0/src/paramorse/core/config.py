# ---------------------------------------------------------------------------- #
# paramorse.core.config
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import copy

from typing import Any, Union
from collections.abc import Mapping, MutableMapping

import logging

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------- #


_SEPAR_DOT_TOKEN = "um"
_SEPAR_DASH_TOKEN = "uh"
_SEPAR_PARA_LETSEP = "okay"
# SEPAR_PARA_WORDSEP = ""
_SEPAR_PARA_WORDSEP = "alright"
# SEPAR_WORDSEP_OVERWRITE = False
_SEPAR_WORDSEP_OVERWRITE = True

_SEPAR_DD_PARA_MAP: dict[str, str] = {
    ".": _SEPAR_DOT_TOKEN,
    "-": _SEPAR_DASH_TOKEN,
    " ": _SEPAR_PARA_LETSEP,
    "/": _SEPAR_PARA_WORDSEP,
}

_MORSE_ALPHABET_SYMBOL_DD: dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
}

# build morse alphabet maps
_MORSE_ALPHABET_SYMBOL_PARA: dict[str, list[str]] = {}
for sym, dd in _MORSE_ALPHABET_SYMBOL_DD.items():
    para = []
    for ele in list(dd):
        para.append(_SEPAR_DD_PARA_MAP[ele])
    _MORSE_ALPHABET_SYMBOL_PARA[sym] = para


_MORSE_ALPHABET_DOTDASH_SYM: dict[str, str] = {
    dd: sym for sym, dd in _MORSE_ALPHABET_SYMBOL_DD.items()
}


SEPAR_CONFIG: dict[str, Union[str, bool, int, list, dict]] = {

    # USERy
    # paralanguage settings
    # para token values
    "dot_token": _SEPAR_DOT_TOKEN,
    "dash_token": _SEPAR_DASH_TOKEN,
    "letter_separator": _SEPAR_PARA_LETSEP,  # paralanguage marking end of payload letter (empty = disabled)
    "word_separator": _SEPAR_PARA_WORDSEP,  # paralanguage marking end of payload word (empty = disabled)
    # para token operations
    "word_sep_overwrite": _SEPAR_WORDSEP_OVERWRITE,  # overwrite letter separator with word separator (combines spacing, if applicable)
    "allow_adjacent": False,

    # SYSTEMy
    # para token map
    "dd_para_map": _SEPAR_DD_PARA_MAP,
    # morse payload
    # morse payload alphabet
    "symbol_to_dd": _MORSE_ALPHABET_SYMBOL_DD,
    # morse payload alphabet maps
    "dd_to_symbol": _MORSE_ALPHABET_DOTDASH_SYM,
    "symbol_to_para": _MORSE_ALPHABET_SYMBOL_PARA,
    # spaCy settings
    "spacy_model": "en_core_web_sm",
    "language": "en-US",

}


# ---------------------------------------------------------------------------- #


class ParaMorseConfig(dict):
    """
    A dictionary-like configuration whose `.update()` keeps:
      `symbol_to_para`
      `dd_para_map`
    in sync.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(copy.deepcopy(SEPAR_CONFIG))
        if args or kwargs:
            # force a rebuild so the initial overrides are coherent
            self.update(*args, _force_rebuild=True, **kwargs)

    def update(self, *args: Any, _force_rebuild: bool = False, **kwargs: Any) -> None:
        """
        Works like `dict.update`, but refreshes the derived maps
        when any of the dependent keys change.
        """

        # normalize positional & keyword inputs into a single mapping
        update_params_dict: dict[str, Any] = {}

        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 positional argument")

            if len(args) == 1:
                arg = args[0]
                if isinstance(arg, Mapping):
                    update_params_dict.update(arg)
                else:
                    # assume iterable of (k, v) pairs
                    for k, v in arg:
                        update_params_dict[k] = v

        update_params_dict.update(kwargs)
        needs_rebuild = _force_rebuild or any(
            k in _FORCE_RBLD_KEYS and self.get(k) != v
            for k, v in update_params_dict.items()
        )
        super().update(update_params_dict)

        if needs_rebuild:
            _rebuild_para_maps(self)
            # logger.debug("rebuilt symbol_to_para & dd_para_map due to config change.")

    # convenience: clear() + replace everything in one call
    def replace(self, **new_cfg: Any) -> None:
        """
        Convenience clear() with replace all settings in one call
        while preserving dict identity.
        """
        self.clear()
        super().update(copy.deepcopy(SEPAR_CONFIG))
        self.update(new_cfg, _force_rebuild=True)


# ---------------------------------------------------------------------------- #

_FORCE_RBLD_KEYS: set = {
    "dot_token",
    "dash_token",
    "letter_separator",
    "word_separator",
}

_DEPENDANT_KEYS: set = {
    "dd_para_map",
    "symbol_to_para"
}


def _rebuild_para_maps(variant_cfg: MutableMapping[str, Any]) -> None:
    """
    Mutates `variant_cfg` in-place, refreshing:
      `symbol_to_para`
      `dd_para_map`
    """

    dot_para = variant_cfg["dot_token"]
    dash_para = variant_cfg["dash_token"]
    letter_sep_para = variant_cfg["letter_separator"]
    word_sep_para = variant_cfg["word_separator"]
    symbol_to_dd: dict[str, str] = variant_cfg["symbol_to_dd"]

    # _DEPENDANT_KEYS updates

    # dd_para_map
    variant_cfg["dd_para_map"] = {
        ".": dot_para,
        "-": dash_para,
        " ": letter_sep_para,
        "/": word_sep_para,
    }

    # symbol_to_para
    new_symbol_para = {}
    # for sym, dd in variant_cfg['symbol_to_dd'].items():
    for sym, dd in symbol_to_dd.items():
        para = dd
        for key, val in variant_cfg["dd_para_map"].items():
            para = [c.replace(key, val) for c in para]
        new_symbol_para[sym] = para
    variant_cfg["symbol_to_para"] = new_symbol_para
