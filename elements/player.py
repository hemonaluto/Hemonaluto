"""Player module"""
from elements.animate import Animate
from elements.element import Element


class Player(Animate, Element):
    """Class to initialize the player with their own name and description"""
    def __init__(self, name, description, health, **kwargs):
        Animate.__init__(self, name, description, health, **kwargs)
        Element.__init__(self, name, description, **kwargs)
        self.name: str = name
        self.description: str = description
        self.visible: bool = True
        self.hiding: bool = False
