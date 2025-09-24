import json
from collections.abc import Callable
from os import PathLike

from mars_patcher.level_edits import apply_level_edits
from mars_patcher.mf.auto_generated_types import MarsSchemaMF
from mars_patcher.mf.connections import Connections
from mars_patcher.mf.credits import write_credits
from mars_patcher.mf.data import get_data_path
from mars_patcher.mf.door_locks import set_door_locks
from mars_patcher.mf.item_patcher import (
    ItemPatcher,
    set_required_metroid_count,
    set_tank_increments,
)
from mars_patcher.mf.locations import LocationSettings
from mars_patcher.mf.misc_patches import (
    apply_accessibility_patch,
    apply_base_patch,
    apply_instant_unmorph_patch,
    apply_pbs_without_bombs,
    apply_reveal_hidden_tiles,
    apply_reveal_unexplored_doors,
    apply_unexplored_map,
    change_missile_limit,
    disable_demos,
    disable_music,
    disable_sound_effects,
    skip_door_transitions,
    stereo_default,
)
from mars_patcher.mf.navigation_text import NavigationText
from mars_patcher.mf.room_names import write_room_names
from mars_patcher.mf.starting import set_starting_items, set_starting_location
from mars_patcher.minimap import apply_minimap_edits
from mars_patcher.random_palettes import PaletteRandomizer, PaletteSettings
from mars_patcher.rom import Rom
from mars_patcher.text import write_seed_hash
from mars_patcher.titlescreen_text import write_title_text


def patch_mf(
    rom: Rom,
    output_path: str | PathLike[str],
    patch_data: MarsSchemaMF,
    status_update: Callable[[str, float], None],
) -> None:
    """
    Creates a new randomized Fusion game, based off of an input path, an output path,
    a dictionary defining how the game should be randomized, and a status update function.

    Args:
        rom: Rom object for an unmodified Metroid Fusion (U) ROM.
        output_path: The path where the randomized Fusion ROM should be saved to.
        patch_data: A dictionary defining how the game should be randomized.
            This function assumes that it satisfies the needed schema. To validate it, use
            validate_patch_data_mf().
        status_update: A function taking in a message (str) and a progress value (float).
    """

    # Apply base asm patch first
    apply_base_patch(rom)

    # Randomize palettes - palettes are randomized first in case the item
    # patcher needs to copy tilesets
    if "Palettes" in patch_data:
        status_update("Randomizing palettes...", -1)
        pal_settings = PaletteSettings.from_json(patch_data["Palettes"])
        pal_randomizer = PaletteRandomizer(rom, pal_settings)
        pal_randomizer.randomize()

    # Load locations and set assignments
    status_update("Writing item assignments...", -1)
    loc_settings = LocationSettings.initialize()
    loc_settings.set_assignments(patch_data["Locations"])
    item_patcher = ItemPatcher(rom, loc_settings)
    item_patcher.write_items()

    # Required metroid count
    set_required_metroid_count(rom, patch_data["RequiredMetroidCount"])

    # Starting location
    if "StartingLocation" in patch_data:
        status_update("Writing starting location...", -1)
        set_starting_location(rom, patch_data["StartingLocation"])

    # Starting items
    if "StartingItems" in patch_data:
        status_update("Writing starting items...", -1)
        set_starting_items(rom, patch_data["StartingItems"])

    # Tank increments
    if "TankIncrements" in patch_data:
        status_update("Writing tank increments...", -1)
        set_tank_increments(rom, patch_data["TankIncrements"])

    # Elevator connections
    conns = None
    if "ElevatorConnections" in patch_data:
        status_update("Writing elevator connections...", -1)
        conns = Connections(rom)
        conns.set_elevator_connections(patch_data["ElevatorConnections"])

    # Sector shortcuts
    if "SectorShortcuts" in patch_data:
        status_update("Writing sector shortcuts...", -1)
        if conns is None:
            conns = Connections(rom)
        conns.set_shortcut_connections(patch_data["SectorShortcuts"])

    # Hints
    if nav_text := patch_data.get("NavigationText", {}):
        status_update("Writing navigation text...", -1)
        navigation_text = NavigationText.from_json(nav_text)
        navigation_text.write(rom)

    if nav_locks := patch_data.get("NavStationLocks", {}):
        status_update("Writing navigation locks...", -1)
        NavigationText.apply_hint_security(rom, nav_locks)

    # Room Names
    if room_names := patch_data.get("RoomNames", []):
        status_update("Writing room names...", -1)
        write_room_names(rom, room_names)

    # Credits
    if credits_text := patch_data.get("CreditsText", []):
        status_update("Writing credits text...", -1)
        write_credits(rom, credits_text)

    # Misc patches
    if patch_data.get("AccessibilityPatches"):
        apply_accessibility_patch(rom)

    if patch_data.get("DisableDemos"):
        disable_demos(rom)

    if patch_data.get("InstantUnmorph"):
        apply_instant_unmorph_patch(rom)

    if patch_data.get("SkipDoorTransitions"):
        skip_door_transitions(rom)

    if patch_data.get("StereoDefault", True):
        stereo_default(rom)

    if patch_data.get("DisableMusic"):
        disable_music(rom)

    if patch_data.get("DisableSoundEffects"):
        disable_sound_effects(rom)

    if "MissileLimit" in patch_data:
        change_missile_limit(rom, patch_data["MissileLimit"])

    if patch_data.get("PowerBombsWithoutBombs"):
        apply_pbs_without_bombs(rom)

    if patch_data.get("UnexploredMap"):
        apply_unexplored_map(rom)

        if not patch_data.get("HideDoorsOnMinimap", False):
            apply_reveal_unexplored_doors(rom)

    if patch_data.get("RevealHiddenTiles"):
        apply_reveal_hidden_tiles(rom)

    if "LevelEdits" in patch_data:
        apply_level_edits(rom, patch_data["LevelEdits"])

    # Apply base minimap edits
    with open(get_data_path("base_minimap_edits.json")) as f:
        edits_dict = json.load(f)
    apply_minimap_edits(rom, edits_dict)

    # Apply JSON minimap edits
    if "MinimapEdits" in patch_data:
        apply_minimap_edits(rom, patch_data["MinimapEdits"])

    # Door locks
    if door_locks := patch_data.get("DoorLocks", []):
        status_update("Writing door locks...", -1)
        set_door_locks(rom, door_locks)

    write_seed_hash(rom, patch_data["SeedHash"])

    # Title-screen text
    if title_screen_text := patch_data.get("TitleText"):
        status_update("Writing title screen text...", -1)
        write_title_text(rom, title_screen_text)

    rom.save(output_path)
    status_update(f"Output written to {output_path}", -1)
