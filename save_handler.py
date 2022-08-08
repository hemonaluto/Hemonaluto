"""save handler module"""
import json
from elements.activator import Activator
from elements.animate import Animate
from elements.chest import Chest
from elements.door import Door
from elements.element import Element
from elements.food import Food
from elements.location import Location
from elements.player import Player
from elements.rope import Rope
from elements.thing import Thing
from elements.tool import Tool

class SaveHandler():
    """Class to save and load the game state"""
   
    class ElementEncoder(json.JSONEncoder):
        """json encoder for elements"""
        def default(self, o):
            return o.__dict__

    def save(self, all_name_locations, filename):
        """Saves the game"""
        locations = []
        for location in all_name_locations:
            locations.append(location[1])
        with open(filename, "w", encoding="UTF-8") as savefile:
            json.dump(locations, savefile, indent=4, cls=self.ElementEncoder)
        return True

    def load(self, filename):
        """Loads the save file"""
        all_name_locations = []
        player_location = None
        with open(filename, "r", encoding="UTF-8") as savefile:
            location_dictionaries = json.load(savefile)
            for location_dictionary in location_dictionaries:
                contents_dictionary = location_dictionary["contents"]
                location = Location(**location_dictionary)
                # ToDo: Find out why it doesn't do this automatically:
                location.exits = location_dictionary["exits"]
                location.needs_rope = location_dictionary["needs_rope"]
                location.contents = self.dictionary_to_elements(contents_dictionary)
                all_name_locations.append((location.name, location))
                for element in location.contents:
                    if isinstance(element, Player):
                        player_location = location
            return (all_name_locations, player_location)

    def dictionary_to_elements(self, contents_dictionary_list):
        """Converts dictionary to elements"""
        converted_contents = []
        for element_dictionary in contents_dictionary_list:
            class_name = element_dictionary["class_name"]
            if class_name == "Player":
                element = Player(**element_dictionary)
            if class_name == "Animate":
                element = Animate(**element_dictionary)
            if class_name == "Chest":
                element = Chest(**element_dictionary)
            if class_name == "Door":
                element = Door(**element_dictionary)
                element.connects = element_dictionary["connects"]
            if class_name == "Location":
                element = Location(**element_dictionary)
                element.exits = element_dictionary["exits"]
                element.needs_rope = element_dictionary["needs_rope"]
            if class_name == "Thing":
                element = Thing(**element_dictionary)
                element.fixed = element_dictionary["fixed"]
                element.text = element_dictionary["text"]
                element.visible = element_dictionary["visible"]
                element.reveals = element_dictionary["reveals"]
                element.preposition = element_dictionary["preposition"]
                element.when_broken_do = element_dictionary["when_broken_do"]
                element.smell = element_dictionary["smell"]
                element.sound = element_dictionary["sound"]
                element.enterable = element_dictionary["enterable"]
            if class_name == "Element":
                element = Element(**element_dictionary)
            if class_name == "Activator":
                element = Activator(**element_dictionary)
                element.turn_on_method_name = element_dictionary["turn_on_method_name"]
                element.turn_off_method_name = element_dictionary["turn_off_method_name"]
            if class_name == "Food":
                element = Food(**element_dictionary)
                element.regen = element_dictionary["regen"]
                element.taste = element_dictionary["taste"]
                element.smell = element_dictionary["smell"]
            if class_name == "Rope":
                element = Rope(**element_dictionary)
                element.tied_to = element_dictionary["tied_to"]
            if class_name == "Tool":
                element = Tool(**element_dictionary)
            if len(element_dictionary["contents"]) > 0:
                element.contents = self.dictionary_to_elements(element_dictionary["contents"])
            converted_contents.append(element)
        return converted_contents
