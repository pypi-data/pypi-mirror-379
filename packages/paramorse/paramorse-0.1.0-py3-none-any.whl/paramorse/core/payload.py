# ---------------------------------------------------------------------------- #
# paramorse.core.payload
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import copy
import logging

from typing import Union
from typing import TypedDict
from typing import Literal
from typing import TypeAlias
from typing import cast
from typing import get_args

from paramorse.utils.render import pm_pformat # noqa: F401 

import paramorse.utils.helpers as pm_helpers
from paramorse.core.config import ParaMorseConfig

logger = logging.getLogger(__name__)

payload_input_type_alias: TypeAlias = Union[
    str,
    list[str],
    list[list[str]],
]

# ---------------------------------------------------------------------------- #

PayFormat_Literal = Literal["string", "string_list", "nest_list"]

PayKind_Literal = Literal["dd", "sym", "para"]

class PM_Payload(TypedDict):
    sym: str
    sym_list: list[str]

    dd: str
    dd_list: list[str]
    dd_flat: list[str]
    dd_nest: list[list[str]]

    para: str
    para_list: list[str]
    para_flat: list[str]
    para_flat_rs: list[str] # right space
    para_nest: list[list[str]]

    pay_format: PayFormat_Literal | None
    pay_kind: PayKind_Literal | None


# make literals into tuples for validity checks 
PAY_FORMATS = cast(tuple[PayFormat_Literal, ...], get_args(PayFormat_Literal))
PAY_KINDS = cast(tuple[PayKind_Literal, ...], get_args(PayKind_Literal))

_PM_PAYLOADS: dict[str, PM_Payload] = {
    "empty": PM_Payload(
        sym="",
        sym_list=[],
        dd="",
        dd_list=[],
        dd_flat=[],
        dd_nest=[],
        para="",
        para_list=[],
        para_flat=[],
        para_flat_rs=[],
        para_nest=[],
        pay_format=None,
        pay_kind=None,
    )
}


# ---------------------------------------------------------------------------- #
# MORSE MAPS

# between kinds:
# dd: dotdash
# sym: symbol
# para: paralanguage

# across formats:
# string: str
# list: list of str
# nest: list of list of str


def morse_sym_to_dd(
        symbols: str,
        variant_cfg_input: dict | None = None,
    ) -> str:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()
    morse_alphabet = variant_cfg["symbol_to_dd"]

    symbols = symbols.upper()
    dds: list[str] = []
    for sym in symbols:
        if sym == " ":
            dds.append("/")
        elif sym in morse_alphabet:
            dds.append(morse_alphabet[sym])
        else:
            logger.warning("No Morse for %r", sym)

    morse_dd = " ".join(dds)

    return morse_dd


def morse_dd_to_sym(
        morse_dd: str,
        variant_cfg_input: dict | None = None,
    ) -> str:
    
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()
    rev_morse_alphabet = variant_cfg["dd_to_symbol"]

    dd_split = morse_dd.split()
    symbols: list[str] = []
    for dd in dd_split:
        if dd == "/":
            symbols.append(" ")
        elif dd in rev_morse_alphabet:
            symbols.append(rev_morse_alphabet[dd])
        else:
            logger.warning("Unknown Morse %r", dd)

    morse_sym = "".join(symbols)

    return morse_sym


def morse_dd_to_para_nest(
        morse_dd: str,
        variant_cfg_input: dict | None = None,
    ) -> list:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    # assumes dotdashes of letters are space separated
    dd_split = morse_dd.split()
    para_nest = []
    for i_dd, dd in enumerate(dd_split):
        # find seg in alphabet
        if dd in variant_cfg["dd_to_symbol"]:
            morse_sym = variant_cfg["dd_to_symbol"][dd]
            morse_para = variant_cfg["symbol_to_para"][morse_sym]
            para_nest.append(morse_para)

        # skip paralanguage separators on last morse symbol
        if (i_dd + 1) == len(dd_split):
            continue

        # new word separator, if any
        if dd == "/":
            if variant_cfg["word_sep_overwrite"]:
                para_nest.pop()  # drop last end of symbol letter_separator
            para_nest.append([variant_cfg["word_separator"]])

        # new letter separator, if any
        else:
            para_nest.append([variant_cfg["letter_separator"]])

    return para_nest


