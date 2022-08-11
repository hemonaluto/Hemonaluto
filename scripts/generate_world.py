"""Generates the game world"""
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH
)
sys.path.append(SOURCE_PATH)
from game.game.model.activator import Activator
from game.game.model.door import Door
from game.game.model.food import Food
from game.game.model.location import Location
from game.game.model.player import Player
from game.game.model.rope import Rope
from game.game.model.thing import Thing
from game.game.model.tool import Tool
from game.game.model.enums.activator_type import ActivatorType
from game.game.controller.save_controller import SaveHandler
from game.game.data.texts import UP, DOWN, EAST, WEST
from game.game.data.scenario_texts import BED_DESCRIPTION, BED_NAME, BEDROOM_BRIEF, BEDROOM_BUTTON_DESCRIPTION,\
BEDROOM_BUTTON_NAME, BEDROOM_DESCRIPTION, BEDROOM_DOOR_DESCRIPTION,\
BEDROOM_DOOR_NAME, BEDROOM_HOOK_DESCRIPTION, BEDROOM_HOOK_NAME, BEDROOM_KEY_DESCRIPTION,\
BEDROOM_KEY_NAME, BEDROOM_KEY_TEXT, BEDROOM_NAME, BEDROOM_PILE_OF_DUST_DESCRIPTION,\
BEDROOM_PILE_OF_DUST_NAME, BEDROOM_RUG_DESCRIPTION, BEDROOM_RUG_NAME,\
BREAKFAST_KNIFE_DESCRIPTION, BREAKFAST_KNIFE_NAME, CELLAR_ALTAR_DESCRIPTION, CELLAR_ALTAR_NAME, CELLAR_BRIEF,\
CELLAR_DESCRIPTION, CELLAR_NAME, CELLAR_SKELETON_DESCRIPTION,\
CELLAR_SKELETON_NAME, DINING_ROOM_BRIEF, DINING_ROOM_CRATE_DESCRIPTION, DINING_ROOM_CRATE_NAME,\
DINING_ROOM_DESCRIPTION, DINING_ROOM_FIREPLACE_DESCRIPTION, DINING_ROOM_FIREPLACE_NAME,\
DINING_ROOM_FIREPLACE_SOUND, DINING_ROOM_FOOD_DESCRIPTION, DINING_ROOM_FOOD_NAME,\
DINING_ROOM_FOOD_SMELL, DINING_ROOM_FOOD_TASTE, DINING_ROOM_NAME,\
DINING_ROOM_PLATE_DESCRIPTION, DINING_ROOM_PLATE_NAME, DINING_ROOM_TABLE_DESCRIPTION,\
DINING_ROOM_TABLE_NAME, DINING_ROOM_TRAPDOOR_DESCRIPTION, DINING_ROOM_TRAPDOOR_NAME,\
PLAYER_DESCRIPTION, PLAYER_NAME, ROPE_DESCRIPTION, ROPE_NAME


