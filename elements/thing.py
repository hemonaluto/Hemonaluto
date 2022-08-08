"""Thing module"""
from elements.element import Element


class Thing(Element):
    """Class to initialize any kind of object, e.g. a bottle, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)
        self.name: str = name
        self.description: str = description
        self.fixed: bool = False
        self.moved: bool = False
        self.wearable: bool = False
        self.text: str = None
        self.reveals: str = None
        self.when_broken_do: str = None
        """Value must be a method name existing in activator_handler"""
        self.enterable: bool = False