def morse_para_expand(
        morse_para: str,
        variant_cfg_input: dict | None = None,
    ) -> dict[str, list]:
    
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    # assumes morse_para tokens are space separated
    para_split = morse_para.split()
    para_top_list = []
    para_cur_sublist = []
    for para in para_split:
        if para == variant_cfg["dot_token"]:
            para_cur_sublist.append(para)
        elif para == variant_cfg["dash_token"]:
            para_cur_sublist.append(para)
        elif (
            para == variant_cfg["letter_separator"]
            or para == variant_cfg["word_separator"]
        ):
            if para_cur_sublist:
                para_top_list.append(para_cur_sublist)
            para_top_list.append([para])
            para_cur_sublist = []
        else:
            logger.warning("No Morse for %r", para)

    # flush last segment
    if para_cur_sublist:
        para_top_list.append(para_cur_sublist)

    para_expansion = {
        "para_list": para_split,
        "para_nest": para_top_list,
    }

    return para_expansion


def morse_para_to_dd(
        morse_para: str,
        variant_cfg_input: dict | None = None,
    ) -> str:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    # assumes morse_para tokens are space separated
    para_split = morse_para.split()
    dds: list[str] = []
    for para in para_split:
        if para == variant_cfg["dot_token"]:
            dds.append(".")
        elif para == variant_cfg["dash_token"]:
            dds.append("-")
        elif para == variant_cfg["letter_separator"]:
            dds.append(" ")
        elif para == variant_cfg["word_separator"]:
            if variant_cfg["word_sep_overwrite"]:
                dds.append(" ")
                dds.append("/")
            else:
                dds.append("/")
            dds.append(" ")
        else:
            logger.warning("No Morse for %r", para)

    morse_dd = "".join(dds)

    return morse_dd


# ---------------------------------------------------------------------------- #
# DETECT PAYLOAD
# payload kind 
# payload format

def _detect_payload_format(
        payload_input: payload_input_type_alias,
    ) -> PayFormat_Literal | None:

    pay_format = None

    if pm_helpers.is_string(payload_input):
        pay_format = "string"

    elif pm_helpers.is_list_of_strings(payload_input):
        pay_format = "string_list"

    elif pm_helpers.is_list_of_list_of_strings(payload_input):
        pay_format = "nest_list"

    return pay_format


def _detect_payload_kind(
        payload_input: payload_input_type_alias,
        pay_format: str | None = None,
        variant_cfg_input: dict | None = None,
    ) -> PayKind_Literal | None:
    
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    dd_para_map: dict = variant_cfg["dd_para_map"]
    tok_map_dd_set = set(dd_para_map.keys())
    tok_map_para_set = set(dd_para_map.values())

    pay_kind = None

    if payload_input is None or (
        not isinstance(payload_input, str) and not isinstance(payload_input, list)
    ):
        return pay_kind

    # return on empty input
    payload_input_len = len(payload_input)
    if not payload_input_len > 0:
        return pay_kind

    if pay_format not in PAY_FORMATS:
        pay_format = _detect_payload_format(payload_input)

    if pay_format == "string":
        if not pm_helpers.is_string(payload_input):
            raise TypeError(f"""Expected str payload for pay_format '{pay_format}'""")
        
        payload_set = set(payload_input)
        payload_split_set = set(payload_input.split())

        if payload_set.issubset(tok_map_dd_set):
            pay_kind = "dd"
        elif payload_split_set.issubset(tok_map_para_set):
            pay_kind = "para"
        else:
            pay_kind = "sym"

    elif pay_format == "nest_list":
        if not pm_helpers.is_list_of_list_of_strings(payload_input):
            raise TypeError(f"""Expected list[list[str]] payload for pay_format '{pay_format}'""")
        
        payload_input_set = set()
        for pld_list in payload_input:
            payload_input_set = payload_input_set.union(set(pld_list))

        if payload_input_set.issubset(tok_map_dd_set):
            pay_kind = "dd"
        elif payload_input_set.issubset(tok_map_para_set):
            pay_kind = "para"
        else:
            pay_kind = "sym"

    elif pay_format == "string_list":
        if not pm_helpers.is_list_of_strings(payload_input):
            raise TypeError(f"""Expected list[str] payload for pay_format '{pay_format}'""")
        
        payload_input_set = set()
        payload_input_split_set = set()
        for pld_str in payload_input:
            payload_input_set = payload_input_set.union(set(pld_str))
            payload_input_split_set = payload_input_split_set.union(
                set(pld_str.split())
            )
        if payload_input_set.issubset(tok_map_dd_set):
            pay_kind = "dd"
        elif payload_input_split_set.issubset(tok_map_para_set):
            pay_kind = "para"
        else:
            pay_kind = "sym"

    # logger.debug(f'pay_kind: {pay_kind}')

    return pay_kind


