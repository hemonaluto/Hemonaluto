"""console view module"""
from functools import partial
import random
from texts import DOWN, EAST, GREETINGS, INPUT_INDICATOR, INTRODUCTION, JUMP_RESPONSE, NORTH, NORTHEAST, NORTHWEST, NOTHING_RESPONSES,\
QUIT_MESSAGE, SOUTH, SOUTHEAST, SOUTHWEST, SWEAR_RESPONSE, UP, WEST


class ConsoleView:
    """Class to initialize a view for the console"""

    def __init__(self, dungeon_master):
        self.quit = False
        self.current_room = None
        self.dungeon_master = dungeon_master

    def toggle_quit(self):
        """Quits the game"""
        self.quit = True
        return QUIT_MESSAGE

    def string_to_method(self, user_input):
        """Runtime polymorphic method to map the possible user input to a corresponding method"""
        split_user_input = user_input.lower().split()
        if len(split_user_input) < 2:
            split_user_input.append("")
        rest_input_joined = " ".join(split_user_input[1:])
        describe = self.dungeon_master.describe
        move = self.dungeon_master.move_player
        unlock = self.dungeon_master.unlock
        take = self.dungeon_master.take
        inventory = self.dungeon_master.get_player_inventory
        save = self.dungeon_master.save
        load = self.dungeon_master.load
        score = self.dungeon_master.get_score
        health = self.dungeon_master.get_health
        throw = self.dungeon_master.throw
        move_dictionary = {
            "examine": partial(describe, rest_input_joined),
            "look": partial(describe, rest_input_joined),
            "l": partial(describe, rest_input_joined),
            "brief": partial(describe, rest_input_joined),
            "north": partial(move, NORTH),
            "n": partial(move, NORTH),
            "east": partial(move, EAST),
            "e": partial(move, EAST),
            "south": partial(move, SOUTH),
            "s": partial(move, SOUTH),
            "west": partial(move, WEST),
            "w": partial(move, WEST),
            "northeast": partial(move, NORTHEAST),
            "ne": partial(move, NORTHEAST),
            "northwest": partial(move, NORTHWEST),
            "nw": partial(move, NORTHWEST),
            "southeast": partial(move, SOUTHEAST),
            "se": partial(move, SOUTHEAST),
            "southwest": partial(move, SOUTHWEST),
            "sw": partial(move, SOUTHWEST),
            "up": partial(move, UP),
            "u": partial(move, UP),
            "climb": partial(move, UP),
            "down": partial(move, DOWN),
            "d": partial(move, DOWN),
        }
        general_dictionary = {
            "quit": self.toggle_quit,
            "q": self.toggle_quit,
            "exit": self.toggle_quit,
            "go": move_dictionary.get(rest_input_joined, None),
            "open": partial(unlock, rest_input_joined),
            "unlock": partial(unlock, rest_input_joined),
            "get": partial(take, rest_input_joined),
            "take": partial(take, rest_input_joined),
            "pick": partial(take, " ".join(split_user_input[2:])),
            "inventory": inventory,
            "i": inventory,
            "hi": partial(random.choice, GREETINGS),
            "hello": partial(random.choice, GREETINGS),
            "shit": SWEAR_RESPONSE,
            "damn": SWEAR_RESPONSE,
            "fuck": SWEAR_RESPONSE,
            "jump": JUMP_RESPONSE,
            "save": save,
            "load": partial(load, "save.json"),
            "restore": load,
            "restart": partial(load, "scenario.json"),
            "score": score,
            "diagnostic": health,
            "health": health,
            "": partial(random.choice, NOTHING_RESPONSES),
            "hemonaluto": INTRODUCTION,
            "throw": partial(throw, rest_input_joined)
        }
        """
        ToDo:
        "throw": throw,
        "open": closent,
        "close": close,
        "read": decipher,
        "drop": drop,
        "put": put,
        "turn": turn,
        "turn on": turn_on,
        "turn off": turn_off,
        "move": move_element,
        "attack": attack,
        "kill": attack,
        "eat": eat,
        "shout": shout,
        "tie": tie,
        "break": destroy,
        "pray": pray,
        "drink": drink,
        "smell": smell,
        "cut": cut,
        "listen": listen,
        """
        move_action = move_dictionary.get(split_user_input[0], None)
        if move_action is not None:
            return move_action()
        general_action = general_dictionary.get(split_user_input[0], None)
        if general_action is not None:
            return general_action()

    def start_view(self):
        """Start the process of displaying messages to the cosole"""
        with open("logo.txt", "r", encoding="UTF-8") as logo_file:
            print(logo_file.read())
        print(INTRODUCTION)
        while self.quit is False:
            user_input = input(INPUT_INDICATOR)
            print(self.string_to_method(user_input))
            