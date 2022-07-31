"""Thing module"""
from elements.element import Element


class Thing(Element):
    """Class to initialize any kind of object, e.g. a sword, with its own name and description"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.fixed = False
        self.moved = False
        self.wearable = False
        self.concealed = False
