"""Animate module"""
from elements.element import Element


class Animate(Element):
    """Class to initialize any animate being, e.g. a dwarf, with its own name and description"""
    def __init__(self, name, description):
        Element.__init__(self, name, description)
        self.name = name
        self.description = description
        self.clothes = []