all_name_locations = []
# Create all game elements
player = Player(PLAYER_NAME, PLAYER_DESCRIPTION)
player.health = 100
bedroom = Location(BEDROOM_NAME, BEDROOM_DESCRIPTION)
bedroom.brief = BEDROOM_BRIEF
bedroom.exits[WEST] = DINING_ROOM_NAME
bed = Thing(BED_NAME, BED_DESCRIPTION)
bed.fixed = True
bed.enterable = True
bedroom_door = Door(BEDROOM_DOOR_NAME, BEDROOM_DOOR_DESCRIPTION)
bedroom_door.connects.append(DINING_ROOM_NAME)
bedroom_door.locked = True
bedroom_key = Thing(BEDROOM_KEY_NAME, BEDROOM_KEY_DESCRIPTION)
bedroom_key.text = BEDROOM_KEY_TEXT
bedroom_door.key = BEDROOM_KEY_NAME
bedroom_hook = Thing(BEDROOM_HOOK_NAME, BEDROOM_HOOK_DESCRIPTION)
bedroom_hook.fixed = True
bedroom_hook.contents.append(bedroom_key)
bedroom_rug = Thing(BEDROOM_RUG_NAME, BEDROOM_RUG_DESCRIPTION)
bedroom_button = Activator(BEDROOM_BUTTON_NAME, BEDROOM_BUTTON_DESCRIPTION)
bedroom_button.type = ActivatorType.PRESS
bedroom_button.turn_on_method_name = "bedroom_button_on"
bedroom_button.turn_off_method_name = "bedroom_button_off"
bedroom_pile_of_dust = Thing(BEDROOM_PILE_OF_DUST_NAME, BEDROOM_PILE_OF_DUST_DESCRIPTION)
bedroom_pile_of_dust.visible = False
bedroom_rug.reveals = bedroom_pile_of_dust.name
bedroom_door.connects.append(BEDROOM_NAME)
bedroom.contents.extend([player, bed, bedroom_door, bedroom_hook,\
    bedroom_rug, bedroom_button, bedroom_pile_of_dust])
dining_room = Location(DINING_ROOM_NAME, DINING_ROOM_DESCRIPTION)
dining_room.brief = DINING_ROOM_BRIEF
dining_room.exits[EAST] = BEDROOM_NAME
dining_room.exits[DOWN] = CELLAR_NAME
dining_room_table = Thing(DINING_ROOM_TABLE_NAME, DINING_ROOM_TABLE_DESCRIPTION)
dining_room_table.preposition = "on"
dining_room_plate = Thing(DINING_ROOM_PLATE_NAME, DINING_ROOM_PLATE_DESCRIPTION)
dining_room_plate.preposition = "on"
dining_room_breakfast = Food(DINING_ROOM_FOOD_NAME, DINING_ROOM_FOOD_DESCRIPTION)
dining_room_breakfast.taste = DINING_ROOM_FOOD_TASTE
dining_room_breakfast.smell = DINING_ROOM_FOOD_SMELL
dining_room_plate.contents.append(dining_room_breakfast)
dining_room_trapdoor = Door(DINING_ROOM_TRAPDOOR_NAME, DINING_ROOM_TRAPDOOR_DESCRIPTION)
rope = Rope(ROPE_NAME, ROPE_DESCRIPTION)
dining_room_crate = Thing(DINING_ROOM_CRATE_NAME, DINING_ROOM_CRATE_DESCRIPTION)
dining_room_crate.fixed = True
breakfast_knife = Tool(BREAKFAST_KNIFE_NAME, BREAKFAST_KNIFE_DESCRIPTION)
dining_room_plate.when_broken_do = "break_plate"
dining_room_fireplace = Thing(DINING_ROOM_FIREPLACE_NAME, DINING_ROOM_FIREPLACE_DESCRIPTION)
dining_room_fireplace.sound = DINING_ROOM_FIREPLACE_SOUND
dining_room_table.contents.extend([dining_room_plate, breakfast_knife])
dining_room.contents.extend([dining_room_table, dining_room_trapdoor,\
    rope, dining_room_crate, dining_room_fireplace])
cellar = Location(CELLAR_NAME, CELLAR_DESCRIPTION)
cellar.brief = CELLAR_BRIEF
cellar.exits[UP] = dining_room.name
cellar.needs_rope = True
cellar_altar = Thing(CELLAR_ALTAR_NAME, CELLAR_ALTAR_DESCRIPTION)
cellar_skeleton = Thing(CELLAR_SKELETON_NAME, CELLAR_SKELETON_DESCRIPTION)
cellar.contents.extend([cellar_altar, cellar_skeleton])

# add all rooms to all_name_rooms list and save
all_name_locations.append((bedroom.name, bedroom))
all_name_locations.append((dining_room.name, dining_room))
all_name_locations.append((cellar.name, cellar))
save_handler = SaveHandler()
save_handler.save(all_name_locations, "game/data/scenario.json")
