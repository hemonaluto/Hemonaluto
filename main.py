"""main module"""


from console_view import ConsoleView
from dungeon_master import DungeonMaster


def main ():
    """main method that starts the program"""
    dungeon_master = DungeonMaster()
    dungeon_master.generate_world()
    view = ConsoleView(dungeon_master)
    view.start_view()

if __name__ == '__main__':
    main()
