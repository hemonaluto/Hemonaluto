"""Animate module"""
from elements.element import Element


class Animate(Element):
    """Class to initialize any animate being, e.g. a dwarf, with its own name and description"""
    def __init__(self, name, description, health, **kwargs):
        Element.__init__(self, name, description, **kwargs)
        self.name = name
        self.description = description
        self.clothes = []
        self.health = health
