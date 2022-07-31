"""Element module"""


class Element:
    """Class to initialize any element with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.visible = True
        self.contents = []
        #self.class_name = __class__
