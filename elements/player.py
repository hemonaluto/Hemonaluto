"""Player module"""


from elements.animate import Animate
from elements.element import Element


class Player(Animate, Element):
    """Class to initialize the player with their own name and description"""
    def __init__(self, name, description):
        Animate.__init__(self, name, description)
        Element.__init__(self, name, description)
        self.name = name
        self.description = description
