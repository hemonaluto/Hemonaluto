"""Door module"""


class Door():
    """Class to initialize any kind of door, e.g. a trapdoor, with its own name and description"""
    def __init__(self, name, description, key=None):
        self.name = name
        self.description = description
        self.open = False
        self.lockable = key is not None
        self.locked = True if key else False
        self.key = key
        self.connects = []
