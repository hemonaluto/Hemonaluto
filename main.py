"""main module"""


from view.console_view import ConsoleView
from world import World


def main ():
    """main method that starts the program"""
    world = World()
    world.generate_world()
    view = ConsoleView(world)
    view.start_view()

if __name__ == '__main__':
    main()
