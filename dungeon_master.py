"""world module"""


from elements.container import Container
from elements.door import Door
from elements.location import Location
from elements.player import Player
from elements.thing import Thing
from texts import BED_DESCRIPTION, BED_NAME, BEDROOM_DESCRIPTION, BEDROOM_DOOR_DESCRIPTION,\
    BEDROOM_DOOR_NAME, BEDROOM_HOOK_DESCRIPTION, BEDROOM_HOOK_NAME, BEDROOM_KEY_DESCRIPTION,\
    BEDROOM_KEY_NAME, BEDROOM_NAME, BEDROOM_RUG_DESCRIPTION, BEDROOM_RUG_NAME, DINING_ROOM_DESCRIPTION, DINING_ROOM_NAME, EAST, ELEMENT_NOT_FOUND,\
    KEY_MISSING, LOCATION_PREFIX, LOCATION_SUFFIX,\
    door_not_locked, door_unlocked, GENERIC_LOCATAION_NAME, INVALID_DIRECTION, LOCKED_DOOR,\
    PLAYER_DESCRIPTION, PLAYER_NAME, WEST, picked_up_element, element_in_container


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
        bedroom_hook.peekable = True
        bedroom_hook.fixed = True
        bedroom_hook.contents.append(bedroom_key)
        bedroom_rug = Thing(BEDROOM_RUG_NAME, BEDROOM_RUG_DESCRIPTION)
        # bedroom exits
        bedroom.exits[WEST] = dining_room
        # bedroom contents
        self.set_player_location(bedroom)
        bedroom.contents.append(bed)
        bedroom.contents.append(bedroom_door)
        bedroom.contents.append(bedroom_hook)
        bedroom.contents.append(bedroom_rug)
        # dining room exits
        dining_room.exits[EAST] = bedroom
        # dining room contents
        dining_room.contents.append(bedroom_door)
        bedroom_door.connects.append(bedroom)

    def move_player(self, direction):
        """Move the player from one location to the next, which lies in the given direction"""
        if direction in self.player_location.exits:
            next_room = self.player_location.exits[direction]
            for element in self.player_location.contents:
                if isinstance(element, Door)\
                and next_room in element.connects\
                and element.locked:
                    return LOCKED_DOOR
            self.player_location.contents.remove(self.player)
            self.set_player_location(next_room)
            return self.player_location.description
        else:
            return INVALID_DIRECTION

    def unlock(self, door_name):
        """Unlocks and opens a door"""
        door = self.get_element_container(door_name, self.player_location)[0]
        if not door.locked:
            return door_not_locked(door_name)
        if door.key in self.player.contents:
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
        if element_name == self.player_location.name or\
            element_name == GENERIC_LOCATAION_NAME or\
            element_name == "":
            return self.describe_location()
        else:
            return self.describe_element(element_name)

    def describe_location(self):
        """Describes the location where the player is"""
        return self.describe_container(self.player_location, (LOCATION_PREFIX, LOCATION_SUFFIX))

    def describe_element(self, element_name):
        """Get description of a single element"""
        element_container = self.get_element_container(element_name, self.player_location)
        if element_container:
            return self.describe_container(element_container[0])
        else:
            return ELEMENT_NOT_FOUND

    def describe_container(self, top_container, prefix_suffix=None):
        """Descsribe any container and its contents and all the contents contents etc."""
        if prefix_suffix:
            description = top_container.name + "\n" + prefix_suffix[0] +\
            top_container.description.lower() + prefix_suffix[1]
        else:
            description = top_container.name + "\n" + top_container.description.lower()
        visible_elements = self.get_all_visible_elements(top_container)
        for element_container in visible_elements:
            if element_container[1] is not self.player_location:
                description = description + "\n" +\
                element_in_container(element_container[0].name, element_container[1].name)
            else:
                if not isinstance(element_container[0], Player):
                    description = description + "\n" + element_container[0].description
        return description


    def get_element_container(self, element_name, container):
        """Get an element in the container
        by its name and the corresponding container.
        If it's not found it returns None"""
        for element_container in self.get_all_visible_elements(container):
            element = element_container[0]
            if element.name.lower() == element_name:
                return (element, element_container[1])
        return None

    def get_all_visible_elements(self, container):
        """Recursive method to get all elements in the container
        and their corresponding container. If there is nothing it returns None"""
        visible_elements_container = []
        for element in container.contents:
            if element.visible:
                visible_elements_container.append((element, container))
            if self.is_peekable_container(element):
                visible_elements_container = visible_elements_container +\
                self.get_all_visible_elements(element)
        return visible_elements_container

    def is_peekable_container(self, element):
        """Check if element is a container and if it is open or transparent"""
        return isinstance(element, Container) and element.peekable or\
        isinstance(element, Container) and element.open

    def take(self, element_name):
        """Take an element and put it into the players inventory"""
        element_container = self.get_element_container(element_name, self.player_location)
        if not element_container:
            return ELEMENT_NOT_FOUND
        element_container[1].contents.remove(element_container[0])
        self.player.contents.append(element_container[0])
        return picked_up_element(element_container[0].name)

    def get_player_inventory(self):
        """Returns the invenotry of the player as a string listing all things"""
        description = ""
        for element in self.player.contents:
            description = description + element.name + "\n"
        return description
