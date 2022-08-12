"""main module"""
from game.view.console_view import ConsoleView
from game.controller.dungeon_controller import DungeonController
import pkg_resources


def run():
    """main method that starts the program"""
    dungeon_master = DungeonController()
    scenario_filename = pkg_resources.resource_filename("game.data", "scenario.json")
    dungeon_master.load(scenario_filename)
    view = ConsoleView(dungeon_master)
    view.start_view()
