# ---------------------------------------------------------------------------- #
# paramorse.utils.helpers
# ---------------------------------------------------------------------------- #

from __future__ import annotations

import os
import logging

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any 
from typing import TypeGuard

from spacy.tokens.token import Token as spacyToken
from spacy.tokens.doc import Doc as spacyDoc

from paramorse.utils.paths import get_data_dirs

logger = logging.getLogger(__name__)


_DATADIRS: dict[str, dict]=get_data_dirs()


# FILE IO

def read_text_file(text_input_file: str) -> str:
    
    logger.debug(f"text_input_file:\n{text_input_file}")

    if os.path.isfile(text_input_file):
        text_input_filepath = text_input_file
    elif os.path.isfile(f"{_DATADIRS['paths_string']['raw']}/{text_input_file}"):
        text_input_filepath = f"{_DATADIRS['paths_string']['raw']}/{text_input_file}"
    elif os.path.isdir(text_input_file):
        logger.error("text_input_file provided is directory")
        return ""
    else:
        logger.error(f"text_input_file not found:\n{text_input_file}")
        return ""
    
    with open(text_input_filepath, 'r', encoding = 'utf8') as file:
        text = file.read()

    return text

def _split_file_ext(file: str) -> tuple[str, str]:
    file_name, file_ext = os.path.splitext(file)
    return file_name, file_ext




# GENERATE IDENTIFIERS

def get_timestamp_string(timestamp_format: str | None=None) -> str:
   
    time_now = datetime.now()

    if(timestamp_format is not None):
        timestamp_string = time_now.strftime(f"{timestamp_format}")
    else:
        # timestamp_string = time_now.strftime("%Y%m%d_%H_%M_%S")
        # timestamp_string = time_now.strftime("%Y%m%d_%H_%M_%S.%f")
        frac_seconds = time_now.strftime("%f")[0:3]
        timestamp_string = time_now.strftime(f"%Y%m%d_%H_%M_%S_{frac_seconds}")

    return timestamp_string


def _get_uuid(uuid_format: str = "string") -> str | UUID:
   
    uuid_object = uuid4()
    uuid_string = str(uuid_object)

    if(uuid_format=="string"):
        uuid_result = uuid_string
    else:
        uuid_result = uuid_object

    return uuid_result




# TYPE CHECKING

# STR

def is_string(input: Any) -> TypeGuard[str]:
    return isinstance(input, str)

def is_empty_string(input: Any) -> TypeGuard[str]:
    return isinstance(input, str) and input == ""


# SPACY

def is_spacyToken(input: Any) -> TypeGuard[spacyToken]:
    return isinstance(input, spacyToken)

def is_spacyDoc(input: Any) -> TypeGuard[spacyDoc]:
    return isinstance(input, spacyDoc)


# DICT

def is_dict(input: Any) -> TypeGuard[dict]:
    return isinstance(input, dict)

def is_empty_dict(input: Any) -> TypeGuard[dict]:
    return isinstance(input, dict) and len(input) == 0

def is_nonempty_dict(input: Any) -> TypeGuard[dict]:
    return isinstance(input, dict) and len(input) > 0


# LIST

def is_list(input: Any) -> TypeGuard[list]:
    return isinstance(input, list)

def is_empty_list(input: Any) -> TypeGuard[list[Any]]:
    return isinstance(input, list) and len(input) == 0

def is_nonempty_list(input: Any) -> TypeGuard[list[Any]]:
    return isinstance(input, list) and len(input) > 0

def is_list_of_strings(input: Any) -> TypeGuard[list[str]]:
    return isinstance(input, list) and all(isinstance(sub, str) for sub in input)


def is_nonempty_list_of_strings(input: Any) -> TypeGuard[list[str]]:
    return (
        isinstance(input, list)
        and len(input) > 0
        and all(isinstance(sub, str) for sub in input)
        )

def is_list_of_lists(input: Any) -> TypeGuard[list[list]]:
    return isinstance(input, list) and all(isinstance(sub, list) for sub in input)

def is_list_of_list_of_strings(input: Any) -> TypeGuard[list[list[str]]]:
    return (
        isinstance(input, list)
        and all(isinstance(sub, list) for sub in input)
        and all(all(isinstance(sub_ele, str) for sub_ele in sub) for sub in input)
    )

def is_list_of_nonempty_list_of_strings(input: Any) -> TypeGuard[list[list[str]]]:
    return (
        # outer list reqs:
        isinstance(input, list)
        and len(input) > 0                                 
        and all(
            # sublist reqs:
            isinstance(sub, list)
            and len(sub) > 0
            # sublist string reqs:
            and all(isinstance(sub_ele, str) for sub_ele in sub)
            for sub in input
        )
    )

def is_list_of_spacyTokens(input: Any) -> TypeGuard[list[spacyToken]]:
    return isinstance(input, list) and all(isinstance(sub, spacyToken) for sub in input)

def is_non_empty_list_of_spacyTokens(input: Any) -> TypeGuard[list[spacyToken]]:
    return (
        isinstance(input, list)
        and len(input) > 0
        and all(isinstance(sub, spacyToken) for sub in input)
    )

