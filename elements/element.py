"""Element module"""


class Element:
    """Class to initialize any element with its own name and description"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
