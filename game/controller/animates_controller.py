"""controls all animate behavior"""
from random import choice


class AnimatesController:
    """Contains methods that dictate how animates talk and move"""

    def move_jester(self, doors):
        """Moves the jester to the next location or stays put depending on random outcome"""
        willmove = choice([True, False])
        if not willmove:
            return
        return choice(doors)
