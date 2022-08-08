"""Animate module"""
from elements.element import Element


class Animate(Element):
    """Class to initialize any animate being, e.g. a dwarf, with its own name and description"""
    def __init__(self, name, description, health, **kwargs):
        Element.__init__(self, name, description, **kwargs)
        self.name: str = name
        self.description: str = description
        self.clothes: list = []
        """Values in list must be names of clothes as strings"""
        self.health: int = health
