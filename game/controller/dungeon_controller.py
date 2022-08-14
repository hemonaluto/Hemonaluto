"""kind of like a dungeon master that controls everything that's happening in the in-game world"""
# pylint: disable=no-name-in-module
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
import re
from typing import Tuple
import pkg_resources
from game.model.element import Element
from game.model.location import Location
from game.model.activator import Activator
from game.model.animate import Animate
from game.model.chest import Chest
from game.model.door import Door
from game.model.player import Player
from game.model.rope import Rope
from game.model.thing import Thing
from game.model.tool import Tool
from game.model.enums.activator_type import ActivatorType
from game.helper_methods import isinstanceorsubclass
from game.controller.activator_controller import ActivatorController
from game.controller.save_controller import SaveController
from game.data.texts import ACTION_FAILED, ACTION_NOT_POSSIBLE, ALREADY_OFF, ALREADY_ON,\
    ALREADY_UNTIED, APPEARING, CANT_BREAK, CANT_SEE_LOCATION_FROM_HIDING,\
    CANT_TIE_TO_ELEMENT, CLIMBING_DOWN, CLOSED, DONE, DOWN,\
    FAILED_SAVE_MESSAGE, KEY_MISSING, LOADED_SAVE_MESSAGE, LOCATION_PREFIX,\
    LOCATION_SUFFIX, NEEDS_TO_BE_TOOL, NO_SMELLS, NO_TIED_ROPE, NOT_ENTERABLE,\
    NOT_HIDING, NOT_OPENABLE, NOT_READABLE, NOTHING_HAPPENS, SAVED_GAME_MESSAGE,\
    SILENCE, SPECIFIY_HIDING_PLACE, TARGET_NOT_SPECIFIED, THAT_WONT_HOLD,\
    THREW_AT_NOTHING, TURNED_OFF, TURNED_ON, UNTIE, WEAPON_NOT_SPECIFIED,\
    door_leads_to, door_not_locked, door_unlocked, GENERIC_LOCATAION_NAME,\
    INVALID_DIRECTION, LOCKED_DOOR, eat_food, element_not_found, element_not_in_inventory,\
    entering_thing, hit_target, noises_description, picked_up_element,\
    element_in_container, reveal_element, smell_description, tie_rope_to_target


