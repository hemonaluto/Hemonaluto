"""Container module"""


from thing import Thing


class Container(Thing):
    """Class to initialize any kind of container, e.g. a chest, with its own name and description"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.contents = []
        self.open = False
        self.locked = False
        self.key = None
        self.transparent = False
        self.enterable = False
