"""main module"""
from game.view.console_view import ConsoleView
from game.controller.dungeon_controller import DungeonMaster


def run():
    """main method that starts the program"""
    dungeon_master = DungeonMaster()
    dungeon_master.load("game/data/scenario.json")
    view = ConsoleView(dungeon_master)
    view.start_view()
