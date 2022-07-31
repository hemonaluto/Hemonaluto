"""texts module"""
# introduction
INTRODUCTION = "\nWelcome to Hemonaluto! A curious magical world with a dark and powerful secret."\
        "\n\nType any command to start exploring your new environment."

# quit message
QUIT_MESSAGE = "It will miss you."

# indicator for the user to recognize it's their turn to type something
INPUT_INDICATOR = "\n>"

# examine command
EXAMINE_COMMAND_NAME = "examine"
EXAMINE_COMMAND_DESCRIPTION = "Examine anything in the game"
EXAMINE_COMMAND_HELP = "Type examine followed by the thing you want to examine."\
        "\nExamples:\nexamine door\nexamine location\nexamine knife"

# directions
NORTH = "north"
EAST = "east"
SOUTH = "south"
WEST = "west"
NORTHEAST = "northeast"
NORTHWEST = "northwest"
SOUTHEAST = "southeast"
SOUTHWEST = "southwest"
UP = "up"
DOWN = "down"
INVALID_DIRECTION = "You can't go there."

# door
LOCKED_DOOR = "There is a locked door blocking the path."
def door_unlocked(door_name):
    """Returns the message for when the player unlocks a specific door."""
    return f"You have unlocked the {door_name}."
def door_not_locked(door_name):
    """Returns the message for when the player tries to unlock a\
    specific door that already is unlocked."""
    return f"{door_name.capitalize()} is already unlocked."
KEY_MISSING = "You don't have the required key for that."

# player
PLAYER_NAME = "Player"
PLAYER_DESCRIPTION = "A slim person with fiery blue eyes and pitch-black hair."

# examine location
LOCATION_PREFIX = "You are in "
LOCATION_SUFFIX = " You look around you and you see:"

# bed
BED_NAME = "bed"
BED_DESCRIPTION = "A comfy wooden red bed."

# bedroom door
BEDROOM_DOOR_NAME = "door"
BEDROOM_DOOR_DESCRIPTION = "A mundane wooden door."

# bedroom key
BEDROOM_KEY_NAME = "crude key"
BEDROOM_KEY_DESCRIPTION = "A key with a cursive letter B inscribed on it."

# bedroom hook
BEDROOM_HOOK_NAME = "hook"
BEDROOM_HOOK_DESCRIPTION = "A blunt wooden hook attached to the wall."

# thing in container
def thing_in_container(things_as_string, container):
    """Returns a description for a thing within a container"""
    return f"There is a {things_as_string} in the {container}."

# element not found
ELEMENT_NOT_FOUND = "You couldn't find such a thing"

# picked up element
def picked_up_element(element_name):
    """Returns the information that the player picked up a specific element"""
    return f"You picked up the {element_name}"

# generic location
GENERIC_LOCATAION_NAME = "location"

# bedroom
BEDROOM_NAME = "Bedroom"
BEDROOM_DESCRIPTION = "A room designed for humans to rest."

# dining room
DINING_ROOM_NAME = "Dining Room"
DINING_ROOM_DESCRIPTION = "A room designed for humans to eat."
