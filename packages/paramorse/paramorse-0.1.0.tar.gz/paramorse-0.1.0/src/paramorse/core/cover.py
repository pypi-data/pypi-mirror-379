# ---------------------------------------------------------------------------- #
# paramorse.core.cover
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import copy
import logging

from typing import Union
from typing import TypedDict
from typing import TypeAlias

from paramorse.utils.render import pm_pformat # noqa: F401 

from spacy.tokens.token import Token as spacyToken
from spacy.tokens.doc import Doc as spacyDoc

import paramorse.utils.helpers as pm_helpers
import paramorse.core.linguistics as pm_ling


from paramorse.core.config import ParaMorseConfig

logger = logging.getLogger(__name__)



cover_input_type_alias: TypeAlias = Union[
        str,
        list[str],
        list[spacyToken],
        spacyDoc,
    ]

# ---------------------------------------------------------------------------- #

class PM_Cover(TypedDict):
    cover_text: str
    cover_parse_sdoc: spacyDoc | None
    cover_parse_stoks: list[spacyToken]
    cover_parse_list: list[str]
    cover_parse_list_ws: list[str]
    cover_parse_cap: list[int]
    cover_list: list[str]
    cover_tokens: list[str]
    cover_tokens_cap: list[int]
    cover_tokens_stok_subsets: list[list[int]] 


_PM_COVERS: dict[str, PM_Cover] = {
    'empty': PM_Cover(
        cover_text = "",
        cover_parse_sdoc = None,
        cover_parse_stoks = [],
        cover_parse_list = [],
        cover_parse_list_ws = [],
        cover_parse_cap = [],
        cover_list = [],
        cover_tokens = [],
        cover_tokens_cap = [],
        cover_tokens_stok_subsets = [],
    )
}

# ---------------------------------------------------------------------------- #

def tokenize_cover(
        cover_text: str | None=None,
        variant_cfg_input: dict | None=None,
    ) -> PM_Cover:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    Cvr_Dict: PM_Cover = copy.deepcopy(_PM_COVERS['empty'])

    if(not isinstance(cover_text, str) or cover_text==""): return Cvr_Dict
    
    Cvr_Dict['cover_text'] = cover_text

    snlp = pm_ling.load_spacy_model(variant_cfg["spacy_model"])
    
    Cvr_Dict['cover_parse_sdoc'] = snlp(cover_text)
    Cvr_Dict['cover_parse_stoks'] = list(Cvr_Dict['cover_parse_sdoc'])
    Cvr_Dict['cover_parse_list'] = [stok.text for stok in Cvr_Dict['cover_parse_stoks']]
    Cvr_Dict['cover_parse_list_ws'] = [stok.text_with_ws for stok in Cvr_Dict['cover_parse_stoks']]
    
    # start_on_non_encoding_ele = False
    for i_stok, stok in enumerate(Cvr_Dict['cover_parse_stoks']):

        if(pm_ling.stok_has_capacity(stok)):
            Cvr_Dict['cover_parse_cap'].append(1)
            Cvr_Dict['cover_tokens'].append(stok.text_with_ws)
            Cvr_Dict['cover_tokens_stok_subsets'].append([i_stok])
            Cvr_Dict['cover_tokens_cap'].append(1)
        else:
            Cvr_Dict['cover_parse_cap'].append(0)
            if(i_stok==0):
                # start_on_non_encoding_ele = True
                Cvr_Dict['cover_tokens'].append(stok.text_with_ws)
                Cvr_Dict['cover_tokens_stok_subsets'].append([i_stok])
                Cvr_Dict['cover_tokens_cap'].append(0)
            else:
                Cvr_Dict['cover_tokens'][-1] = Cvr_Dict['cover_tokens'][-1] + stok.text_with_ws
                Cvr_Dict['cover_tokens_stok_subsets'][-1].append(i_stok)

    # for now cover_list duplicatates cover_tokens 
    for tok in Cvr_Dict['cover_tokens']: Cvr_Dict['cover_list'].append(tok)

    return Cvr_Dict


def build_cover(
        cover_input: cover_input_type_alias,
        variant_cfg_input: dict | None=None,
    ) -> PM_Cover:

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()

    if(pm_helpers.is_string(cover_input)):
        cover_text = cover_input
    elif(pm_helpers.is_list_of_strings(cover_input)):
        cover_text = " ".join(cover_input)
    elif(pm_helpers.is_list_of_spacyTokens(cover_input)):
        cover_text = str(cover_input[0].doc)
    elif(pm_helpers.is_spacyDoc(cover_input)):
        cover_text = str(cover_input)
    else:
        cover_text = None
        
    Cvr_Dict: PM_Cover = tokenize_cover(
        cover_text=cover_text,
        variant_cfg_input=variant_cfg
    )
    
    # logger.debug(f'Cvr_Dict:\n{pm_pformat(Cvr_Dict)}')

    return Cvr_Dict
