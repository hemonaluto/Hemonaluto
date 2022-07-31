"""Container module"""


from elements.element import Element
from elements.thing import Thing


class Container(Thing, Element):
    """Class to initialize any kind of container, e.g. a chest, with its own name and description"""
    def __init__(self, name, description):
        Thing.__init__(self, name, description)
        Element.__init__(self, name, description)
        self.contents = []
        self.open = False
        self.locked = False
        self.key = None
        self.peekable = False
        self.enterable = False
