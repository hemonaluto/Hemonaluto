"""console view module"""
from functools import partial
from constants import INPUT_INDICATOR, INTRODUCTION, QUIT_MESSAGE


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
        split_user_input = user_input.split()
        if len(split_user_input) < 2:
            split_user_input.append("")
        return {
            "quit":  self.toggle_quit,
            "examine":  partial(self.dungeon_master.describe, split_user_input[1])
        }.get(split_user_input[0])()

    def start_view(self):
        """Start the process of displaying messages to the cosole"""
        with open("logo.txt", "r", encoding="UTF-8") as logo_file:
            print(logo_file.read())
        print(INTRODUCTION)
        while self.quit is False:
            user_input = input(INPUT_INDICATOR)
            print(self.string_to_method(user_input))
            