class DungeonController:
    """dungeon controller (dungeon master) class"""
    def __init__(self):
        self.player_location = None
        self.all_name_locations = []
        self.save_handler = SaveController()
        self.player_score = 0
        self.activator_handler = ActivatorController()

    def brief(self, room_name: str):
        """Debrief the player if they arrive at a location they've never been"""
        for name_location in self.all_name_locations:
            if name_location[0] == room_name and\
                not name_location[1].visited and\
                name_location[1].brief:
                name_location[1].visited = True
                return name_location[1].brief + "\n\n"
        return ""

    def get_player(self):
        """Get the player object from the current location"""
        return self.get_element_container("Player", self.player_location)[0]

    def get_score(self):
        """Get the current score"""
        return self.player_score

    def get_health(self):
        """Get the current health"""
        return self.get_player().health

    def move_player(self, direction: str):
        """Move the player from one location to the next, which lies in the given direction"""
        if direction in self.player_location.exits:
            travel_text = ""
            all_name_rooms_dict = dict(self.all_name_locations)
            next_room = all_name_rooms_dict[self.player_location.exits[direction]]
            room_has_attached_rope = False
            for element in self.player_location.contents:
                if isinstanceorsubclass(element, Door):
                    if next_room.name in element.connects and element.locked:
                        return LOCKED_DOOR
                    element.open = True
                if isinstanceorsubclass(element, Rope) and\
                    direction == DOWN and next_room.needs_rope:
                    if not element.tied_to:
                        return NO_TIED_ROPE
                    room_has_attached_rope = True
                    travel_text = CLIMBING_DOWN + "\n"
            if next_room.needs_rope and room_has_attached_rope is False:
                return NO_TIED_ROPE
            player = self.get_player()
            self.player_location.contents.remove(player)
            self.set_player_location(player, next_room)
            brief_text = ""
            brief_text = self.brief(next_room.name)
            return f"{travel_text}{brief_text}{self.player_location.name}"
        return INVALID_DIRECTION

    def unlock(self, door_name: str):
        """Unlocks and opens a door"""
        door = self.get_element_container(door_name, self.player_location)[0]
        if not door.locked:
            return door_not_locked(door_name)
        if any(element.name == door.key for element in self.get_player().contents):
            self.player_score = self.player_score + 1
            door.locked = False
            return door_unlocked(door_name)
        return KEY_MISSING

    def set_player_location(self, player: Player, location: Location):
        """Update the players location to a new one"""
        location.contents.append(player)
        self.player_location = location

    def describe(self, element_name: str):
        """Returns a desription of any kind of in-game element at the location of the player"""
        element_name = element_name.lower()
        if element_name in (self.player_location.name, GENERIC_LOCATAION_NAME, ''):
            return self.describe_location()
        return self.describe_element(element_name)

    def describe_location(self):
        """Describes the location where the player is"""
        if not self.get_player().hiding:
            return self.describe_container(self.player_location, (LOCATION_PREFIX, LOCATION_SUFFIX))
        return CANT_SEE_LOCATION_FROM_HIDING

    def describe_element(self, element_name: str):
        """Get description of a single element"""
        element_container = self.get_element_container(element_name, self.player_location)
        if element_container:
            return self.describe_container(element_container[0])
        return element_not_found(element_name)

    def describe_container(self, top_container: Element, prefix_suffix=None):
        """Descsribe any container and its contents and all the contents contents etc."""
        if prefix_suffix:
            description = top_container.name + "\n" + prefix_suffix[0] +\
                top_container.description.lower() + prefix_suffix[1]
        else:
            description = top_container.description
        visible_elements = self.get_all_elements_container(top_container, only_visible=True)
        for element_container in visible_elements:
            if element_container[1] is not self.get_player():
                if element_container[1] is not self.player_location:
                    description = description + "\n" +\
                        element_in_container(element_container[0].name,
                        element_container[1].preposition,
                        element_container[1].name)
                else:
                    if not isinstanceorsubclass(element_container[0], Player):
                        description = description + "\n" + element_container[0].description
                    if isinstanceorsubclass(element_container[0], Door):
                        description = description + " " +\
                            door_leads_to(self.get_door_directions(element_container))
        return description

    def get_door_directions(self, door_container: Tuple[Door, Element]):
        """Get the directions a door leads to"""
        directions = []
        for direction_location in door_container[1].exits.items():
            if direction_location[1] in door_container[0].connects:
                directions.append(direction_location[0])
        return directions

    def get_element_container(self, compare_element_name: str,
        container: Element, only_visible: bool = True):
        """Get an element in the container
        by its name and the corresponding container.
        If it's not found it returns None"""
        vague_matches = []
        for element_container in self.get_all_elements_container(container, only_visible):
            element = element_container[0]
            if bool(set(compare_element_name.lower().split()) & set(element.name.lower().split())):
                vague_matches.append((element, element_container[1]))
        if len(vague_matches) > 1:
            for vague_match in vague_matches:
                if vague_match[0].name.lower() == compare_element_name.lower():
                    return vague_match
        if len(vague_matches) == 1:
            return vague_matches[0]
        return None

    def get_all_elements_container(self, container: Element,\
        only_visible: bool = False, only_takeable: bool = False):
        """Recursive method to get all elements in the container
        and their corresponding container. If there is nothing it returns None"""
        elements_container = []
        if only_takeable:
            for element in container.contents:
                if isinstanceorsubclass(element, Thing) and element.visible and not element.fixed:
                    elements_container.append((element, container))
                elements_container = elements_container +\
                    self.get_all_elements_container(element, only_visible, only_takeable)
            return elements_container
        if only_visible:
            for element in container.contents:
                if element.visible:
                    elements_container.append((element, container))
                if isinstanceorsubclass(element, Chest) and not element.peekable or\
                isinstanceorsubclass(element, Chest) and not element.open:
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

    def take(self, element_name: str):
        """Take all elements or a single element and put it into the players inventory"""
        if element_name == "all":
            all_takeable = self.get_all_elements_container(self.player_location, only_takeable=True)
            response = ""
            for element_container in all_takeable:
                if not isinstanceorsubclass(element_container[0], Player) and\
                    not element_container[0].fixed:
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
        if self.save_handler.save(self.all_name_locations,
            pkg_resources.resource_filename("game.data", "save.json")):
            return SAVED_GAME_MESSAGE
        return FAILED_SAVE_MESSAGE

    def load(self, filename: str):
        """Loads the game state from file"""
        load_data = self.save_handler.load(filename)
        self.all_name_locations = load_data[0]
        self.player_location = load_data[1]
        return LOADED_SAVE_MESSAGE

    def throw(self, instructions: str):
        """Throws an item"""
        if "at" in instructions:
            thing_target = instructions.split(" at ")
            thing_container = self.get_element_container(thing_target[0], self.get_player())[0]
            if thing_container is None:
                return element_not_found(thing_container.name)
            target_container = self.get_element_container(thing_target[1], self.player_location)[0]
            if target_container is None:
                return element_not_found(target_container.name)
            if isinstanceorsubclass(target_container, Animate):
                self.get_player().contents.remove(thing_container)
                target_container.health = target_container.health - thing_container.damage * 1.5
                self.player_location.contents.append(thing_container)
                return hit_target(target_container.name)
        thing_container = self.get_element_container(instructions, self.player_location)
        self.get_player().contents.remove(thing_container[0])
        self.player_location.contents.append(thing_container[0])
        return THREW_AT_NOTHING

    def close(self, element_name: str):
        """Closes a door or chest element"""
        element_container = self.get_element_container(element_name, self.player_location)
        if isinstanceorsubclass(element_container[0], (Chest, Door)):
            element_container[0].open = False
            return CLOSED
        return NOT_OPENABLE

    def read(self, element_name: str):
        """Read an elements text"""
        element_container = self.get_element_container(element_name, self.player_location)
        if isinstanceorsubclass(element_container[0], Thing) and element_container[0].text:
            return element_container[0].text
        return NOT_READABLE

    def put(self, instructions: str):
        """Put element into the contents of another element"""
        if " in " in instructions or " on " in instructions:
            thing_target = re.split(" in | on ", instructions)
            thing_container = self.get_element_container(thing_target[0], self.get_player())
            if thing_container is None:
                return element_not_found(thing_target[0])
            target_container = self.get_element_container(thing_target[1], self.player_location)
            if target_container is None:
                return element_not_found(thing_target[1])
            thing_container[1].contents.remove(thing_container[0])
            target_container[0].contents.append(thing_container[0])
            return DONE
        return TARGET_NOT_SPECIFIED

    def activate(self, instructions: str, expected_activator_type: ActivatorType):
        """Activate an activator"""
        split_input = instructions.split()
        if "on" in instructions.split():
            split_input.remove("on")
            activator = self.get_element_container(split_input[0], self.player_location)[0]
            if not self.turn_on(activator, self.activator_handler):
                return ALREADY_ON
            return TURNED_ON
        if "off" in instructions.split():
            split_input.remove("off")
            activator = self.get_element_container(split_input[0], self.player_location)[0]
            if not self.turn_off(activator, self.activator_handler):
                return ALREADY_OFF
            return TURNED_OFF
        activator = self.get_element_container(instructions, self.player_location)[0]
        if not activator:
            return element_not_found(instructions)
        if not expected_activator_type is activator.type:
            return ACTION_NOT_POSSIBLE
        if activator.is_on is True:
            return self.turn_off(activator, self.activator_handler)
        if activator.is_on is False:
            return self.turn_on(activator, self.activator_handler)
        return ACTION_FAILED

    def turn_on(self, activator: Activator, activator_handler: ActivatorController):
        """Turns an activator on"""
        if activator.is_on:
            return ALREADY_ON
        turn_on_method = getattr(activator_handler, activator.turn_on_method_name)
        activator.is_on = True
        if turn_on_method:
            return turn_on_method()
        return NOTHING_HAPPENS

    def turn_off(self, activator: Activator, activator_handler: ActivatorController):
        """Turns an activator off"""
        if not activator.is_on:
            return ALREADY_OFF
        turn_off_method = getattr(activator_handler, activator.turn_off_method_name)
        activator.is_on = False
        if turn_off_method:
            return turn_off_method()
        return NOTHING_HAPPENS

    def move_element(self, element_name: str):
        """Moves element"""
        element_container = self.get_element_container(element_name, self.player_location)
        if not element_container:
            return element_not_found(element_name)
        element_container[0].moved = True
        revealed_element = self.get_element_container(element_container[0].reveals,
            self.player_location, only_visible=False)[0]
        revealed_element.visible = True
        return reveal_element(element_name, revealed_element.description.lower())

    def attack(self, instructions: str):
        """Attacks a target"""
        if "with" in instructions:
            target_thing = instructions.split(" with ")
            tool_container = self.get_element_container(target_thing[1], self.get_player())
            if tool_container is None:
                return element_not_in_inventory(target_thing[1])
            if not isinstanceorsubclass(tool_container[0], Tool):
                return NEEDS_TO_BE_TOOL
            target_container = self.get_element_container(target_thing[0], self.player_location)
            if target_container is None:
                return element_not_found(target_thing[0])
            if isinstanceorsubclass(target_container[0], Animate):
                target_container[0].health = target_container[0].health - tool_container[0].damage
                return hit_target(target_container[0].name)
            if isinstanceorsubclass(target_container[0], Thing):
                if not target_container[0].when_broken_do:
                    return CANT_BREAK
                break_method = getattr(self.activator_handler, target_container[0].when_broken_do)
                target_container[1].contents.remove(target_container[0])
                target_container[1].contents.append(
                    Thing("broken " + target_container[0].name,
                    target_container[0].description))
                return break_method()
        return WEAPON_NOT_SPECIFIED

    def eat(self, element_name: str):
        """Feeds the player"""
        food = self.get_element_container(element_name, self.player_location)[0]
        if not food:
            return element_not_found(food)
        self.get_player().health += food.regen
        return eat_food(food.name, food.taste)

    def tie(self, instructions: str):
        """Ties a rope to something"""
        if "to" in instructions:
            thing_target = instructions.split(" to ")
            thing_container = self.get_element_container(thing_target[0], self.get_player())
            if thing_container is None:
                return element_not_in_inventory(thing_target[0])
            target_container = self.get_element_container(thing_target[1], self.player_location)
            if target_container is None:
                return element_not_found(thing_target[1])
            if not isinstanceorsubclass(target_container[0], Thing):
                return CANT_TIE_TO_ELEMENT
            if not target_container[0].fixed:
                return THAT_WONT_HOLD
            if isinstanceorsubclass(thing_container[0], Rope):
                self.get_player().contents.remove(thing_container[0])
                target_container[1].contents.append(thing_container[0])
                thing_container[0].tied_to = target_container[0].name
                return tie_rope_to_target(target_container[0].name.lower())
        return TARGET_NOT_SPECIFIED

    def untie(self, rope_name: str):
        """Unties a rope"""
        rope = self.get_element_container(rope_name, self.player_location)
        if rope is None:
            return element_not_found(rope_name)
        if self.get_element_container(rope.tied_to, self.player_location):
            rope.tied_to = None
            return UNTIE
        return ALREADY_UNTIED

    def listen(self):
        """Listens to environment"""
        noises = []
        for element_container in self.get_all_elements_container(self.player_location):
            if element_container[0].sound:
                noises.append(element_container[0].sound)
        if len(noises) == 0:
            return SILENCE
        return noises_description(noises)

    def smell(self):
        """Smells the environment"""
        smells = []
        for element_container in self.get_all_elements_container(self.player_location):
            if element_container[0].smell:
                smells.append(element_container[0].smell)
        if len(smells) == 0:
            return NO_SMELLS
        return smell_description(smells)

    def hide(self, instructions: str):
        """Hides player in thing"""
        if "in" in instructions or "under" in instructions:
            target = re.split("in|under", instructions)[1]
            element_container = self.get_element_container(target, self.player_location)
            if isinstanceorsubclass(element_container[0], Thing) and element_container[0].enterable:
                self.get_player().hiding = True
                return entering_thing(element_container[0].name)
            return NOT_ENTERABLE
        return SPECIFIY_HIDING_PLACE

    def appear(self):
        """Puts player out of hiding"""
        player = self.get_player()
        if player.hiding is True:
            player.hiding = False
            return APPEARING
        return NOT_HIDING
