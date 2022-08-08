"""Generate test world module"""
import json
from elements.animate import Animate
from elements.chest import Chest
from elements.element import Element
from elements.activator import Activator
from elements.door import Door
from elements.food import Food
from elements.location import Location
from elements.player import Player
from elements.rope import Rope
from elements.thing import Thing
from elements.tool import Tool
from enums.activator_type import ActivatorType

test_activator = Activator("test", "test")
test_activator.type = ActivatorType.PRESS
test_activator.is_on = True
test_activator.turn_on_method_name = "test_turn_on_method"
test_activator.turn_off_method_name = "test_turn_off_method"
test_animate = Animate("test", "test")
test_animate.name = "test"
test_animate.description = "test"
test_animate.clothes = ["test"]
test_animate.health = "test"
test_chest = Chest("test", "test")
test_chest.open = True
test_chest.locked = True
test_chest.key = "test"
test_chest.peekable = True
test_door = Door("test", "test")
test_door.name = "test"
test_door.description = "test"
test_door.open = True
test_door.lockable = True
test_door.locked = True
test_door.key = "test"
test_door.connects = ["test"]
test_element = Element("test", "test")
test_element.name = "test"
test_element.description = "test"
test_element.visible = True
test_element.contents = [Element("test", "test")]
test_element.class_name = "test"
test_element.preposition = "test"
test_element.sound = "test"
test_element.smell = "test"
test_food = Food("test", "test")
test_player = Player("test", "test")
test_rope = Rope("test", "test")
test_thing = Thing("test", "test")
test_tool = Tool("test", "test")
test_location = Location("test", "test")
test_location.exits = {"test": "test"}
test_location.brief = "test"
test_location.has_light = True
test_location.needs_rope = True
test_location.contents.extend([
    test_activator,
    test_animate,
    test_chest,
    test_door,
    test_element,
    test_food,
    test_player,
    test_rope,
    test_thing,
    test_tool
])
class ElementEncoder(json.JSONEncoder):
    """json encoder for elements"""
    def default(self, o):
        return o.__dict__
with open("test_world.json", "w", encoding="UTF-8") as savefile:
    json.dump([("test", test_location)], savefile, indent=4, cls=ElementEncoder)
