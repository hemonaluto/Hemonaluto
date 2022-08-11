"""Player module"""
from elements.animate import Animate
from elements.element import Element


class Player(Animate, Element):
    """Class to initialize the player with their own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.visible: bool = kwargs.get("visible", True)
        self.hiding: bool = kwargs.get("hiding", False)
        Animate.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
