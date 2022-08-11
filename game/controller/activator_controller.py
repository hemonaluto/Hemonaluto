"""activator handler module"""
from data.scenario_texts import BUTTON_GOES_DARK, BUTTON_LIGHTS_UP, PLATE_BREAKS


class ActivatorHandler():
    """Class containing the methods corresponding to button presses,
    valve turns or thing breaking"""
    def __init__(self):
        pass

    def bedroom_button_on(self):
        """Turns on bedroom test button"""
        return BUTTON_LIGHTS_UP

    def bedroom_button_off(self):
        """Turns off bedroom test button"""
        return BUTTON_GOES_DARK

    def break_plate(self):
        """Reacts to the player breaking a plate"""
        return PLATE_BREAKS
