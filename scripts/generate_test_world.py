"""Generate test world module"""
import os
import sys
import json
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH
)
sys.path.append(SOURCE_PATH)
from game.model.animate import Animate
from game.model.chest import Chest
from game.model.element import Element
from game.model.activator import Activator
from game.model.door import Door
from game.model.food import Food
from game.model.location import Location
from game.model.player import Player
from game.model.rope import Rope
from game.model.thing import Thing
from game.model.tool import Tool
from game.model.enums.activator_type import ActivatorType
from game.helper_methods import isinstanceorsubclass

test_elements = [
    Activator("test", "test"),
    Animate("test", "test"),
    Chest("test", "test"),
    Door("test", "test"),
    Food("test", "test"),
    Element("test", "test"),
    Player("test", "test"),
    Rope("test", "test"),
    Thing("test", "test"),
    Tool("test", "test"),
    Location("test", "test")
]

for element in test_elements:
    if isinstanceorsubclass(element, Activator):
        element.type = ActivatorType.PRESS
        element.is_on = True
        element.turn_on_method_name = "test_turn_on_method"
        element.turn_off_method_name = "test_turn_off_method"
    if isinstanceorsubclass(element, Animate):
        element.clothes = ["test"]
        element.health = 50
    if isinstanceorsubclass(element, Chest):
        element.open = True
        element.locked = True
        element.key = "test"
        element.peekable = True
    if isinstanceorsubclass(element, Door):
        element.open = True
        element.lockable = True
        element.locked = True
        element.key = "test"
        element.connects = ["test"]
    if isinstanceorsubclass(element, Food):
        element.regen = 50
        element.taste = "test"
    if isinstanceorsubclass(element, Player):
        element.hiding = True
    if isinstanceorsubclass(element, Rope):
        element.tied_to = "test"
    if isinstanceorsubclass(element, Thing):
        element.when_broken_do = "test_broken_method"
        element.reveals = "test"
        element.moved = True
        element.fixed = True
        element.visible = True
        element.enterable = True
        element.wearable = True
        element.text = "test"
    if isinstanceorsubclass(element, Tool):
        element.damage = 50
        element.durability = 50
    if isinstanceorsubclass(element, Element):
        element.visible = True
        element.preposition = "test"
        element.sound = "test"
        element.smell = "test"
        element.contents = [Element("test", "test")]

test_location = Location("test", "test")
test_location.exits = {"test": "test"}
test_location.brief = "test"
test_location.has_light = True
test_location.needs_rope = True
test_location.visited = True
test_location.contents.extend(test_elements)

class ElementEncoder(json.JSONEncoder):
    """json encoder for elements"""
    def default(self, o):
        return o.__dict__

with open("tests/test_world.json", "w", encoding="UTF-8") as savefile:
    json.dump([test_location], savefile, indent=4, cls=ElementEncoder)
