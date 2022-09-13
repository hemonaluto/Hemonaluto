"""console view that prints out what the player sees"""
# pylint: disable=too-many-locals
from functools import partial
import random
import pkg_resources
import colorama
from colorama import Fore, Style
from game.model.enums.activator_type import ActivatorType
from game.data.scenario_texts import BEDROOM_NAME
from game.data.texts import ACTION_NOT_POSSIBLE, DOWN, EAST, GREETINGS,\
    INPUT_INDICATOR, INTRODUCTION, JUMP_RESPONSE,\
    NORTH, NORTHEAST, NORTHWEST, NOTHING_RESPONSES, PLEASE_TYPE,\
    QUIT_MESSAGE, SHOUT_RESPONSE, SOUTH, SOUTHEAST,\
    SOUTHWEST, SWEAR_RESPONSE, UP, WEST


class ConsoleView:
    """Class to initialize a view for the console"""

    def __init__(self, dungeon_master, logger):
        self.quit = False
        self.dungeon_master = dungeon_master
        self.logger = logger

    def toggle_quit(self):
        """Quits the game"""
        self.quit = True
        return QUIT_MESSAGE

    def parse(self, user_input: str):
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
        close = self.dungeon_master.close
        read = self.dungeon_master.read
        put = self.dungeon_master.put
        activate = self.dungeon_master.activate
        move_element = self.dungeon_master.move_element
        attack = self.dungeon_master.attack
        eat = self.dungeon_master.eat
        tie = self.dungeon_master.tie
        untie = self.dungeon_master.untie
        listen = self.dungeon_master.listen
        smell = self.dungeon_master.smell
        hide = self.dungeon_master.hide
        appear = self.dungeon_master.appear
        log = self.logger.get_log
        clear = self.logger.clear
        move_dictionary = {
            "examine": partial(describe, rest_input_joined),
            "look": partial(describe, rest_input_joined),
            "l": partial(describe, rest_input_joined),
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
            "load": partial(load, pkg_resources.resource_filename("game.data", "save.json")),
            "restore": partial(load, pkg_resources.resource_filename("game.data", "save.json")),
            "restart": partial(load, pkg_resources.resource_filename("game.data", "scenario.json")),
            "score": score,
            "diagnostic": health,
            "health": health,
            "": partial(random.choice, NOTHING_RESPONSES),
            "hemonaluto": INTRODUCTION,
            "throw": partial(throw, rest_input_joined),
            "close": partial(close, rest_input_joined),
            "read": partial(read, rest_input_joined),
            "drop": partial(throw, rest_input_joined),
            "put": partial(put, rest_input_joined),
            "press": partial(activate, rest_input_joined, ActivatorType.PRESS),
            "turn": partial(activate, rest_input_joined, ActivatorType.TURN),
            "push": partial(move_element, rest_input_joined),
            "pull": partial(move_element, rest_input_joined),
            "move": partial(move_element, rest_input_joined),
            "attack": partial(attack, rest_input_joined),
            "kill": partial(attack, rest_input_joined),
            "eat": partial(eat, rest_input_joined),
            "drink": partial(eat, rest_input_joined),
            "shout": SHOUT_RESPONSE,
            "tie": partial(tie, rest_input_joined),
            "attach": partial(tie, rest_input_joined),
            "untie": partial(untie, rest_input_joined),
            "destroy": partial(attack, rest_input_joined),
            "break": partial(attack, rest_input_joined),
            "cut": partial(attack, rest_input_joined),
            "listen": listen,
            "smell": smell,
            "hide": partial(hide, rest_input_joined),
            "leave": appear,
            "appear": appear,
            "log": log,
            "clear": clear
        }
        response = None
        move_action = move_dictionary.get(split_user_input[0], None)
        general_action = general_dictionary.get(split_user_input[0], None)
        if move_action:
            if isinstance(move_action, str):
                response = move_action
            else:
                response = move_action()
        elif general_action:
            if isinstance(general_action, str):
                response = general_action
            else:
                response = general_action()
        if response:
            if not user_input in {"clear", "log"}:
                self.logger.log(user_input, response)
            return response
        return ACTION_NOT_POSSIBLE

    def start_view(self):
        """Start the process of displaying messages to the cosole"""
        colorama.init(autoreset=True)
        with open(pkg_resources.resource_filename("game.data", "logo.txt"),
            "r", encoding="UTF-8") as logo_file:
            print(Fore.BLUE + logo_file.read() + Style.RESET_ALL)
        print(INTRODUCTION + "\n")
        print(self.dungeon_master.brief(BEDROOM_NAME))
        print(PLEASE_TYPE)
        while self.quit is False:
            user_input = input(INPUT_INDICATOR)
            print(self.parse(user_input))
            