"""main module"""
from view.console_view import ConsoleView
from controller.dungeon_controller import DungeonMaster


def main():
    """main method that starts the program"""
    dungeon_master = DungeonMaster()
    dungeon_master.load("game/data/scenario.json")
    view = ConsoleView(dungeon_master)
    view.start_view()

if __name__ == '__main__':
    main()
