"""data structure to store information about in-game elements"""


class Element:
    """Class to initialize any element with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.visible: bool = kwargs.get("visible", True)
        self.class_name: str = kwargs.get("class_name", type(self).__name__)
        self.preposition: str = kwargs.get("preposition", "in")
        self.sound: str = kwargs.get("sound", None)
        self.smell: str = kwargs.get("smell", None)
        self.contents: list = kwargs.get("contents", [])
        """Values in list must be Element objects"""
