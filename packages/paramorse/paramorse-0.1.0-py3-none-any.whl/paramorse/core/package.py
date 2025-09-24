# ---------------------------------------------------------------------------- #
# paramorse.core.package_list
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import random
import copy

from typing import Any 
from typing import TypedDict

from typing import Optional

import logging

from paramorse.utils.render import pm_pformat # noqa: F401 

import paramorse.core.linguistics as pm_ling
from paramorse.core.config import ParaMorseConfig

logger = logging.getLogger(__name__)


PAD_LEFT_PARA_SPACING_ALL_TOKS = True
PUNCT_AWARE_PAD_LEFT_PARA_SPACING_ALL_TOKS = True
TRIM_RIGHT_PARA_SPACING_LAST_TOK = False

# ---------------------------------------------------------------------------- #

class PM_Package(TypedDict):
    package_list: list[str]
    package_str: str


_PM_PACKAGES: dict[str, PM_Package] = {
    'empty': PM_Package(
        package_list = [],
        package_str = "",
    )
}


# ---------------------------------------------------------------------------- #

def parse_package_input(
        package_input: str,
        variant_cfg_input: dict[str, Any] | None=None,
    ) -> dict:
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    dd_para_map: dict = variant_cfg['dd_para_map']

    snlp = pm_ling.load_spacy_model(variant_cfg["spacy_model"])
    package_parse_sdoc = snlp(package_input)
    package_parse_stoks = list(package_parse_sdoc)

    package_parse_list_lower_strip = [
        stok.text.lower().strip() for stok in package_parse_stoks
        ]

    cover_list = []
    para_flat = []

    for pkg_str in package_parse_list_lower_strip:
        if(pkg_str in dd_para_map.values()):
            para_flat.append(pkg_str)
        else:
            cover_list.append(pkg_str)

    pay_config = {
        'pay_format':'string_list',
        'pay_kind':'para'
    }
    
    parse_pkg_dict = {
        'package_input': package_input,
        'pay_config': pay_config,
        'para_flat': para_flat,
        'cover_list': cover_list,
    }

    return parse_pkg_dict


# ---------------------------------------------------------------------------- #


def build_package(
        cover_tokens: list[str],
        cover_tokens_cap: list,
        payload_para_flat: list[str],
        preamble_len: int = 0,
        variant_cfg_input: dict | None=None,
    ) -> PM_Package:

    # variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    Pkg_Dict: PM_Package = copy.deepcopy(_PM_PACKAGES['empty'])

    # allow_adjacent = variant_cfg['allow_adjacent'] # for now ignore

    cover_len = len(cover_tokens)
    if(preamble_len > cover_len):
        logger.warning("truncating preamble_len")
        preamble_len = cover_len
    if(preamble_len > 0):
        for i in range(preamble_len):
            cover_tokens_cap[i]=0

    if(len(payload_para_flat) > 0):
        package_list = splice_payload_into_cover(
            cover_tokens=cover_tokens,
            cover_tokens_cap=cover_tokens_cap,
            payload_para_flat=payload_para_flat
        )
    else:
        package_list = cover_tokens

    package_str = "".join(package_list)

    Pkg_Dict = {
        'package_list': package_list,
        'package_str': package_str
    }

    # logger.debug(f'Pkg_Dict:\n{pm_pformat(Pkg_Dict)}')

    return Pkg_Dict


