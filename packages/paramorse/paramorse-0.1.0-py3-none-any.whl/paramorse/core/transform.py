# ---------------------------------------------------------------------------- #
# paramorse.core.transform
# ---------------------------------------------------------------------------- #

from __future__ import annotations

from typing import Any
from typing import TypedDict

import json
import logging 
import copy
from paramorse.utils.render import pm_pformat # noqa: F401 

from paramorse.utils.paths import data_path_resolver
from paramorse.utils.paths import get_data_dirs

import paramorse.utils.helpers as pm_helpers

from paramorse.core.config import ParaMorseConfig

# import paramorse.core as pm_core
import paramorse.core.linguistics as pm_ling
import paramorse.core.payload as pm_payload
import paramorse.core.cover as pm_cover
import paramorse.core.package as pm_package

logger = logging.getLogger(__name__)

_DATADIRS: dict[str, dict] = get_data_dirs()


# ---------------------------------------------------------------------------- #

class PM_SeparEnc(TypedDict):
    package_list: list[str]
    package_str: str
    package_dict: pm_package.PM_Package
    cover_dict: pm_cover.PM_Cover
    payload_dict: pm_payload.PM_Payload
    variant_cfg: ParaMorseConfig


class PM_SeparDec(TypedDict):
    pay_para: list # para_flat
    pay_morse: str
    pay_text: str
    variant_cfg: ParaMorseConfig


_PM_SEPAR_ENCS: dict[str, PM_SeparEnc] = {
    'empty': PM_SeparEnc(
        package_list = [],
        package_str = "",
        package_dict = copy.deepcopy(pm_package._PM_PACKAGES['empty']),
        cover_dict = copy.deepcopy(pm_cover._PM_COVERS['empty']),
        payload_dict = copy.deepcopy(pm_payload._PM_PAYLOADS['empty']),
        variant_cfg = ParaMorseConfig(),
    )
}


_PM_SEPAR_DECS: dict[str, PM_SeparDec] = {
    'empty': PM_SeparDec(
        pay_para = [],  # para_flat list
        pay_morse = "", # dd string
        pay_text = "", # sym string
        variant_cfg = ParaMorseConfig(),
    )
}



# ---------------------------------------------------------------------------- #

def encode(
        cover: str,
        payload: str,
        config: dict | None=None,
        output_path: str | None=None,
    ) -> str:

    enc_out_dict = None
    if(output_path is not None):
        if(isinstance(output_path, str)):
            enc_out_dict = {'data_file_path': output_path}
        else:
            logger.error('encode output_path must be a string type (str)')

    SeparEnc_Dict = encode_separ(
        cover_input = cover,
        payload_input = payload,
        variant_cfg_input = config,
        enc_out_dict = enc_out_dict,
    )
    package = SeparEnc_Dict['package_str']

    return package


def encode_separ(
        cover_input: str | None = None,
        payload_input: pm_payload.payload_input_type_alias | None = None, # detects payload type and format
        variant_cfg_input: dict[str, Any] | None = None,
        enc_out_dict: dict[str,Any] | None = None,
    ) -> PM_SeparEnc:

    SeparEnc_Dict: PM_SeparEnc = copy.deepcopy(_PM_SEPAR_ENCS['empty'])
    
    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()
    SeparEnc_Dict['variant_cfg'] = variant_cfg


    # COVER

    if( (cover_input is None or payload_input is None)
       or (cover_input == "") ):
        return SeparEnc_Dict

    cover_dict = pm_cover.build_cover(
        cover_input=cover_input,
        variant_cfg_input=variant_cfg
        )
    
    cover_tokens = cover_dict['cover_tokens']
    cover_parse_list = cover_dict['cover_parse_list']


    # PAYLOAD

    payload_dict = pm_payload.build_payload(
        payload_input=payload_input,
        variant_cfg_input=variant_cfg
        )


    # PACKAGE

    # para_toks_in_cover_set = pm_core.linguistics.para_toks_in_cover(
    para_toks_in_cover_set = pm_ling.para_toks_in_cover(
        cover_parse_list=cover_parse_list,
        payload_para_flat=payload_dict['para_flat']
        )
    if (len(para_toks_in_cover_set)>0):
        raise ValueError(f"cover_parse_list contains para tokens: {para_toks_in_cover_set}")

    package_dict = pm_package.build_package(
        cover_tokens=cover_tokens
        ,cover_tokens_cap=cover_dict['cover_tokens_cap']
        ,payload_para_flat=payload_dict['para_flat_rs']
        ,variant_cfg_input=variant_cfg
    )

    package_list = package_dict['package_list']
    package_str = package_dict['package_str']

    SeparEnc_Dict = {
        'package_list': package_list, # TODO duplicated data
        'package_str': package_str,
        'package_dict': package_dict, 
        'cover_dict': cover_dict,
        'payload_dict': payload_dict,
        'variant_cfg': variant_cfg
    }

    if(enc_out_dict is not None):
        encode_save_to_file(
            enc_dict=SeparEnc_Dict,
            enc_out_dict=enc_out_dict,
            variant_cfg_input=variant_cfg_input,
            variant_cfg=variant_cfg,
            )
        
    return SeparEnc_Dict


