"""Player module"""


from elements.animate import Animate


class Player(Animate):
    """Class to initialize the player with their own name and description"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
