# ---------------------------------------------------------------------------- #
# paramorse.utils.paths
# ---------------------------------------------------------------------------- #

from __future__ import annotations

from pprint import PrettyPrinter
from pathlib import Path
from typing import Any
import os
import logging

_pp = PrettyPrinter(
    indent=2,
    width=80,
    compact=True,
    # compact=False,
    # sort_dicts=True,
    sort_dicts=False,
)

logger = logging.getLogger(__name__)

_ENV_PM_DATADIR = "PARAMORSE_DATA_DIR"

_ROOT_DATADIR_NAME = "pm_data"

_PM_DATADIR_PATH = Path(
    os.getenv(
        _ENV_PM_DATADIR,
        Path.cwd() / _ROOT_DATADIR_NAME
        )
    ).expanduser().resolve()

if(not _PM_DATADIR_PATH.is_dir):
    _PM_DATADIR_PATH = Path.cwd() / _ROOT_DATADIR_NAME

_DATADIR_NAMES = {
    # <data>: _ROOT_DATADIR_NAME/<dirname>
    "root": "",
    "raw": "raw",
    "cover": "cover",
    "payload": "payload",
    "encoded_pkg": "package_enc",
    "decoded_pkg": "package_dec",
    "tts": "tts",
    "transcribe": "transcribe",
    "test": "test",
    "misc": "misc",
}

_DATADIR_PATH_OBJS = dict()
for data, dirname in _DATADIR_NAMES.items():
    _DATADIR_PATH_OBJS[data] = (Path(_PM_DATADIR_PATH) / dirname).expanduser().resolve()

_DATADIR_PATH_STRINGS = dict()
for data, path_obj in _DATADIR_PATH_OBJS.items():
    _DATADIR_PATH_STRINGS[data] = str(path_obj)

def get_data_dirs() -> dict:
    data_dirs_dict = dict()
    data_dirs_dict['names'] = _DATADIR_NAMES
    data_dirs_dict['paths_obj'] = _DATADIR_PATH_OBJS
    data_dirs_dict['paths_string'] = _DATADIR_PATH_STRINGS
    return data_dirs_dict 

def _ensure_dir(dir_path: Path) -> Path:
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

def _ensure_file(file_path: Path) -> Path:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch()
    return file_path

def data_path_resolver(
        data_file_path: str | Path | None=None, # e.g. "mydir/myfile.txt"
        data_dir_name: str = _DATADIR_NAMES['misc'], # e.g. "transcribe"   
        data_item_name: str | None=None, # e.g. "peter_test"
        data_item_subname: str | None=None, # e.g. "dec", "enc", "whisper_transcribe" 
        data_item_id: str | None=None, # e.g. timestamp_string, uuid
        data_file_suffix: str | None=None, # e.g. ".mp3", "_tts.mp3"
    ) -> dict[str, Any]:

    resolve_path_dict = {}

    resolve_source = ""

    if data_file_path is not None:
        resolve_source = 'data_file_path'

        if(isinstance(data_file_path, str)):
            file_path_obj = Path(data_file_path).expanduser().resolve()
        elif(isinstance(data_file_path, Path)):
            file_path_obj = data_file_path.expanduser().resolve()
        else:
            logger.error(f'data_file_path must be str or Path, not {type(data_file_path)}:\n{data_file_path}')
            return resolve_path_dict
        if(file_path_obj.is_dir()):
            logger.error(f'file_path_obj is dir, should be file instead:\n{file_path_obj}')
            return resolve_path_dict
        dir_path_obj = file_path_obj.parent
        _ensure_dir(dir_path_obj)

    else:
        resolve_source = 'data_dir_name'

        if (data_item_name is None or data_item_name == ""): data_item_name = "noname"

        if (data_item_subname is None): data_item_subname = ""
        else: data_item_subname = "_" + data_item_subname

        if (data_item_id is None): data_item_id = ""
        else: data_item_id = "_" + data_item_id

        if data_file_suffix is None: data_file_suffix = ""

        dir_path_obj = _PM_DATADIR_PATH / data_dir_name / data_item_name 
        dir_path_obj = Path(dir_path_obj).expanduser().resolve()
        _ensure_dir(dir_path_obj)

        file_stem = data_item_name + data_item_subname + data_item_id
        file_name = file_stem + data_file_suffix
        file_path_obj = _PM_DATADIR_PATH / data_dir_name / data_item_name / file_name
        file_path_obj = Path(file_path_obj).expanduser().resolve()


    dir_path_string = str(dir_path_obj)
    file_path_string = str(file_path_obj)

    resolve_path_dict = {

        'resolve_source': resolve_source,
        'data_file_path': data_file_path,
        'data_dir_name': data_dir_name,

        'dir_path_obj': dir_path_obj,

        'file_path_obj' : file_path_obj,
        'file_path_obj_name' : file_path_obj.name,
        'file_path_obj_stem' : file_path_obj.stem,
        'file_path_obj_suffix' : file_path_obj.suffix,

        'dir_path_string' : dir_path_string,
        'file_path_string': file_path_string,
    }

    # logger.debug(f'resolve_path_dict:\n{_pp.pformat(resolve_path_dict, sort_dicts=False)}')

    return resolve_path_dict

