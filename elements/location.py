"""Location module"""


class Location:
    """Class to initialize any kind of place, e.g. a room, with its own name and description"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.visited = False
        self.exits = {}
        self.contents = []
