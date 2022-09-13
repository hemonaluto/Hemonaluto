"""responses to the players inputs, excluding descriptions of the in-game world"""
from colorama import Fore, Style

# introduction
INTRODUCTION = f"\nWelcome to {Fore.CYAN}Hemonaluto{Style.RESET_ALL}!"\
    f" A curious magical world with a dark and powerful {Fore.MAGENTA}secret{Style.RESET_ALL}."
PLEASE_TYPE = "Type any command to start exploring your new environment."

# quit message
QUIT_MESSAGE = "Okay, bye."

# indicator for the user to recognize it's their turn to type something
INPUT_INDICATOR = "\n>"

# examine command
EXAMINE_COMMAND_NAME = "examine"
EXAMINE_COMMAND_DESCRIPTION = "Examine anything in the game"
EXAMINE_COMMAND_HELP = "Type examine followed by the thing you want to examine."\
        "\nExamples:\nexamine door\nexamine location\nexamine knife"

# examine location
LOCATION_PREFIX = "You are in "
LOCATION_SUFFIX = "\nYou look around you and you see:"

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
INVALID_DIRECTION = f"{Fore.RED}You can't go there.{Style.RESET_ALL}"

# door
LOCKED_DOOR = f"{Fore.RED}There is a locked door blocking the path.{Style.RESET_ALL}"
def door_unlocked(door_name: str):
    """Returns the message for when the player unlocks a specific door."""
    return f"You have unlocked the {door_name}."
def door_not_locked(door_name: str):
    """Returns the message for when the player tries to unlock a\
    specific door that already is unlocked."""
    return f"{door_name.capitalize()} is already unlocked."
KEY_MISSING = f"{Fore.RED}You don't have the required key for that.{Style.RESET_ALL}"

# thing in container
def element_in_container(things_as_string: str, preposition: str, container: str):
    """Returns a description for a thing within a container"""
    return f"    There is a {things_as_string} {preposition} the {container}."

# element not found
def element_not_found(element_name: str):
    """Returns element not found message"""
    return f"{Fore.RED}You couldn't find the {element_name}.{Style.RESET_ALL}"

# element not in inventory
def element_not_in_inventory(element_name: str):
    """Returns element not in inventory message"""
    return f"{Fore.RED}You don't have the {element_name} in your inventory.{Style.RESET_ALL}"

# picked up element
def picked_up_element(element_name: str):
    """Returns the information that the player picked up a specific element"""
    return f"You picked up the {element_name}."

# generic location
GENERIC_LOCATAION_NAME = "location"

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
SAVED_GAME_MESSAGE = f"{Fore.GREEN}Saved the game!{Style.RESET_ALL}"

# loaded save message
LOADED_SAVE_MESSAGE = f"{Fore.GREEN}Loaded last save!{Style.RESET_ALL}"

# failed save message
FAILED_SAVE_MESSAGE = f"{Fore.RED}Failed to load last save.{Style.RESET_ALL}"

# scenario loaded message
SCENARIO_LOADED = f"{Fore.GREEN}Loaded scenario.{Style.RESET_ALL}"

# nothing response
NOTHING_RESPONSES = ["What do sea monsters eat for dinner?\n\nFish and ships.",
    "Why did the necromancer kill his depressed allies?\n\nHe wanted to raise their spirits.",
    "Why do dwarven bards sound better by candlelight?\n\nYou can shove the wax in your ears."]

# hit target response
def hit_target(target_name: str):
    """Returns hit target message"""
    return f"Your weapon hit the {target_name}."

# threw thing at nothing specific response
THREW_AT_NOTHING = "You threw it on the ground."

# closed door or chest response
CLOSED = "Closed it."

# tries to close something unopenable response
NOT_OPENABLE = f"{Fore.RED}You can't close that.{Style.RESET_ALL}"

# tries to read something unreadable response
NOT_READABLE = f"{Fore.RED}You can't read that.{Style.RESET_ALL}"

