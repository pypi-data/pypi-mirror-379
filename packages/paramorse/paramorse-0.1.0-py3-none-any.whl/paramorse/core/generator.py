# ---------------------------------------------------------------------------- #
# paramorse.core.generator
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import functools
import random
import textwrap
import logging
from typing import Any

import functools
from importlib.resources import files
from pathlib import Path


from paramorse.utils.helpers import read_text_file

import paramorse.core.transform as pm_transform
import paramorse.core.payload as pm_payload
import paramorse.core.cover as pm_cover
from paramorse.core.config import ParaMorseConfig

logger = logging.getLogger(__name__)


_DEFAULT_WORDS_FILE = "words_1k.txt"

""" GENERATE COVERS """


def _read_packaged_text(package: str, relative_path: str) -> str:
    return (files(package) / relative_path).read_text(encoding="utf-8")

@functools.lru_cache(maxsize=5)
def load_wordlist(words_file: str = _DEFAULT_WORDS_FILE) -> list[str]:
   
    p = Path(words_file)
    if p.is_file():
        # user-supplied override by path
        words_input = p.read_text(encoding="utf-8")
    else:
        # packaged fallback
        words_input = _read_packaged_text("paramorse", f"data/{words_file}")

    return words_input.splitlines()


def rand_list_words(
        n_words: int = 10,
        trailing_space: bool = False
    ) -> list:

    wordlist = load_wordlist()
    list_words = random.sample(wordlist, n_words)

    if(trailing_space):
        for i in range(len(list_words)):
            list_words[i] = list_words[i] + " "

    return list_words


def rand_two_word_list(
        n_word_pairs: int = 5,
        mode: str = "alternating",
        preamble: int = 0,
        trailing_space: bool = False
    ) -> list:
    
    if(n_word_pairs<0): n_word_pairs=0
    if(preamble<0): preamble=0

    word_1 = None
    word_2 = None
    max_word_len = 8

    wordlist = load_wordlist()

    while (word_1 is None
            or len(word_1) > max_word_len):
            word_1 = random.sample(wordlist, 1)[0]
    while (word_2 is None
            or word_2 == word_1
            or len(word_2) > max_word_len):
            word_2 = random.sample(wordlist, 1)[0]

    word_bank = [word_1, word_2]

    list_words = []

    if(preamble>0):
        for i in range(0, preamble, 1):
            if(i%2==0):
                list_words.append(word_1)
            else:
                list_words.append(word_2)

    if(mode=="alternating"):    
        for _ in range(0, n_word_pairs, 1):
            list_words.append(word_1)
            list_words.append(word_2)
    elif(mode=="random"):
        for _ in range(0, n_word_pairs, 1):
            list_words.append(random.choice(word_bank))
            list_words.append(random.choice(word_bank))

    if(trailing_space):
         for i in range(len(list_words)):
              list_words[i] = list_words[i] + " "

    return list_words


def intro_exercise_cover() -> dict:
    
    text_string = '''
    This message is in ParaMorse, a super language variant of oral English.
    ParaMorse maps the dots and dashes of Morse code onto paralinguistic filler sounds.
    What symbol has been embedded in this message?
    '''

    text_string = textwrap.dedent(text_string)
    text_string = text_string[1:-1]

    cover_dict = pm_cover.build_cover(text_string)
    
    exercise_dict = {
        'text_string': text_string,
        'cover_dict': cover_dict,
    }

    return exercise_dict




""" GENERATE PAYLOADS """


def rand_payload_sym(
        n_symbols: int=2,
        spaced: bool=False,
        variant_cfg_input: dict[str, Any] | None = None,
    ) -> str:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()
    
    # default alphabet indices:
    # 0-26 letters
    # 26-37 numbers
    # 37-54 punctuation & special chars
    N_THRU_LETTERS = 26
    # N_THRU_NUMBERS = 36
    payload_alphabet_n = N_THRU_LETTERS

    rand_source = list(variant_cfg['symbol_to_dd'])[0:payload_alphabet_n]
    rand_symbols = []
    for _ in range(0, n_symbols):
        rand_char = random.choice(rand_source)
        rand_symbols.append(rand_char)
        if(spaced):
            rand_symbols.append(" ")

    rand_sym_string = "".join(rand_symbols)

    return rand_sym_string


def get_payload_list_dicts(
        idx_lower: int = 0,
        idx_upper: int = 26,
        payload_type: str = 'sym',
        variant_cfg_input: dict[str, Any] | None = None,
    ) -> dict:
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    # default alphabet indices:
    # 0-26 letters
    # 26-37 numbers
    # 37-54 punctuation & special chars
    # N_THRU_LETTERS = 26
    # N_THRU_NUMBERS = 36

    if(payload_type == 'sym'):
        list_source = list(variant_cfg['symbol_to_dd'])
        symbol_list = list_source[idx_lower:idx_upper]
        payload_list = symbol_list
    else:
        # payload_list = ['hello', 'world']
        payload_list = ['hello world']

    payload_dict_list = {}
    for pay in payload_list:
        payload_dict_list[f'pay_{pay}'] = pm_payload.build_payload(payload_input=pay)
    
    return payload_dict_list




""" GENERATE PACKAGES """


def rand_encode_separ(
        cover_input: str | None = None,
        payload_input: pm_payload.payload_input_type_alias | None = None, # detects payload type and format
        variant_cfg_input: dict[str, Any] | None = None,
        enc_out_dict: dict[str,Any] | None = None,
    ) -> pm_transform.PM_SeparEnc:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    if(cover_input is None):
        word_len = 30
        list_words = rand_two_word_list(n_word_pairs=word_len)
        cover_input = " ".join(list_words)

    if(payload_input is None):
        letter_len = 2
        payload_input = rand_payload_sym(
            n_symbols=letter_len,
            spaced=True,
            variant_cfg_input=variant_cfg,
            )

    encode_dict = pm_transform.encode_separ(
        cover_input=cover_input,
        payload_input=payload_input,
        variant_cfg_input=variant_cfg,
        enc_out_dict=enc_out_dict,
    )

    return encode_dict