def detect_payload(
        payload_input: payload_input_type_alias,
        variant_cfg_input: dict | None = None,
    ) -> dict:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    pay_format = _detect_payload_format(payload_input)
    pay_kind = _detect_payload_kind(
        payload_input=payload_input,
        pay_format=pay_format,
        variant_cfg_input=variant_cfg,
    )

    # logger.debug(f"pay_format: {pay_format}")
    # logger.debug(f"pay_kind: {pay_kind}")

    detect_result = {
        "pay_format": pay_format,
        "pay_kind": pay_kind,
    }

    return detect_result


# ---------------------------------------------------------------------------- #
# CREATE PAYLOAD


def _start_payload(
        Pay_Dict: PM_Payload,
        payload_input: payload_input_type_alias,
        pay_format: str,
        pay_kind: str,
        variant_cfg_input: dict | None = None,
    ) -> PM_Payload:
    
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    if pay_format == "string":
        if not pm_helpers.is_string(payload_input): return Pay_Dict

        payload_input = payload_input.strip()

        if pay_kind == "dd":
            Pay_Dict["dd"] = payload_input
            Pay_Dict["dd_list"] = Pay_Dict["dd"].split(" ")
            Pay_Dict["dd_nest"] = [list(mark) for mark in Pay_Dict["dd_list"]]
        elif pay_kind == "sym":
            Pay_Dict["sym"] = payload_input
            Pay_Dict["sym_list"] = list(Pay_Dict["sym"].split())
        elif pay_kind == "para":
            Pay_Dict["para"] = payload_input
            para_expansion = morse_para_expand(Pay_Dict["para"], variant_cfg)
            Pay_Dict["para_list"] = para_expansion["para_list"]
            Pay_Dict["para_nest"] = para_expansion["para_nest"]

    elif pay_format == "string_list":
        if not pm_helpers.is_list_of_strings(payload_input): return Pay_Dict

        if pay_kind == "dd":
            Pay_Dict["dd_list"] = payload_input
            Pay_Dict["dd"] = " ".join(Pay_Dict["dd_list"])
            Pay_Dict["dd_nest"] = [list(mark) for mark in Pay_Dict["dd_list"]]
        elif pay_kind == "sym":
            Pay_Dict["sym_list"] = payload_input
            Pay_Dict["sym"] = " ".join(Pay_Dict["sym_list"])
        elif pay_kind == "para":
            Pay_Dict["para_list"] = payload_input
            Pay_Dict["para_nest"] = [mark.split() for mark in payload_input]
            Pay_Dict["para"] = " ".join(Pay_Dict["para_list"])

    elif pay_format == "nest_list":
        if not pm_helpers.is_list_of_list_of_strings(payload_input): return Pay_Dict

        if pay_kind == "dd":
            Pay_Dict["dd_nest"] = payload_input
            Pay_Dict["dd_list"] = ["".join(mark) for mark in Pay_Dict["dd_nest"]]
            Pay_Dict["dd"] = " ".join(Pay_Dict["dd_list"])
        elif pay_kind == "para":
            Pay_Dict["para_nest"] = payload_input
            Pay_Dict["para_list"] = [" ".join(mark) for mark in Pay_Dict["para_nest"]]
            Pay_Dict["para"] = " ".join(Pay_Dict["para_list"])

    return Pay_Dict


