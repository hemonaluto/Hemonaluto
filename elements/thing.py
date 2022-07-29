"""Thing module"""


class Thing:
    """Class to initialize any kind of object, e.g. a sword, with its own name and description"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.fixed = False
        self.moved = False
        self.wearable = False
        self.concealed = False
