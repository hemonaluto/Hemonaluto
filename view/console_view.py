"""console view module"""
from constants import INPUT_INDICATOR, INTRODUCTION


class ConsoleView:
    """Class to initialize a view for the console"""

    def __init__(self, world):
        self.quit = False
        self.current_room = None
        self.world = world

    def start_view(self):
        """Start the process of displaying messages to the cosole"""
        with open("logo.txt", "r", encoding="UTF-8") as logo_file:
            print(logo_file.read())
        print(INTRODUCTION)
        while self.quit is False:
            user_input = input(INPUT_INDICATOR)