def splice_payload_into_cover(
        cover_tokens: list[str],
        cover_tokens_cap: list[int],
        payload_para_flat: list[str],
        seed: Optional[int] = None,
    ) -> list[str]:

    if len(cover_tokens) != len(cover_tokens_cap):
        raise ValueError("cover_tokens and cover_tokens_cap must be the same length.")
    if any(c not in (0, 1) for c in cover_tokens_cap):
        raise ValueError("cover_tokens_cap must contain only 0 or 1.")

    cap1_indices = [i for i, c in enumerate(cover_tokens_cap) if c == 1]
    cap1_tokens = [cover_tokens[i] for i in cap1_indices] 

    cover_len = len(cover_tokens)
    payload_len = len(payload_para_flat)

    # number of slots available around the tokens with cap==1
    k = len(cap1_tokens) + 1 
    m = payload_len
    # playload paras can be 1 greater than the number of tokens with capacity

    # enforce non-adjacency capacity
    if m > k:
        logger.warning("truncating payload")
        payload_para_flat = payload_para_flat[:k]
        m = k

    rng = random.Random(seed) if seed is not None else random

    # randomly choose slots
    k_slots_range = range(k)
    k_slots = sorted(rng.sample(k_slots_range, m)) if m > 0 else []
    # k_slots = sorted(rng.choices(k_slots_range, k=m)) if m > 0 else [] # for allow adj

    k_slots_para = {}
    for k_slot, para in zip(k_slots, payload_para_flat):
        k_slots_para[k_slot] = para

    package_list: list[str] = []

    if not cap1_indices:
        # if no cap==1 tokens, then only one k_slot (k == 1).
        # place para (if any) for k_slot 0 at beginning
        # rest is the entirety of the cover
        para_at_pos0 = k_slots_para.get(0)
        if para_at_pos0 is not None:
            package_list.append(para_at_pos0)
        package_list.extend(cover_tokens)
        return package_list

    # therefore at least one cap==1 token
    first_cap1_idx = cap1_indices[0] 
    # walk the original cover tokens in order
    # keeping track of the cap==1 tokens passed 
    # at each cover token, look for the "after" k_slot index 
    # see if it exists and insert para token
    curr_cap1_pos = 0 # position within cap1_tokens (0..len-1)
    head = None
    head_is_para = False
    for i in range(cover_len):

        # ZERO-TH PARA TOKEN
        # if/when at the first cap==1,  check if there is k_slot for pos0
        # insert the "before first" k_slot
        if i == first_cap1_idx:
            if(i>0): first_token_is_cap0 = True
            else: first_token_is_cap0 = False
            para_at_pos0 = k_slots_para.get(0)
            if para_at_pos0 is not None:
                if(first_token_is_cap0): # add any post processing
                    para_at_pos0 = edit_spacing_at_para_tok_start(
                        preceding_token=cover_tokens[i-1],
                        para_tok=para_at_pos0
                        )
                head = para_at_pos0
                head_is_para = True
                package_list.append(head)

        # COVER TOKENS
        # add cover token itself
        head = cover_tokens[i]
        head_is_para = False
        package_list.append(head)

        # ALL OTHER PARA TOKENS
        # if cover token has capacity and next k_slot follows immediately
        # insert the "after" k_slot para token 
        if cover_tokens_cap[i] == 1:
            # k_slot indices: after 0th cap1 is k_slot 1, etc.
            slot_after = curr_cap1_pos + 1
            para_after = k_slots_para.get(slot_after)
            if para_after is not None:
                para_after = edit_spacing_at_para_tok_start(
                    preceding_token=cover_tokens[i],
                    para_tok=para_after
                    )
                head = para_after
                head_is_para = True
                package_list.append(head)
            curr_cap1_pos += 1

    if(head_is_para and TRIM_RIGHT_PARA_SPACING_LAST_TOK):
        package_list[-1] = edit_spacing_at_para_tok_end(para_tok=package_list[-1])

    # logger.debug(f'package_list: {pm_pformat(package_list)}')

    return package_list


def edit_spacing_at_para_tok_start(preceding_token: str, para_tok: str):

    # assumes para is of default form, eg. "uh " or "um "
    proc_para = para_tok
    if(PAD_LEFT_PARA_SPACING_ALL_TOKS):
        if(PUNCT_AWARE_PAD_LEFT_PARA_SPACING_ALL_TOKS):
            if(not pm_ling.last_char_is_space(pkg_substring=preceding_token)
               and not pm_ling.last_char_is_no_space_punct(pkg_substring=preceding_token)):
                proc_para = " " + para_tok
        else:
            if(not pm_ling.last_char_is_space(pkg_substring=preceding_token)):
                proc_para = " " + para_tok
                
    return proc_para


def edit_spacing_at_para_tok_end(para_tok: str):

    proc_para = para_tok
    if(TRIM_RIGHT_PARA_SPACING_LAST_TOK):
        proc_para = proc_para[:-1]

    return proc_para