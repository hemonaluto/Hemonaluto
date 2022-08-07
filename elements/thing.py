"""Thing module"""
from elements.element import Element


class Thing(Element):
    """Class to initialize any kind of object, e.g. a bottle, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)
        self.name = name
        self.description = description
        self.fixed = False
        self.moved = False
        self.wearable = False
        self.text = None
        self.reveals = None
        self.when_broken_do = None
