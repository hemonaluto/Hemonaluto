"""data structure to store information about in-game elements"""
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
from dataclasses import dataclass, field


@dataclass
class Element:
    """Class to initialize any element with its own name and description"""
    def get_type(self):
        """Get the type of self"""
        return type(self).__name__
    name: str
    description: str
    visible: bool = True
    class_name: str = None#field(init=False)
    preposition: str = "in"
    sound: str = None
    smell: str = None
    contents: list = field(default_factory=list)
    """Values in list must be Element objects"""

    def __post_init__(self):
        self.class_name = self.get_type()
