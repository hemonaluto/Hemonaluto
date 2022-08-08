"""Door module"""
from elements.element import Element


class Door(Element):
    """Class to initialize any kind of door, e.g. a trapdoor, with its own name and description"""
    def __init__(self, name, description, key=None, **kwargs):
        super().__init__(name, description, **kwargs)
        self.name: str = name
        self.description: str = description
        self.open: bool = False
        self.lockable: bool = key is not None
        self.locked: bool = True if key else False
        self.key: str = key
        """Value must be the name of the key as a string"""
        self.connects: list = []
        """Values in list must be names of locations as strings"""
