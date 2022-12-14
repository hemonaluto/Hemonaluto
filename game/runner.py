"""starts the game"""
# pylint: disable=no-name-in-module
import pkg_resources
from game.view.console_view import ConsoleView
from game.controller.dungeon_controller import DungeonController
from game.view.logger import LoggerController


def run():
    """main method that starts the program"""
    dungeon_master = DungeonController()
    scenario_filename = pkg_resources.resource_filename("game.data", "scenario.json")
    dungeon_master.load(scenario_filename)
    logger = LoggerController()
    logger.setup()
    view = ConsoleView(dungeon_master, logger)
    view.start_view()
