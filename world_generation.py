"""Generates the game world"""


from elements.door import Door
from elements.location import Location
from elements.player import Player
from elements.thing import Thing
from save_handler import SaveHandler
from texts import BED_DESCRIPTION, BED_NAME, BEDROOM_DESCRIPTION, BEDROOM_DOOR_DESCRIPTION,\
BEDROOM_DOOR_NAME, BEDROOM_HOOK_DESCRIPTION, BEDROOM_HOOK_NAME, BEDROOM_KEY_DESCRIPTION,\
BEDROOM_KEY_NAME, BEDROOM_NAME, BEDROOM_RUG_DESCRIPTION, BEDROOM_RUG_NAME, DINING_ROOM_DESCRIPTION,\
DINING_ROOM_NAME, EAST, PLAYER_DESCRIPTION, PLAYER_NAME, WEST


all_name_locations = []
# bedroom
bedroom = Location(BEDROOM_NAME, BEDROOM_DESCRIPTION)
# dining room
dining_room = Location(DINING_ROOM_NAME, DINING_ROOM_DESCRIPTION)
# things in bedroom
player = Player(PLAYER_NAME, PLAYER_DESCRIPTION)
bed = Thing(BED_NAME, BED_DESCRIPTION)
bedroom_door = Door(BEDROOM_DOOR_NAME, BEDROOM_DOOR_DESCRIPTION)
bedroom_door.connects.append(dining_room.name)
bedroom_door.locked = True
bedroom_key = Thing(BEDROOM_KEY_NAME, BEDROOM_KEY_DESCRIPTION)
bedroom_door.key = bedroom_key.name
bedroom_hook = Thing(BEDROOM_HOOK_NAME, BEDROOM_HOOK_DESCRIPTION)
bedroom_hook.contents.append(bedroom_key)
bedroom_rug = Thing(BEDROOM_RUG_NAME, BEDROOM_RUG_DESCRIPTION)
# bedroom exits
bedroom.exits[WEST] = dining_room.name
# bedroom contents
bedroom.contents.append(player)
bedroom.contents.append(bed)
bedroom.contents.append(bedroom_door)
bedroom.contents.append(bedroom_hook)
bedroom.contents.append(bedroom_rug)
# dining room exits
dining_room.exits[EAST] = bedroom.name
# dining room contents
dining_room.contents.append(bedroom_door)
bedroom_door.connects.append(bedroom.name)
# add all rooms to all_name_rooms list
all_name_locations.append((bedroom.name, bedroom))
all_name_locations.append((dining_room.name, dining_room))
save_handler = SaveHandler()
save_handler.save(all_name_locations, "scenario.json")
