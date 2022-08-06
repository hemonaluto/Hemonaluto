"""texts module"""
# introduction
INTRODUCTION = "\nWelcome to Hemonaluto! A curious magical world with a dark and powerful secret."\
        "\n\nType any command to start exploring your new environment."

# quit message
QUIT_MESSAGE = "They will miss you."

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

# bedroom rug
BEDROOM_RUG_NAME = "rug"
BEDROOM_RUG_DESCRIPTION = "A large soft red rug."

# thing in container
def element_in_container(things_as_string, container):
    """Returns a description for a thing within a container"""
    return f"There is a {things_as_string} in the {container}."

# element not found
def element_not_found(element_name):
    """Returns element not found message"""
    return f"You couldn't find such {element_name}"

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

# greetings
GREETINGS = ["Hi.", "Hello.", "Greetings"]

# swear response
SWEAR_RESPONSE = "No. More. Saying. Cuss words! It. Is. Not. Good. I\'m putting a video on YouTube \
about no more saying cuss words. No more saying cuss words guys! It's inappropriate and violent! \
If you say a cuss word then you're like, going to jail, and you're like, and when you go to jail, \
i- ba- when you go to jail, if you say, if you say a cuss word you go to jail and if you go to \
jail cause you said a cuss word, then... You're only gonna eat BROCCOLI and OTHER VEGETABLES \
for your WHOLE LIFE. You don't want to eat vegetables. Sometimes people like eating sweets but, \
I eat broccoli. So, I'm okay with broccoli but I do not want to go to jail. You can not go to jail. \
And saying cuss words is ILLEGAL. They are now gonna make a law about that. It is illegal, it is \
inappropriate, it is really violent. I better warn my school about that."

# jump response
JUMP_RESPONSE = "You jump up and down."

# saved game message
SAVED_GAME_MESSAGE = "Saved the game!"

# loaded save message
LOADED_SAVE_MESSAGE = "Loaded last save!"

# failed save message
FAILED_SAVE_MESSAGE = "Failed to load last save."

# scenario loaded message
SCENARIO_LOADED = "Loaded scenario."

# nothing response
NOTHING_RESPONSES = ["What do sea monsters eat for dinner?\n\nFish and ships.",\
"Why did the necromancer kill his depressed allies?\n\nHe wanted to raise their spirits.",\
"Why do dwarven bards sound better by candlelight?\n\nYou can shove the wax in your ears."]

# hit target response
def hit_target(target_name):
    """Returns hit target message"""
    return f"Your projectile hit {target_name}."

# threw thing at nothing specific response
THREW_AT_NOTHING = "You threw it on the ground."

# closed door or chest response
CLOSED = "Closed it."

# tries to close something unopenable response
NOT_OPENABLE = "You can't close that."

# tries to read something unreadable response
NOT_READABLE = "You can't read that."

# tries to throw something unthrowable
NOT_THROWABLE = "You can't throw that."