# tries to throw something unthrowable
NOT_THROWABLE = f"{Fore.RED}You can't throw that.{Style.RESET_ALL}"

# tries to turn on something that is already on
ALREADY_ON = "That's already turned on."

# tries to turn off something that is already off
ALREADY_OFF = "That's already turned off."

# tries to do an impossible action
ACTION_NOT_POSSIBLE = f"{Fore.RED}You can't do that.{Style.RESET_ALL}"

# action failed
ACTION_FAILED = f"{Fore.RED}Action failed.{Style.RESET_ALL}"

# tries activator that does nothing
NOTHING_HAPPENS = "Nothing happens."

# reveal element
def reveal_element(moved_item: str, revealed_item: str):
    """Revealing element message"""
    return f"You move the {moved_item} and reveal {revealed_item.lower()}"

# attacks without specifying weapon
WEAPON_NOT_SPECIFIED = f"{Fore.RED}You didn't specify a weapon.{Style.RESET_ALL}"

# eating food message
def eat_food(food_name: str, taste: str):
    """Eating food message"""
    return f"You eat the {food_name}. It tastes {taste}."

# shouting response
SHOUT_RESPONSE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

# tied element to target
def tie_rope_to_target(target: str):
    """Tying rope to something message"""
    return f"You tie the rope to the {target}."

# tries to tie something that isn't a rope
NOT_A_ROPE = f"{Fore.RED}That's not a rope.{Style.RESET_ALL}"

# that won't hold
THAT_WONT_HOLD = f"{Fore.RED}That won't hold your weight.{Style.RESET_ALL}"

# target not specified
TARGET_NOT_SPECIFIED = f"{Fore.RED}Target not specified.{Style.RESET_ALL}"

# untie
UNTIE = "You untie it."

# climbing down text
CLIMBING_DOWN = "You climb down the rope.\n"

# tries to go down when there is no tied rope in the room
NO_TIED_ROPE = "There is a steep way down but you'll need something to lower yourself."

# tries to tie rope to something you can't tie ropes to
CANT_TIE_TO_ELEMENT = f"{Fore.RED}You can't tie the rope to that.{Style.RESET_ALL}"

# tries to untie an already untied rope
ALREADY_UNTIED = "No need for that, it's already untied."

# tries to break a thing that has no break method
CANT_BREAK = "Breaking that would be pointless."

# tries to attack something without a valid tool
NEEDS_TO_BE_TOOL = "Try using a tool or weapon instead."

# door leads to message
def door_leads_to(directions: str):
    """describes where a door leads to"""
    description = ""
    for direction in directions:
        description += f"\n    The door leads to the {direction}."
    return description

# hears nothing message
SILENCE = "You hear nothing specific."

# smells nothing message
NO_SMELLS = "You smell nothing specific."

# noises description
def noises_description(noises: str):
    """Describes noises"""
    description = "You hear:"
    for noise in noises:
        description += f"\n    {noise}"
    return description

# smell description
def smell_description(smells: str):
    """Describes smells"""
    description = "You smell:"
    for smell in smells:
        description += f"\n    {smell}"
    return description

# hiding
def entering_thing(thing: str):
    """Entering thing message"""
    return f"Hiding in {thing}"
NOT_ENTERABLE = "You can't enter that."
SPECIFIY_HIDING_PLACE = "Hidingplace not specified."
CANT_SEE_LOCATION_FROM_HIDING = "You can't see anything from your hididng spot."
APPEARING = "You leave your hiding place."
NOT_HIDING = "You're not hiding in the first place."

# done generic action
DONE = "Done."

# take errors
ELEMENT_IS_FIXED = f"{Fore.RED}That element is attached to something and"\
    "can't be picked up.{Style.RESET_ALL}"
CANT_PICK_UP_SELF = "You can't take yourself."

# clear log response
CLEAR = "Cleared log."
