"""Element module"""
# pylint: disable=unused-argument

class Element:
    """Class to initialize any element with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.visible: bool = True
        self.contents: list = []
        """Values in list must be names of Elements as strings"""
        self.class_name: str = type(self).__name__
        self.preposition: str = "in"
        self.sound: str = None
        self.smell: str = None
