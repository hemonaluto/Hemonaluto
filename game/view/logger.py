"""takes care of all logging processes"""
from pathlib import Path
import pkg_resources
from game.data.texts import CLEAR


class LoggerController:
    """Class that controls the logging of the output"""


    def setup(self):
        """Set up the logger"""
        Path(pkg_resources.resource_filename("game.data", "log.txt")).touch(exist_ok=True)

    def clear(self):
        """Clear the log file"""
        with open(pkg_resources.resource_filename("game.data", "log.txt"),
            'w+', encoding="UTF-8"):
            return CLEAR

    def log(self, user_input, text):
        """Log text to file"""
        with open(pkg_resources.resource_filename("game.data", "log.txt"),
            'a', encoding="UTF-8") as logfile:
            logfile.write(user_input + ": " + text + "\n")

    def get_log(self):
        """Get the log of the current session"""
        with open(pkg_resources.resource_filename("game.data", "log.txt"),
            'r', encoding="UTF-8") as logfile:
            return logfile.read()
