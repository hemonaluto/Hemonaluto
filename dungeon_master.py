"""dungeon master module"""
from elements.animate import Animate
from elements.chest import Chest
from elements.door import Door
from elements.player import Player
from elements.thing import Thing
from save_handler import SaveHandler
from texts import CLOSED, FAILED_SAVE_MESSAGE,\
    KEY_MISSING, LOADED_SAVE_MESSAGE, LOCATION_PREFIX, LOCATION_SUFFIX, NOT_OPENABLE, NOT_READABLE,\
    SAVED_GAME_MESSAGE, THREW_AT_NOTHING, door_not_locked, door_unlocked, GENERIC_LOCATAION_NAME,\
    INVALID_DIRECTION, LOCKED_DOOR, element_not_found, hit_target, picked_up_element, element_in_container


class DungeonMaster:
    """dungeon master class"""
    def __init__(self):
        self.player_location = None
        self.all_name_locations = []
        self.save_handler = SaveHandler()
        self.player_score = 0

    def get_player(self):
        """Get the player object from the current location"""
        return self.get_element_container("Player", self.player_location)[0]

    def get_score(self):
        """Get the current score"""
        return self.player_score

    def get_health(self):
        """Get the current health"""
        return self.get_player().health

    def move_player(self, direction):
        """Move the player from one location to the next, which lies in the given direction"""
        if direction in self.player_location.exits:
            all_name_rooms_dict =  dict(self.all_name_locations)
            next_room = all_name_rooms_dict[self.player_location.exits[direction]]
            for element in self.player_location.contents:
                if isinstance(element, Door):
                    if next_room.name in element.connects and element.locked:
                        return LOCKED_DOOR
                    element.open = True
            player = self.get_player()
            self.player_location.contents.remove(player)
            self.set_player_location(player, next_room)
            return self.player_location.name
        return INVALID_DIRECTION

    def unlock(self, door_name):
        """Unlocks and opens a door"""
        door = self.get_element_container(door_name, self.player_location)[0]
        if not door.locked:
            return door_not_locked(door_name)
        if any(element.name == door.key for element in self.get_player().contents):
            self.player_score = self.player_score + 1
            door.locked = False
            return door_unlocked(door_name)
        return KEY_MISSING

    def set_player_location(self, player, location):
        """Update the players location to a new one"""
        location.contents.append(player)
        self.player_location = location

    def describe(self, element_name):
        """Returns a desription of any kind of in-game element at the location of the player"""
        element_name = element_name.lower()
        if element_name in (self.player_location.name, GENERIC_LOCATAION_NAME, ''):
            return self.describe_location()
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
            return element_not_found(element_name)

    def describe_container(self, top_container, prefix_suffix=None):
        """Descsribe any container and its contents and all the contents contents etc."""
        if prefix_suffix:
            description = top_container.name + "\n" + prefix_suffix[0] +\
            top_container.description.lower() + prefix_suffix[1]
        else:
            description = top_container.description
        visible_elements = self.get_all_elements_container(top_container, True)
        for element_container in visible_elements:
            if element_container[1] is not self.get_player():
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
        for element_container in self.get_all_elements_container(container, True):
            element = element_container[0]
            if element.name.lower() == element_name.lower():
                return (element, element_container[1])

    def get_all_elements_container(self, container, only_visible=False, only_takeable=False):
        """Recursive method to get all elements in the container
        and their corresponding container. If there is nothing it returns None"""
        elements_container = []
        if only_takeable:
            for element in container.contents:
                if isinstance(element, Thing) and element.visible and not element.fixed:
                    elements_container.append((element, container))
                elements_container = elements_container +\
                self.get_all_elements_container(element, only_visible, only_takeable)
            return elements_container
        if only_visible:
            for element in container.contents:
                if element.visible:
                    elements_container.append((element, container))
                if isinstance(element, Chest) and not element.peekable or\
                isinstance(element, Chest) and not element.open:
                    pass
                else:
                    elements_container = elements_container +\
                    self.get_all_elements_container(element, only_visible)
            return elements_container
        if not only_visible:
            for element in container.contents:
                elements_container.append((element, container))
                elements_container = elements_container +\
                self.get_all_elements_container(element, only_visible)
            return elements_container
        return None

    def take(self, element_name):
        """Take all elements or a single element and put it into the players inventory"""
        if element_name == "all":
            all_takeable = self.get_all_elements_container(self.player_location, only_takeable=True)
            response = ""
            for element_container in all_takeable:
                if not isinstance(element_container[0], Player) and not element_container[0].fixed:
                    element_container[1].contents.remove(element_container[0])
                    self.get_player().contents.append(element_container[0])
                    response = response + picked_up_element(element_container[0].name) + "\n"
            return response
        element_container = self.get_element_container(element_name, self.player_location)
        if not element_container:
            return element_not_found(element_name)
        element_container[1].contents.remove(element_container[0])
        self.get_player().contents.append(element_container[0])
        return picked_up_element(element_container[0].name)

    def get_player_inventory(self):
        """Returns the invenotry of the player as a string listing all things"""
        description = ""
        for element in self.get_player().contents:
            description = description + element.name + "\n"
        return description

    def save(self):
        """Saves the game state to file"""
        if self.save_handler.save(self.all_name_locations, "save.json"):
            return SAVED_GAME_MESSAGE
        return FAILED_SAVE_MESSAGE

    def load(self, filename):
        """Loads the game state from file"""
        load_data = self.save_handler.load(filename)
        self.all_name_locations = load_data[0]
        self.player_location = load_data[1]
        return LOADED_SAVE_MESSAGE

    def throw(self, instructions):
        """Throws an item"""
        if "at" in instructions:
            thing_target = instructions.split(" at ")
            thing = self.get_element_container(thing_target[0], self.player_location)[0]
            if thing is None:
                return element_not_found(thing.name)
            target = self.get_element_container(thing_target[1], self.player_location)[0]
            if target is None:
                return element_not_found(target.name)
            if isinstance(target, Animate):
                self.get_player().contents.remove(thing)
                target.health = target.health - thing.damage * 1.5
                self.player_location.contents.append(thing)
                return hit_target(target.name)
        thing = self.get_element_container(instructions, self.player_location)
        self.get_player().contents.remove(thing[0])
        self.player_location.contents.append(thing[0])
        return THREW_AT_NOTHING

    def close(self, element_name):
        """Closes a door or chest element"""
        element_container = self.get_element_container(element_name, self.player_location)
        if isinstance(element_container[0], (Chest, Door)):
            element_container[0].open = False
            return CLOSED
        return NOT_OPENABLE

    def read(self, element_name):
        """Read an elements text"""
        element_container = self.get_element_container(element_name, self.player_location)
        if isinstance(element_container[0], Thing) and element_container[0].text:
            return element_container[0].text
        return NOT_READABLE
