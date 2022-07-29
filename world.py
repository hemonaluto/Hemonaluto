"""world module"""


from elements.location import Location
from elements.player import Player
from elements.thing import Thing
from constants import WEST


class World:
    """world class"""
    def __init__(self):
        pass

    def generate_world(self):
        """Generates the game world"""
        player = Player("Player", "A slim human with fiery blue eyes and pitch-black hair.")
        bed = Thing("Bed", "A comfy wooden red bed.")
        bedroom = Location("Bedroom", "A room designed for human-like beings to rest.")
        dining_room = Location("Dining Room", "A room designed for human-linke beings to eat.")
        bedroom.exits[WEST] = dining_room
        bedroom.contents.append(player)
        bedroom.contents.append(bed)
