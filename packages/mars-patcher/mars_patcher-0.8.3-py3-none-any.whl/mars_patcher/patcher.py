import json
import typing
from collections.abc import Callable
from os import PathLike

from jsonschema import validate

import mars_patcher.mf.data as data_mf
import mars_patcher.zm.data as data_zm
from mars_patcher.mf.auto_generated_types import MarsSchemaMF
from mars_patcher.mf.patcher import patch_mf
from mars_patcher.rom import Rom
from mars_patcher.zm.auto_generated_types import MarsSchemaZM
from mars_patcher.zm.patcher import patch_zm


def validate_patch_data_mf(patch_data: dict) -> MarsSchemaMF:
    """
    Validates whether the specified patch_data satisfies the schema for it.

    Raises:
        ValidationError: If the patch data does not satisfy the schema.
    """
    with open(data_mf.get_data_path("schema.json")) as f:
        schema = json.load(f)
    validate(patch_data, schema)
    return typing.cast("MarsSchemaMF", patch_data)


def validate_patch_data_zm(patch_data: dict) -> MarsSchemaZM:
    """
    Validates whether the specified patch_data satisfies the schema for it.

    Raises:
        ValidationError: If the patch data does not satisfy the schema.
    """
    with open(data_zm.get_data_path("schema.json")) as f:
        schema = json.load(f)
    validate(patch_data, schema)
    return typing.cast("MarsSchemaZM", patch_data)


def patch(
    input_path: str | PathLike[str],
    output_path: str | PathLike[str],
    patch_data: dict,
    status_update: Callable[[str, float], None],
) -> None:
    """
    Creates a new randomized GBA Metroid game, based off of an input path, an output path,
    a dictionary defining how the game should be randomized, and a status update function.

    Args:
        input_path: The path to an unmodified GBA Metroid (U) ROM.
        output_path: The path where the randomized GBA Metroid ROM should be saved to.
        patch_data: A dictionary defining how the game should be randomized.
        status_update: A function taking in a message (str) and a progress value (float).
    """

    # Load input rom
    rom = Rom(input_path)

    if rom.is_mf():
        patch_mf(rom, output_path, validate_patch_data_mf(patch_data), status_update)
    elif rom.is_zm():
        patch_zm(rom, output_path, validate_patch_data_zm(patch_data), status_update)
    else:
        raise ValueError(rom)
