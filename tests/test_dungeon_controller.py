"""test dungeon controller module"""
# pylint: disable=no-name-in-module
# pylint: disable=too-many-locals
# pylint: disable=line-too-long
import unittest
from unittest.mock import MagicMock, Mock
from parameterized import parameterized
from game.controller.activator_controller import ActivatorController
from game.controller.dungeon_controller import DungeonController
from game.data.texts import ALREADY_UNTIED, APPEARING, CANT_PICK_UP_SELF,\
    CLOSED, DONE, DOWN, ELEMENT_IS_FIXED, INVALID_DIRECTION,\
    KEY_MISSING, LOCKED_DOOR, NO_SMELLS, NO_TIED_ROPE, NOT_A_ROPE,\
    NOT_ENTERABLE, NOT_HIDING, NOT_OPENABLE, NOT_READABLE, SILENCE,\
    TARGET_NOT_SPECIFIED, THAT_WONT_HOLD, THREW_AT_NOTHING, UNTIE,\
    WEST, door_not_locked, door_unlocked, eat_food,\
    element_not_found, element_not_in_inventory, entering_thing,\
    hit_target, noises_description, picked_up_element, reveal_element,\
    smell_description, tie_rope_to_target
from game.model.animate import Animate
from game.model.door import Door
from game.model.enums.activator_type import ActivatorType
from game.model.location import Location
from game.model.player import Player
from game.model.rope import Rope
from game.model.thing import Thing
from game.model.food import Food
from game.model.tool import Tool
from game.model.chest import Chest
from game.model.activator import Activator