def _fill_out_payload(
        Pay_Dict: PM_Payload, pay_kind: str, variant_cfg_input
    ) -> PM_Payload:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    if pay_kind == "dd":
        Pay_Dict["sym"] = morse_dd_to_sym(Pay_Dict["dd"], variant_cfg)
        Pay_Dict["sym_list"] = list(Pay_Dict["sym"].split())
        Pay_Dict["para_nest"] = morse_dd_to_para_nest(Pay_Dict["dd"], variant_cfg)
        Pay_Dict["para_list"] = [para for mark in Pay_Dict["para_nest"] for para in mark]
        Pay_Dict["para"] = " ".join(Pay_Dict["para_list"])

    elif pay_kind == "sym":
        Pay_Dict["dd"] = morse_sym_to_dd(Pay_Dict["sym"], variant_cfg)
        Pay_Dict["dd_list"] = Pay_Dict["dd"].split(" ")
        Pay_Dict["dd_nest"] = [list(mark) for mark in Pay_Dict["dd_list"]]
        Pay_Dict["para_nest"] = morse_dd_to_para_nest(Pay_Dict["dd"], variant_cfg)
        Pay_Dict["para_list"] = [" ".join(mark) for mark in Pay_Dict["para_nest"]]
        Pay_Dict["para"] = " ".join(Pay_Dict["para_list"])

    elif pay_kind == "para":
        Pay_Dict["dd"] = morse_para_to_dd(Pay_Dict["para"], variant_cfg)
        Pay_Dict["dd_list"] = Pay_Dict["dd"].split(" ")
        Pay_Dict["dd_nest"] = [list(mark) for mark in Pay_Dict["dd_list"]]
        Pay_Dict["sym"] = morse_dd_to_sym(Pay_Dict["dd"], variant_cfg)
        Pay_Dict["sym_list"] = list(Pay_Dict["sym"].split())

    # flat dd lists
    Pay_Dict["dd_flat"] = []
    for mark in Pay_Dict["dd"].split():
        Pay_Dict["dd_flat"].extend(mark)
        Pay_Dict["dd_flat"].append(" ")

    # flat para lists
    Pay_Dict["para_flat"] = Pay_Dict["para"].split()
    Pay_Dict["para_flat_rs"] = [para + " " for para in Pay_Dict["para_flat"]]

    return Pay_Dict


def build_payload(
        payload_input: payload_input_type_alias,
        pay_config: dict | None = None,
        variant_cfg_input: dict | None = None,
    ) -> PM_Payload:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    Pay_Dict: PM_Payload = copy.deepcopy(_PM_PAYLOADS["empty"])

    if not (
        pm_helpers.is_string(payload_input)
        or pm_helpers.is_list_of_strings(payload_input)
        or pm_helpers.is_list_of_list_of_strings(payload_input)
    ):
        return Pay_Dict

    # SET pay_format & pay_kind

    if pay_config is not None:
        pay_format = pay_config.get("pay_format", None)
        pay_kind = pay_config.get("pay_kind", None)

    pay_format = _detect_payload_format(payload_input)

    pay_kind = _detect_payload_kind(
        payload_input=payload_input,
        pay_format=pay_format,
        variant_cfg_input=variant_cfg,
    )

    Pay_Dict["pay_format"] = pay_format
    Pay_Dict["pay_kind"] = pay_kind

    if pay_format not in PAY_FORMATS or pay_kind not in PAY_KINDS:
        return Pay_Dict

    # BUILD Pay_Dict

    _start_payload(
        Pay_Dict=Pay_Dict,
        payload_input=payload_input,
        pay_format=pay_format,
        pay_kind=pay_kind,
        variant_cfg_input=variant_cfg,
    )

    _fill_out_payload(
        Pay_Dict=Pay_Dict,
        pay_kind=pay_kind,
        variant_cfg_input=variant_cfg,
    )

    # logger.debug(f"Pay_Dict:\n{pm_pformat(Pay_Dict)}")

    return Pay_Dict
