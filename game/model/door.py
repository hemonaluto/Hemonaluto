"""data structure to store information about in-game doors"""
# pylint: disable=too-few-public-methods
from game.model.element import Element


class Door(Element):
    """Class to initialize any kind of door, e.g. a trapdoor, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.open: bool = kwargs.get("open", False)
        self.key: str = kwargs.get("key", None)
        self.lockable: bool = kwargs.get("lockable", self.key is not None)
        self.locked: bool = kwargs.get("locked", bool(self.key))
        """Value must be the name of the key as a string"""
        self.connects: list = kwargs.get("connects", [])
        """Values in list must be names of locations as strings"""
        super().__init__(name, description, **kwargs)
