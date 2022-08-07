"""activator handler module"""



class ActivatorHandler():
    """Class containing the methods corresponding to button presses, valve turns or thing breaking"""
    def __init__(self):
        pass

    def bedroom_button_on(self):
        """Turns on bedroom test button"""
        return "The button lights up."

    def bedroom_button_off(self):
        """Turns off bedroom test button"""
        return "The button goes dark."

    def break_plate(self):
        """Reacts to the player breaking a plate"""
        return "The plate shatters into a dozen pieces."