class TestDungeonController(unittest.TestCase):
    """Test DungeonController class"""

    def setUp(self):
        """Set up environment required for tests"""
        self.dungeon_master = DungeonController()

    @parameterized.expand([
        ["You enter a quirky test location.", "You enter a quirky test location.\n\n"],
        ["", ""],
    ])
    def test_brief(self, brief, expected):
        """Test brief method"""
        # Arrange
        mock_location = Mock()
        attrs = {
            "brief": brief,
            "visited": False
        }
        mock_location.configure_mock(**attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        # Act
        actual = self.dungeon_master.brief("test")
        # Assert
        self.assertEqual(actual, expected)

    def test_get_player(self):
        """Test get_player method"""
        # Arrange
        mock_player = Mock(spec=Player)
        mock_location = Mock()
        location_attrs = {
            "contents": [mock_player]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        # Act
        result_player = self.dungeon_master.get_player()
        # Assert
        self.assertEqual(mock_player, result_player)

    def test_get_score(self):
        """Test get_score method"""
        # Arrange
        expected_score = 23452
        self.dungeon_master.player_score = expected_score
        # Act
        actual_score = self.dungeon_master.get_score()
        # Assert
        self.assertEqual(expected_score, actual_score)

    def test_get_health(self):
        """Test get_health method"""
        # Arrange
        expected_health = 35262
        mock_player = Mock(spec=Player)
        mock_location = Mock()
        location_attrs = {
            "contents": [mock_player]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True,
            "health": expected_health
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        # Act
        actual_health = self.dungeon_master.get_health()
        # Assert
        self.assertEqual(expected_health, actual_health)

    @parameterized.expand([
        ["west", "west location"],
        ["east", LOCKED_DOOR],
        ["down", NO_TIED_ROPE],
        ["", INVALID_DIRECTION]
    ])
    def test_move_player(self, direction, expected_response):
        """Test move_player method"""
        # Arrange
        mock_player = Mock(spec=Player)
        mock_door = Mock(spec=Door)
        mock_location_start = Mock()
        mock_location_west = Mock()
        mock_location_east = Mock()
        mock_location_down = Mock()
        mock_player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True
        }
        mock_door_attrs = {
            "contents": [],
            "name": "Door",
            "locked": True,
            "visible": True,
            "connects": ["east location"]
        }
        mock_location_west_attrs = {
            "contents": [],
            "needs_rope": False,
            "name": "west location"
        }
        mock_location_east_attrs = {
            "contents": [],
            "needs_rope": False,
            "name": "east location"
        }
        mock_location_down_attrs = {
            "contents": [],
            "needs_rope": True,
            "name": "down location"
        }
        mock_location_down_attrs = {
            "contents": [],
            "needs_rope": True,
            "name": "down location"
        }
        mock_location_down_attrs = {
            "contents": [],
            "needs_rope": True,
            "name": "down location"
        }
        mock_location_down_attrs = {
            "contents": [],
            "needs_rope": True,
            "name": "down location"
        }
        mock_location_start_attrs = {
            "name": "start location",
            "contents": [mock_player, mock_door],
            "exits": {
                "west": "west location",
                "down": "down location",
                "east": "east location"
            }
        }
        mock_player.configure_mock(**mock_player_attrs)
        mock_door.configure_mock(**mock_door_attrs)
        mock_location_west.configure_mock(**mock_location_west_attrs)
        mock_location_east.configure_mock(**mock_location_east_attrs)
        mock_location_down.configure_mock(**mock_location_down_attrs)
        mock_location_down.configure_mock(**mock_location_down_attrs)
        mock_location_down.configure_mock(**mock_location_down_attrs)
        mock_location_down.configure_mock(**mock_location_down_attrs)
        mock_location_start.configure_mock(**mock_location_start_attrs)
        self.dungeon_master.all_name_locations.extend([
            ("start location", mock_location_start),
            ("west location", mock_location_west),
            ("east location", mock_location_east),
            ("down location", mock_location_down),
        ])
        self.dungeon_master.player_location = mock_location_start
        # Act
        actual_response = self.dungeon_master.move_player(direction)
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        [True, True],
        [False, True],
        [True, False]
    ])
    def test_unlock(self, player_has_key: bool, locked: bool):
        """Test unlock method"""
        # Arrange
        mock_door = Mock(spec=Door)
        door_name = "test door"
        mock_location = Mock()
        mock_player = Mock()
        mock_key = Mock()
        location_attrs = {
            "contents": [mock_door, mock_player]
        }
        if player_has_key:
            player_contents = [mock_key]
        else:
            player_contents = []
        player_attrs = {
            "contents": player_contents,
            "name": "Player",
            "visible": True
        }
        key_attrs = {
            "contents": [],
            "name": "test key",
            "visible": True
        }
        door_attrs = {
            "contents": [],
            "name": door_name,
            "locked": locked,
            "visible": True,
            "key": "test key"
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_key.configure_mock(**key_attrs)
        mock_door.configure_mock(**door_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.unlock(door_name)
        # Assert
        if player_has_key and locked:
            self.assertEqual(door_unlocked(door_name), actual_response)
        elif not player_has_key and locked:
            self.assertEqual(KEY_MISSING, actual_response)
        else:
            self.assertEqual(door_not_locked(door_name), actual_response)

    def test_set_player_location(self):
        """Test set player method"""
        # Arrange
        mock_location = Mock()
        mock_player = Mock()
        location_attrs = {
            "contents": []
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        # Act
        self.dungeon_master.set_player_location(mock_player, mock_location)
        # Assert
        self.assertIn(mock_player, mock_location.contents)

    @parameterized.expand([
        ["table", "A quirky test table."],
        ["", "Test location\nYou are in a quirky test location.\nYou look around you and you see:\nA quirky test player.\nA quirky test table."]
    ])
    def test_describe(self, user_input, expected_response):
        """test describe method"""
        # Arrange
        mock_location = Mock()
        mock_player = Mock()
        mock_table = Mock()
        location_attrs = {
            "name": "Test location",
            "description": "A quirky test location.",
            "contents": [mock_player, mock_table]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "description": "A quirky test player.",
            "hiding": False
        }
        table_attrs = {
            "contents": [],
            "name": "table",
            "description": "A quirky test table."
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_table.configure_mock(**table_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.describe(user_input)
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_describe_location(self):
        """test describe_location method"""
        # Arrange
        mock_location = Mock()
        mock_player = Mock()
        mock_table = Mock()
        location_attrs = {
            "name": "Test location",
            "description": "A quirky test location.",
            "contents": [mock_player, mock_table]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "description": "A quirky test player.",
            "hiding": False
        }
        table_attrs = {
            "contents": [],
            "name": "table",
            "description": "A quirky test table."
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_table.configure_mock(**table_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        expected_response = "Test location\nYou are in a quirky test location.\nYou look around you and you see:\nA quirky test player.\nA quirky test table."
        # Act
        actual_response = self.dungeon_master.describe_location()
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_describe_element(self):
        """test describe_element method"""
        # Arrange
        mock_location = Mock()
        mock_table = Mock()
        location_attrs = {
            "name": "Test location",
            "contents": [mock_table]
        }
        table_attrs = {
            "contents": [],
            "name": "table",
            "description": "A quirky test table."
        }
        mock_location.configure_mock(**location_attrs)
        mock_table.configure_mock(**table_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        expected_response = "A quirky test table."
        # Act
        actual_response = self.dungeon_master.describe_element("table")
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_describe_container(self):
        """test describe_container method"""
        # Arrange
        mock_box = Mock()
        mock_envelope = Mock()
        mock_letter = Mock()
        box_attrs = {
            "name": "box",
            "contents": [mock_envelope],
            "description": "A quirky test box.",
            "preposition": "in"
        }
        envelope_attrs = {
            "name": "envelope",
            "contents": [mock_letter],
            "description": "A quirky test envelope.",
            "preposition": "in"
        }
        letter_attrs = {
            "name": "letter",
            "contents": [],
            "description": "A quirky test letter.",
            "preposition": "in"
        }
        mock_box.configure_mock(**box_attrs)
        mock_envelope.configure_mock(**envelope_attrs)
        mock_letter.configure_mock(**letter_attrs)
        expected_response = "A quirky test box.\n    There is a envelope in the box.\n    There is a letter in the envelope."
        # Act
        actual_response = self.dungeon_master.describe_container(mock_box)
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_get_door_directions(self):
        """test get_door_directions"""
        # Arrange
        mock_location = Mock()
        mock_door = Mock()
        location_attrs = {
            "contents": [mock_door],
            "exits": {
                WEST: "quirky location",
                DOWN: "special location"
            },
        }
        door_attrs = {
            "connects": ["quirky location"]
        }
        mock_location.configure_mock(**location_attrs)
        mock_door.configure_mock(**door_attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.dungeon_master.player_location = mock_location
        expected_response = ["west"]
        # Act
        actual_response = self.dungeon_master.get_door_directions((mock_door, mock_location))
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        ["envelope", "box"],
        ["letter", "envelope"]
    ])
    def test_get_element_container(self, element_name, expected_container_name):
        """test get_element_container method"""
        # Arrange
        mock_location = Mock()
        mock_box = Mock()
        mock_envelope = Mock()
        mock_letter = Mock()
        location_attrs = {
            "name": "Test location",
            "contents": [mock_box]
        }
        box_attrs = {
            "name": "box",
            "contents": [mock_envelope]
        }
        envelope_attrs = {
            "name": "envelope",
            "contents": [mock_letter]
        }
        letter_attrs = {
            "name": "letter",
            "contents": [],
        }
        mock_location.configure_mock(**location_attrs)
        mock_box.configure_mock(**box_attrs)
        mock_envelope.configure_mock(**envelope_attrs)
        mock_letter.configure_mock(**letter_attrs)
        # Act
        actual_element_container = self.dungeon_master.get_element_container(element_name, mock_location)
        # Assert
        self.assertEqual(actual_element_container[0].name, element_name)
        self.assertEqual(actual_element_container[1].name, expected_container_name)

    @parameterized.expand([
        [False, False],
        [False, True],
        [True, False]
    ])
    def test_get_all_elements_container(self, only_takeable, only_visible):
        """test get_all_elements_container method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_box = Mock(spec=Thing)
        mock_envelope = Mock(spec=Thing)
        mock_letter = Mock(spec=Thing)
        location_attrs = {
            "name": "Test location",
            "contents": [mock_box],
            "fixed": True,
            "visible": True
        }
        box_attrs = {
            "name": "box",
            "contents": [mock_envelope],
            "fixed": True,
            "visible": True
        }
        envelope_attrs = {
            "name": "envelope",
            "contents": [mock_letter],
            "fixed": True,
            "visible": False
        }
        letter_attrs = {
            "name": "letter",
            "contents": [],
            "fixed": False,
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_box.configure_mock(**box_attrs)
        mock_envelope.configure_mock(**envelope_attrs)
        mock_letter.configure_mock(**letter_attrs)
        # Act
        actual_elements_container = self.dungeon_master.get_all_elements_container(
            mock_location,
            only_visible,
            only_takeable
        )
        # Assert
        if only_takeable:
            self.assertEqual(len(actual_elements_container), 1)
        elif only_visible:
            self.assertEqual(len(actual_elements_container), 2)
        else:
            # actual_elements_container..
            #   [0]<-the element_container tuple to test
            #   [1]<-the index of the tuple, in this case container
            self.assertEqual(actual_elements_container[0][1].name, mock_location.name)
            self.assertEqual(actual_elements_container[1][1].name, mock_box.name)
            self.assertEqual(actual_elements_container[2][1].name, mock_envelope.name)

    @parameterized.expand([
        ["table", ELEMENT_IS_FIXED],
        ["knife", picked_up_element("knife")],
        ["spoon", element_not_found("spoon")],
        ["player", CANT_PICK_UP_SELF]
    ])
    def test_take(self, element_to_take, expected_response):
        """test take method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_table = Mock(spec=Thing)
        mock_knife = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_player, mock_table],
            "name": "Test location",
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "hiding": False,
            "visible": True,
            "fixed": False
        }
        table_attrs = {
            "contents": [mock_knife],
            "name": "table",
            "fixed": True,
            "visible": True
        }
        knife_attrs = {
            "contents": [],
            "name": "knife",
            "fixed": False,
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_table.configure_mock(**table_attrs)
        mock_knife.configure_mock(**knife_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.take(element_to_take)
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_get_player_inventory(self):
        """test get_player_inventory method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_apple = Mock(spec=Food)
        mock_orange = Mock(spec=Food)
        location_attrs = {
            "contents": [mock_player]
        }
        player_attrs = {
            "contents": [mock_apple, mock_orange],
            "name": "Player",
            "visible": True
        }
        apple_attrs = {
            "contents": [],
            "name": "apple",
            "visible": True
        }
        orange_attrs = {
            "contents": [],
            "name": "orange",
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_apple.configure_mock(**apple_attrs)
        mock_orange.configure_mock(**orange_attrs)
        self.dungeon_master.player_location = mock_location
        expected_response = mock_apple.name + "\n" + mock_orange.name + "\n"
        # Act
        actual_response = self.dungeon_master.get_player_inventory()
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        ["sickle at enemy", element_not_found("sickle")],
        ["hammer at gandalf", element_not_found("gandalf")],
        ["hammer at enemy", hit_target("enemy")],
        ["hammer", THREW_AT_NOTHING]
    ])
    def test_throw(self, instructions, expected_response):
        """test throw method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_hammer = Mock(spec=Tool)
        mock_enemy = Mock(spec=Animate)
        location_attrs = {
            "contents": [mock_player, mock_enemy]
        }
        player_attrs = {
            "contents": [mock_hammer],
            "name": "Player",
            "visible": True
        }
        hammer_attrs = {
            "contents": [],
            "name": "hammer",
            "visible": True,
            "damage": 2
        }
        enemy_attrs = {
            "contents": [],
            "name": "enemy",
            "visible": True,
            "health": 10
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_hammer.configure_mock(**hammer_attrs)
        mock_enemy.configure_mock(**enemy_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.throw(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == "hammer at enemy":
            # 7 because throwing damage is x1.5, so 10-2*1.5
            self.assertEqual(mock_enemy.health, 7)

    @parameterized.expand([
        ["chest", CLOSED],
        ["door", CLOSED],
        ["bed", NOT_OPENABLE],
        ["picture", element_not_found("picture")]
    ])
    def test_close(self, element_to_close, expected_response):
        """test close method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_chest = Mock(spec=Chest)
        mock_door = Mock(spec=Door)
        mock_bed = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_chest, mock_door, mock_bed]
        }
        chest_attrs = {
            "contents": [],
            "name": "chest",
            "visible": True,
            "open": True,
            "peekable": True
        }
        door_attrs = {
            "contents": [],
            "name": "door",
            "visible": True,
            "open": True
        }
        bed_attrs = {
            "contents": [],
            "name": "bed",
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_chest.configure_mock(**chest_attrs)
        mock_door.configure_mock(**door_attrs)
        mock_bed.configure_mock(**bed_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.close(element_to_close)
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        ["scroll", "quirky test text"],
        ["table", NOT_READABLE],
        ["E", element_not_found("E")]
    ])
    def test_read(self, element_name, expected_response):
        """test read method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_scroll = Mock(spec=Thing)
        mock_table = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_scroll, mock_table]
        }
        scroll_attrs = {
            "contents": [],
            "name": "scroll",
            "visible": True,
            "text": "quirky test text"
        }
        table_attrs = {
            "contents": [],
            "name": "table",
            "visible": True,
            "text": None
        }
        mock_location.configure_mock(**location_attrs)
        mock_scroll.configure_mock(**scroll_attrs)
        mock_table.configure_mock(**table_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.read(element_name)
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        ["spoon in mug", DONE],
        ["sword in mug", element_not_found("sword")],
        ["spoon in bowl", element_not_found("bowl")],
        ["get spooned", TARGET_NOT_SPECIFIED]
    ])
    def test_put(self, instructions, expected_response):
        """test put method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_mug = Mock(spec=Thing)
        mock_spoon = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_player, mock_mug]
        }
        player_attrs = {
            "contents": [mock_spoon],
            "name": "Player",
            "visible": True
        }
        mug_attrs = {
            "contents": [],
            "name": "mug",
            "visible": True
        }
        spoon_attrs = {
            "contents": [],
            "name": "spoon",
            "visible": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_mug.configure_mock(**mug_attrs)
        mock_spoon.configure_mock(**spoon_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.put(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == "spoon in mug":
            self.assertEqual(mock_mug.contents[0].name, "spoon")

    @parameterized.expand([
        ["lever on", "It makes a quirky bootup noise."],
        ["lever off", "That's already turned off."],
        ["button on", element_not_found("button")]
    ])
    def test_activate(self, instructions, expected_response):
        """test activate method"""
        # Arrange
        mock_activator_controller = Mock(spec=ActivatorController)
        mock_activator_controller.lever_on = MagicMock(return_value="It makes a quirky bootup noise.")
        self.dungeon_master.activator_handler = mock_activator_controller
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_lever = Mock(spec=Activator)
        location_attrs = {
            "contents": [mock_player, mock_lever]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True
        }
        lever_attrs = {
            "contents": [],
            "name": "lever",
            "visible": True,
            "is_on": False,
            "turn_on_method_name": "lever_on"
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_lever.configure_mock(**lever_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.activate(instructions, ActivatorType.PRESS)
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        ["rug", reveal_element("rug", "A quirky diamond.")],
        ["diamond", element_not_found("diamond")]
    ])
    def test_move_element(self, instructions, expected_response):
        """test move_element method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_rug = Mock(spec=Thing)
        mock_diamond = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_rug, mock_diamond]
        }
        rug_attrs = {
            "contents": [],
            "name": "rug",
            "visible": True,
            "reveals": "diamond"
        }
        diamond_attrs = {
            "contents": [],
            "name": "diamond",
            "visible": False,
            "description": "A quirky diamond."
        }
        mock_location.configure_mock(**location_attrs)
        mock_rug.configure_mock(**rug_attrs)
        mock_diamond.configure_mock(**diamond_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.move_element(instructions)
        # Assert
        self.assertEqual(actual_response, expected_response)
        if instructions == "rug":
            self.assertEqual(mock_diamond.visible, True)

    @parameterized.expand([
        ["enemy with knife", hit_target("enemy")],
        ["glas with knife", "The glas shatters."],
        ["laptop with knife", element_not_found("laptop")],
        ["enemy with nintendo", element_not_in_inventory("nintendo")]
    ])
    def test_attack(self, instructions, expected_response):
        """test attack method"""
        # Arrange
        mock_activator_controller = Mock(spec=ActivatorController)
        mock_activator_controller.glas_break = MagicMock(return_value="The glas shatters.")
        self.dungeon_master.activator_handler = mock_activator_controller
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_enemy = Mock(spec=Animate)
        mock_knife = Mock(spec=Tool)
        mock_glas = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_player, mock_enemy, mock_glas]
        }
        player_attrs = {
            "contents": [mock_knife],
            "name": "player",
            "visible": True
        }
        enemy_attrs = {
            "contents": [],
            "name": "enemy",
            "visible": True,
            "health": 10
        }
        knife_attrs = {
            "contents": [],
            "name": "knife",
            "visible": True,
            "damage": 5
        }
        glas_attrs = {
            "contents": [],
            "name": "glas",
            "visible": True,
            "description": "A quirky test glas.",
            "breakable": True,
            "when_broken_do": "glas_break"
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_enemy.configure_mock(**enemy_attrs)
        mock_knife.configure_mock(**knife_attrs)
        mock_glas.configure_mock(**glas_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.attack(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == "enemy with knife":
            self.assertEqual(mock_enemy.health, 5)


    @parameterized.expand([
        ["pear", element_not_found("pear")],
        ["apple", eat_food("apple", "It tastes quirky.")]
    ])
    def test_eat(self, instructions, expected_response):
        """test eat method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_apple = Mock(spec=Food)
        location_attrs = {
            "contents": [mock_player, mock_apple]
        }
        player_attrs = {
            "contents": [],
            "name": "player",
            "visible": True,
            "health": 10
        }
        apple_attrs = {
            "contents": [],
            "name": "apple",
            "visible": True,
            "taste": "It tastes quirky.",
            "regen": 5
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_apple.configure_mock(**apple_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.eat(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == "apple":
            self.assertEqual(mock_player.health, 15)

    @parameterized.expand([
        ["string to chair", element_not_in_inventory("string")],
        ["rope to table", element_not_found("table")],
        ["chair to pole", NOT_A_ROPE],
        ["rope", TARGET_NOT_SPECIFIED],
        ["rope to chair", THAT_WONT_HOLD],
        ["rope to pole", tie_rope_to_target("pole")]
    ])
    def test_tie(self, instructions, expected_response):
        """test tie method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_rope = Mock(spec=Rope)
        mock_chair = Mock(spec=Thing)
        mock_pole = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_player, mock_pole]
        }
        player_attrs = {
            "contents": [mock_rope, mock_chair],
            "name": "player",
            "visible": True
        }
        rope_attrs = {
            "contents": [],
            "name": "rope",
            "visible": True
        }
        chair_attrs = {
            "contents": [],
            "name": "chair",
            "visible": True,
            "fixed": False
        }
        pole_attrs = {
            "contents": [],
            "name": "pole",
            "visible": True,
            "fixed": True
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_rope.configure_mock(**rope_attrs)
        mock_chair.configure_mock(**chair_attrs)
        mock_pole.configure_mock(**pole_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.tie(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == "rope to pole":
            self.assertEqual(mock_rope.tied_to, "pole")


    @parameterized.expand([
        ["yarn", element_not_found("yarn")],
        ["rope", UNTIE],
        ["string", ALREADY_UNTIED]
    ])
    def test_untie(self, instructions, expected_response):
        """test untie method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_rope = Mock(spec=Rope)
        mock_string = Mock(spec=Rope)
        location_attrs = {
            "contents": [mock_player, mock_rope, mock_string]
        }
        player_attrs = {
            "contents": [],
            "name": "player",
            "visible": True
        }
        rope_attrs = {
            "contents": [],
            "name": "rope",
            "visible": True,
            "tied_to": "pole"
        }
        string_attrs = {
            "contents": [],
            "name": "string",
            "visible": True,
            "tied_to": None
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_rope.configure_mock(**rope_attrs)
        mock_string.configure_mock(**string_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.untie(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == "rope":
            self.assertIsNone(mock_rope.tied_to)

    @parameterized.expand([
        ["A quirky melody.", noises_description(["A quirky melody."])],
        [None, SILENCE]
    ])
    def test_listen(self, piano_noise, expected_response):
        """test listen method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_piano = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_piano]
        }
        piano_attrs = {
            "contents": [],
            "name": "piano",
            "visible": True,
            "sound": piano_noise
        }
        mock_location.configure_mock(**location_attrs)
        mock_piano.configure_mock(**piano_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.listen()
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        ["A quirky smell.", smell_description(["A quirky smell."])],
        [None, NO_SMELLS]
    ])
    def test_smell(self, kebab_smell, expected_response):
        """test smell method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_kebab = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_kebab]
        }
        kebab_attrs = {
            "contents": [],
            "name": "piano",
            "visible": True,
            "smell": kebab_smell
        }
        mock_location.configure_mock(**location_attrs)
        mock_kebab.configure_mock(**kebab_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.smell()
        # Assert
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        [" in wardrobe", entering_thing("wardrobe")],
        [" in cup", NOT_ENTERABLE],
        [" in bed", element_not_found("bed")]
    ])
    def test_hide(self, instructions, expected_response):
        """test smell method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        mock_wardrobe = Mock(spec=Thing)
        mock_cup = Mock(spec=Thing)
        location_attrs = {
            "contents": [mock_player, mock_wardrobe, mock_cup]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True,
            "hiding": False
        }
        wardrobe_attrs = {
            "contents": [],
            "name": "wardrobe",
            "visible": True,
            "enterable": True
        }
        cup_attrs = {
            "contents": [],
            "name": "cup",
            "visible": True,
            "enterable": False
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        mock_wardrobe.configure_mock(**wardrobe_attrs)
        mock_cup.configure_mock(**cup_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.hide(instructions)
        # Assert
        self.assertEqual(expected_response, actual_response)
        if instructions == " in wardrobe":
            self.assertTrue(mock_player.hiding)

    @parameterized.expand([
        [True, APPEARING],
        [False, NOT_HIDING]
    ])
    def test_appear(self, ishidden, expected_response):
        """test appear method"""
        # Arrange
        mock_location = Mock(spec=Location)
        mock_player = Mock(spec=Player)
        location_attrs = {
            "contents": [mock_player]
        }
        player_attrs = {
            "contents": [],
            "name": "Player",
            "visible": True,
            "hiding": ishidden
        }
        mock_location.configure_mock(**location_attrs)
        mock_player.configure_mock(**player_attrs)
        self.dungeon_master.player_location = mock_location
        # Act
        actual_response = self.dungeon_master.appear()
        # Assert
        self.assertEqual(expected_response, actual_response)
        if ishidden:
            self.assertFalse(mock_player.hiding)
