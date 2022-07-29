"""main module"""


from world import World


def main ():
    """main method that starts the program"""
    world = World()
    world.generate_world()

if __name__ == '__main__':
    main()
