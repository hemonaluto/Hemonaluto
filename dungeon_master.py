"""world module"""


from elements.container import Container
from elements.door import Door
from elements.location import Location
from elements.player import Player
from elements.thing import Thing
from texts import BED_DESCRIPTION, BED_NAME, BEDROOM_DESCRIPTION, BEDROOM_DOOR_DESCRIPTION,\
    BEDROOM_DOOR_NAME, BEDROOM_HOOK_DESCRIPTION, BEDROOM_HOOK_NAME, BEDROOM_KEY_DESCRIPTION,\
    BEDROOM_KEY_NAME, BEDROOM_NAME, DINING_ROOM_DESCRIPTION, DINING_ROOM_NAME, ELEMENT_NOT_FOUND, KEY_MISSING, LOCATION_PREFIX, LOCATION_SUFFIX,\
    door_not_locked, door_unlocked, GENERIC_LOCATAION_NAME, INVALID_DIRECTION, LOCKED_DOOR,\
    PLAYER_DESCRIPTION, PLAYER_NAME, WEST, thing_in_container


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
        bedroom_door = Door(BEDROOM_DOOR_NAME, BEDROOM_DOOR_DESCRIPTION)
        bedroom_door.connects.append(dining_room)
        bedroom_door.locked = True
        bedroom_key = Thing(BEDROOM_KEY_NAME, BEDROOM_KEY_DESCRIPTION)
        bedroom_door.key = bedroom_key
        bedroom_hook = Container(BEDROOM_HOOK_NAME, BEDROOM_HOOK_DESCRIPTION)
        bedroom_hook.transparent = True
        bedroom_hook.fixed = True
        bedroom_hook.contents.append(bedroom_key)
        # bedroom exits
        bedroom.exits[WEST] = dining_room
        # bedroom contents
        self.set_player_location(bedroom)
        bedroom.contents.append(bed)
        bedroom.contents.append(bedroom_door)
        bedroom.contents.append(bedroom_hook)

    def move_player(self, direction):
        """Move the player from one location to the next, which lies in the given direction"""
        next_room = self.player_location.exits[direction]
        for element in self.player_location.contents:
            if isinstance(element, Door)\
            and next_room in element.connects\
            and element.locked:
                return LOCKED_DOOR
        if direction in self.player_location.exits:
            self.player_location.contents.remove(self.player)
            self.set_player_location(next_room)
            return self.player_location.description
        else:
            return INVALID_DIRECTION

    def unlock(self, door_name):
        """Unlock and or open doors"""
        for element in self.player_location.contents:
            if element.name.lower() is door_name:
                door = element
                if not door.locked:
                    return door_not_locked(door_name)
                if door.key in self.player.inventory:
                    door.locked = False
                    return door_unlocked(door_name)
                else:
                    return KEY_MISSING


    def set_player_location(self, location):
        """Update the players location to a new one"""
        location.contents.append(self.player)
        self.player_location = location

    def describe(self, element_name):
        """Returns a desription of any kind of in-game element at the location of the player"""
        element_name = element_name.lower()
        description = None
        if element_name == self.player_location.name or\
            element_name == GENERIC_LOCATAION_NAME or\
            element_name == "":
            description = self.player_location.name + "\n" + LOCATION_PREFIX +\
            self.player_location.description.lower() + LOCATION_SUFFIX
            for element in self.player_location.contents:
                if not isinstance(element, Player):
                    description = description + "\n" + element.description
                description = self.if_peekable_extend_description(element, description)
        else:
            for element in self.player_location.contents:
                if element.name.lower() == element_name:
                    description = element.description
                    description = self.if_peekable_extend_description(element, description)
                if self.is_peekable_container(element):
                    for thing in element.contents:
                        if thing.name.lower() == element_name:
                            description = thing.description
        return description
   
    def get_element_by_name_or_none(self, element_name):
        """Get an element in the players location by its name. If it's not found it returns None"""
        for element in self.player_location.contents:
            if element.name.lower() == element_name:
                return element
            if self.is_peekable_container(element):
                for thing in element.contents:
                    if thing.name.lower() == element_name:
                        return element
        return None

    def if_peekable_extend_description(self, element, description):
        """If an element is peekable return the description for it"""
        if self.is_peekable_container(element):
            return description + "\n" +\
            thing_in_container(self.things_as_string(element.contents), element.name)
        else:
            return description

    def is_peekable_container(self, element):
        """Check if element is a container and if it is open or transparent"""
        return isinstance(element, Container) and element.transparent or\
        isinstance(element, Container) and element.open

    def things_as_string(self, things):
        """Convert a list of things into a grammatically correct human readable list"""
        if len(things) > 1:
            things_as_string_missing_last = ','.join(things[:-1])
            things_as_string = things_as_string_missing_last + " and a " + things[-1]
            return things_as_string
        if len(things) == 1:
            return things[0].name
        return "nothing"

    def take(self, element_name):
        """Take an element and put it into the players inventory"""
        element = self.get_element_by_name_or_none(element_name)
        if not element:
            return ELEMENT_NOT_FOUND
        self.player_location.contents.remove(element)
        self.player.inventory.append(element)
