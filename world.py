"""world module"""


from elements.location import Location
from constants import WEST


class World:
    """world class"""
    def __init__(self):
        pass

    def generate_world(self):
        """Generates the game world"""
        bedroom = Location("Bedroom", "A room designed for human-like beings to rest.")
        dining_room = Location("Dining Room", "A room designed for human-linke beings to eat.")
        bedroom.exits[WEST] = dining_room