def encode_save_to_file(
        enc_dict: PM_SeparEnc,
        enc_out_dict: dict = {},
        variant_cfg_input: dict | None=None,
        variant_cfg: dict | None=None,
    ) -> bool:

    encode_saved = False

    save_dict: dict[str, Any]
    if pm_helpers.is_nonempty_dict(enc_out_dict):
        save_dict = enc_out_dict
    else:
        save_dict = {

            # "data_file_path": None,

            # "data_dir_name": None,
            "data_dir_name": _DATADIRS['paths_string']['encoded_pkg'],

            # "data_item_name": "example_item",
            # "data_item_name": "decoded_package",

            # "data_item_subname": None,
            # "data_item_subname": "example_subitem",

            # 'data_item_id': "example_id",

            # "data_file_suffix": ".txt"
        }
    path_dict = data_path_resolver(
        **save_dict
        )
    # logger.debug(f'path_dict:\n{pm_pformat(path_dict)}')

    if (pm_helpers.is_nonempty_dict(enc_dict)
        and pm_helpers.is_nonempty_dict(path_dict)):

        enc_out_filepath = path_dict['file_path_obj']
        enc_out_dir = path_dict['dir_path_obj']

        if(path_dict['resolve_source'] == 'data_file_path'):
            save_filepath = enc_out_filepath
        else:
            save_filename = "enc_pkg_text.txt"
            save_filepath = enc_out_dir / save_filename

        logger.debug(f"saving output to:\n{save_filepath}")
        enc_data_str = enc_dict['package_str']
        with open(save_filepath, 'w', encoding='utf-8') as f:
            f.write(enc_data_str)

        if(path_dict['resolve_source'] == 'data_file_path'):
            enc_out_dir_stem = path_dict['file_path_obj_stem']
            save_filepath = enc_out_dir / (enc_out_dir_stem + "_meta.json")
        else:
            save_filename = "enc_pkg_meta.json"
            save_filepath = enc_out_dir / save_filename

        enc_meta_dict = {
            'variant_cfg_input' : variant_cfg_input,
            'variant_cfg' : variant_cfg
        }
        logger.debug(f"saving output to:\n{save_filepath}")
        with open(save_filepath, "w") as f:
            json.dump(enc_meta_dict, f, indent=4)

        encode_saved = True    

    return encode_saved


# ---------------------------------------------------------------------------- #

def decode(
        package: str,
        config: dict | None=None,
        output_path: str | None=None,
    ) -> str:

    dec_out_dict = None
    if(output_path is not None):
        if(isinstance(output_path, str)):
            dec_out_dict = {'data_file_path': output_path}
        else:
            logger.error('decode output_path must be a string type (str)')

    SeparDec_Dict = decode_separ(
        package = package,
        variant_cfg_input = config,
        dec_out_dict = dec_out_dict,
    )
    payload = SeparDec_Dict['pay_text']

    return payload


