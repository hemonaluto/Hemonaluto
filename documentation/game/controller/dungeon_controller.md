Module game.controller.dungeon_controller
=========================================
kind of like a dungeon master that controls everything that's happening in the in-game world

Classes
-------

`DungeonController()`
:   dungeon controller (dungeon master) class

    ### Methods

    `activate(self, instructions: str, expected_activator_type: game.model.enums.activator_type.ActivatorType)`
    :   Activate an activator

    `appear(self)`
    :   Puts player out of hiding

    `attack(self, instructions: str)`
    :   Attacks a target

    `brief(self, room_name: str)`
    :   Debrief the player if they arrive at a location they've never been

    `close(self, element_name: str)`
    :   Closes a door or chest element

    `describe(self, element_name: str)`
    :   Returns a desription of any kind of in-game element at the location of the player

    `describe_container(self, top_container: game.model.element.Element, prefix_suffix=None)`
    :   Descsribe any container and its contents and all the contents contents etc.

    `describe_element(self, element_name: str)`
    :   Get description of a single element

    `describe_location(self)`
    :   Describes the location where the player is

    `eat(self, element_name: str)`
    :   Feeds the player

    `get_all_elements_container(self, container: game.model.element.Element, only_visible: bool = False, only_takeable: bool = False)`
    :   Recursive method to get all elements in the container
        and their corresponding container. If there is nothing it returns None

    `get_door_directions(self, door_container: Tuple[game.model.door.Door, game.model.element.Element])`
    :   Get the directions a door leads to

    `get_element_container(self, compare_element_name: str, container: game.model.element.Element, only_visible: bool = True)`
    :   Get an element in the container
        by its name and the corresponding container.
        If it's not found it returns None

    `get_health(self)`
    :   Get the current health

    `get_player(self)`
    :   Get the player object from the current location

    `get_player_inventory(self)`
    :   Returns the invenotry of the player as a string listing all things

    `get_score(self)`
    :   Get the current score

    `hide(self, instructions: str)`
    :   Hides player in thing

    `listen(self)`
    :   Listens to environment

    `load(self, filename: str)`
    :   Loads the game state from file

    `move_element(self, element_name: str)`
    :   Moves element

    `move_player(self, direction: str)`
    :   Move the player from one location to the next, which lies in the given direction

    `put(self, instructions: str)`
    :   Put element into the contents of another element

    `read(self, element_name: str)`
    :   Read an elements text

    `save(self)`
    :   Saves the game state to file

    `set_player_location(self, player: game.model.player.Player, location: game.model.location.Location)`
    :   Update the players location to a new one

    `smell(self)`
    :   Smells the environment

    `take(self, element_name: str)`
    :   Take all elements or a single element and put it into the players inventory

    `throw(self, instructions: str)`
    :   Throws an item

    `tie(self, instructions: str)`
    :   Ties a rope to something

    `turn_off(self, activator: game.model.activator.Activator, activator_handler: game.controller.activator_controller.ActivatorController)`
    :   Turns an activator off

    `turn_on(self, activator: game.model.activator.Activator, activator_handler: game.controller.activator_controller.ActivatorController)`
    :   Turns an activator on

    `unlock(self, door_name: str)`
    :   Unlocks and opens a door

    `untie(self, rope_name: str)`
    :   Unties a rope