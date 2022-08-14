"""data structure to store information about in-game things"""
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
from game.model.element import Element


class Thing(Element):
    """Class to initialize any kind of object, e.g. a bottle, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.fixed: bool = kwargs.get("fixed", False)
        self.moved: bool = kwargs.get("moved", False)
        self.wearable: bool = kwargs.get("wearable", False)
        self.text: str = kwargs.get("text", None)
        self.reveals: str = kwargs.get("reveals", None)
        self.when_broken_do: str = kwargs.get("when_broken_do", None)
        """Value must be a method name existing in activator_handler"""
        self.enterable: bool = kwargs.get("enterable", False)
        super().__init__(name, description, **kwargs)
