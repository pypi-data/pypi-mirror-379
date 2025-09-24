# ---------------------------------------------------------------------------- #
# paramorse.core.linguistics
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import functools

import logging
import spacy

from spacy.tokens.token import Token as spacyToken
from spacy.language import Language as spacyLanguage


logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------- #
# sets of linguistic objects 

_CONTRACTIONS = {
    "n't",
    "'s",
    "'d",
    "'ll",
    "'re",
    "'ve",
    "'m",
    }


# _PUNCTUATION = {

#     ".",
#     "?",
#     "!",

#     ",",
#     ":",
#     ";",

#     "}",
#     "{",
#     "]",
#     "[",
#     ")",
#     "(",
#     ">",
#     "<",
    
# }

_PUNCTS_NO_PAD_LEFT_SPACE = {

    # ".",
    # "?",
    # "!",

    # ",",
    # ":",
    # ";",

    # "}",
    "{",
    # "]",
    "[",
    # ")",
    "(",
    # ">",
    "<",

}

# _PUNCTS_NEXT_TO_SPACE = {
#     ws
#     for p in _PUNCTUATION
#     # for ws in (f"{p} ")
#     for ws in (f" {p}", f"{p} ", f" {p} ")
# }

# _SPACINGS_NON_STANDARD = {
#     "\t",
#     "\n",
#     "\r",
#     # " ",
# }

# _SPACINGS = _SPACINGS_NON_STANDARD.union({" "})


# ---------------------------------------------------------------------------- #
# spaCy

@functools.lru_cache(maxsize=1)
def load_spacy_model(model_name: str) -> spacyLanguage:
    try:
        return spacy.load(model_name)
    except OSError:
        spacy.cli.download(model_name) # type: ignore
        return spacy.load(model_name)


# ---------------------------------------------------------------------------- #
# paramorse package creation


# cover-playoad token overlap 
def para_toks_in_cover(
        cover_parse_list: list,
        payload_para_flat: list
    ) -> set:
    cover_toks_set = set(cover_parse_list)
    para_toks_set = set(payload_para_flat)
    toks_intersection = para_toks_set.intersection(cover_toks_set)
    return toks_intersection


# cover token has capacity to carry morse para
def stok_has_capacity(stok: spacyToken) -> bool:

    stok_text = stok.text

    stok_has_capacity = not (

        False

        or stok.is_punct
        or stok.is_bracket
        # or stok_text in _PUNCTUATION
        # or stok_text in _PUNCTS_NEXT_TO_SPACE

        or stok.is_space
        # or stok_text in _SPACINGS_NON_STANDARD
        # or stok_text in _SPACINGS

        or stok_text in _CONTRACTIONS
        or stok_text.startswith("'")
    
    )

    return stok_has_capacity


# ---------------------------------------------------------------------------- #


def last_char_is_space(pkg_substring: str) -> bool:
    last_char = pkg_substring[-1]
    if(last_char.isspace()): is_space = True
    else: is_space = False
    return is_space


def last_char_is_no_space_punct(pkg_substring: str) -> bool:
    last_char = pkg_substring[-1]
    if(last_char in _PUNCTS_NO_PAD_LEFT_SPACE): is_no_space_punct = True
    else: is_no_space_punct = False
    return is_no_space_punct