def decode_separ(
        package: str,
        variant_cfg_input: dict[str, Any] | None = None,
        dec_out_dict: dict | None = None,
    ) -> PM_SeparDec:

    SeparDec_Dict: PM_SeparDec = copy.deepcopy(_PM_SEPAR_DECS['empty'])

    variant_cfg = ParaMorseConfig(**variant_cfg_input) if variant_cfg_input else ParaMorseConfig()
        
    SeparDec_Dict['variant_cfg'] = variant_cfg

    # right now spacy tokens "stoken" are approximation of variant tokens
    parsed_dict = pm_package.parse_package_input(
        package_input=package,
        variant_cfg_input=variant_cfg
    )
    # logger.debug(f'parsed_dict:\n{parsed_dict}')

    para_flat = parsed_dict['para_flat']
    pay_config = parsed_dict['pay_config']

    payload_dict = pm_payload.build_payload(
        para_flat
        ,pay_config
        ,variant_cfg_input=variant_cfg
        )

    decoded_morse = payload_dict['dd']
    decoded_text = payload_dict['sym']

    SeparDec_Dict = {
        "pay_para": para_flat,
        "pay_morse": decoded_morse,
        "pay_text": decoded_text,
        'variant_cfg': variant_cfg,
        }
       
    if(dec_out_dict is not None):
        decode_save_to_file(
            dec_dict=SeparDec_Dict, 
            dec_out_dict=dec_out_dict, 
            variant_cfg_input=variant_cfg_input,
            variant_cfg=variant_cfg,
            )

    return SeparDec_Dict


def decode_save_to_file(
        dec_dict: PM_SeparDec,
        dec_out_dict: dict = {},
        variant_cfg_input: dict | None=None,
        variant_cfg: dict | None=None,
    ) -> bool:

    decode_saved = False

    save_dict: dict[str, Any]
    if pm_helpers.is_nonempty_dict(dec_out_dict):
        save_dict = dec_out_dict
    else:
        save_dict = {
            # "data_file_path": None,

            # "data_dir_name": None,
            "data_dir_name": _DATADIRS['paths_string']['decoded_pkg'],

            # "data_item_name": "example_item",
            # "data_item_name": "decoded_package",

            # "data_item_subname": None,
            # "data_item_subname": "example_subitem",

            # 'data_item_id': "example_id",

            # "data_file_suffix": ".txt"

        }
    path_dict = data_path_resolver(
        **save_dict
        )
    # logger.debug(f'path_dict:\n{pm_pformat(path_dict)}')

    if (pm_helpers.is_nonempty_dict(dec_dict)
        and pm_helpers.is_nonempty_dict(path_dict)):

        dec_out_filepath = path_dict['file_path_obj']
        dec_out_dir = path_dict['dir_path_obj'] 

        if(path_dict['resolve_source'] == 'data_file_path'):
            save_filepath = dec_out_filepath
        else:
            save_filename = "dec_pkg.json"
            save_filepath = dec_out_dir / save_filename
        
        dec_data_dict = {
            'pay_para' : dec_dict['pay_para'],
            'pay_text' : dec_dict['pay_text'],
            'pay_morse' : dec_dict['pay_morse'],
        }
        logger.debug(f"saving output to:\n{save_filepath}")
        with open(save_filepath, "w") as f:
            json.dump(dec_data_dict, f, indent=4)

        if(path_dict['resolve_source'] == 'data_file_path'):
            enc_out_dir_stem = path_dict['file_path_obj_stem']
            save_filepath = dec_out_dir / (enc_out_dir_stem + "_meta.json")
        else:
            save_filename = "dec_pkg_meta.json"
            save_filepath = dec_out_dir / save_filename
            
        dec_meta_dict = {
            'variant_cfg_input' : variant_cfg_input,
            'variant_cfg' : variant_cfg,
        }
        logger.debug(f"saving output to:\n{save_filepath}")
        with open(save_filepath, "w") as f:
            json.dump(dec_meta_dict, f, indent=4)

        decode_saved = True

    return decode_saved


