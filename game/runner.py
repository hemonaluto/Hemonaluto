"""main module"""
from game.view.console_view import ConsoleView
from game.controller.dungeon_controller import DungeonMaster
import pkg_resources


def run():
    """main method that starts the program"""
    dungeon_master = DungeonMaster()
    scenario_filename = pkg_resources.resource_filename("game.data", "scenario.json")
    dungeon_master.load(scenario_filename)
    view = ConsoleView(dungeon_master)
    view.start_view()
