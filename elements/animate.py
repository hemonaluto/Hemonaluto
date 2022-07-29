"""Animate module"""


class Animate:
    """Class to initialize any animate being, e.g. a dwarf, with its own name and description"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []
        self.clothes = []