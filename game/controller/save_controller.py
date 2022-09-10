"""storing and loading game save files"""
# pylint: disable=eval-used
# pylint: disable=unused-import
import json
from typing import Dict, List, Tuple
from game.helper_methods import isinstanceorsubclass
from game.model.location import Location
from game.model.player import Player
from game.model.rope import Rope
from game.model.thing import Thing
from game.model.tool import Tool
from game.model.activator import Activator
from game.model.animate import Animate
from game.model.chest import Chest
from game.model.door import Door
from game.model.food import Food
from game.model.element import Element


class SaveController:
    """Class to save and load the game state"""

    class ElementEncoder(json.JSONEncoder):
        """json encoder for elements"""
        def default(self, o):
            return o.__dict__

    def save(self, all_name_locations: List[Tuple[str, Location]], filename):
        """Saves the game"""
        locations = []
        for location in all_name_locations:
            locations.append(location[1])
        with open(filename, "w", encoding="UTF-8") as savefile:
            json.dump(locations, savefile, indent=4, cls=self.ElementEncoder)
        return True

    def load(self, filename: str):
        """Loads the save file"""
        all_name_locations = []
        player_location = None
        with open(filename, "r", encoding="UTF-8") as savefile:
            location_dictionaries = json.load(savefile)
            for location_dictionary in location_dictionaries:
                contents_dictionary = location_dictionary["contents"]
                location = Location(**location_dictionary)
                location.contents = self.dictionary_to_elements(contents_dictionary)
                all_name_locations.append((location.name, location))
                for element in location.contents:
                    if isinstanceorsubclass(element, Player):
                        player_location = location
            return (all_name_locations, player_location)

    def dictionary_to_elements(self, contents_dictionary_list: Dict):
        """Converts dictionary to elements"""
        converted_contents = []
        for element_dictionary in contents_dictionary_list:
            class_name = element_dictionary["class_name"]
            element = eval(class_name)(**element_dictionary)
            if len(element_dictionary["contents"]) > 0:
                element.contents = self.dictionary_to_elements(element_dictionary["contents"])
            converted_contents.append(element)
        return converted_contents
