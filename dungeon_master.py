"""world module"""


from elements.door import Door
from elements.location import Location
from elements.player import Player
from elements.thing import Thing
from constants import BED_DESCRIPTION, BED_NAME, BEDROOM_DESCRIPTION,\
    BEDROOM_NAME, DINING_ROOM_DESCRIPTION, DINING_ROOM_NAME, GENERIC_LOCATAION_NAME, INVALID_DIRECTION, LOCKED_DOOR,\
    PLAYER_DESCRIPTION, PLAYER_NAME, WEST


class DungeonMaster:
    """world class"""
    def __init__(self):
        self.player_location = None
        self.player = None

    def generate_world(self):
        """Generates the game world"""
        # bedroom
        bedroom = Location(BEDROOM_NAME, BEDROOM_DESCRIPTION)
        # dining room
        dining_room = Location(DINING_ROOM_NAME, DINING_ROOM_DESCRIPTION)

        # things in bedroom
        self.player = Player(PLAYER_NAME, PLAYER_DESCRIPTION)
        bed = Thing(BED_NAME, BED_DESCRIPTION)
        bed_dining_door = Door("Door", "A mundane wooden door.")
        bed_dining_door.connects.append(dining_room)
        bed_dining_door.locked = True

        # bedroom exits
        bedroom.exits[WEST] = dining_room
        # bedroom contents
        self.set_player_location(bedroom)
        bedroom.contents.append(bed)
        bedroom.contents.append(bed_dining_door)

    def move_player(self, direction):
        """Move the player from one location to the next, which lies in the given direction"""
        for element in self.player_location.contents:
            if isinstance(element, Door)\
            and self.player_location.exits[direction] in element.connects\
            and element.locked:
                return LOCKED_DOOR
        if direction in self.player_location.exits:
            self.player_location.contents.remove(self.player)
            self.set_player_location(self.player_location.exits[direction])
            return self.player_location.description
        else:
            return INVALID_DIRECTION

    def set_player_location(self, location):
        """Update the players location to a new one"""
        location.contents.append(self.player)
        self.player_location = location

    def describe(self, element_name):
        """Returns a desription of any kind of in-game element at the location of the player"""
        element_name = element_name.lower()
        if element_name == self.player_location.name or\
            element_name == GENERIC_LOCATAION_NAME or\
            element_name == "":
            return self.player_location.description
        for element in self.player_location.contents:
            if element.name.lower() == element_name:
                return element.description
