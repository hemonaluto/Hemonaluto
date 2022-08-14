"""test dungeon controller module"""
# pylint: disable=no-name-in-module
# pylint: disable=too-many-locals
# pylint: disable=line-too-long
import unittest
from unittest.mock import Mock
from parameterized import parameterized
from game.controller.dungeon_controller import DungeonController
from game.data.texts import INVALID_DIRECTION, KEY_MISSING, LOCKED_DOOR,\
    NO_TIED_ROPE, door_not_locked, door_unlocked
from game.model.door import Door
from game.model.player import Player

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
        mock_location = Mock()
        attrs = {
            "brief": brief,
            "visited": False
        }
        mock_location.configure_mock(**attrs)
        self.dungeon_master.all_name_locations.append(("test", mock_location))
        self.assertEqual(self.dungeon_master.brief("test"), expected)

    def test_get_player(self):
        """Test get_player method"""
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
        result_player = self.dungeon_master.get_player()
        self.assertEqual(mock_player, result_player)

    def test_get_score(self):
        """Test get_score method"""
        expected_score = 23452
        self.dungeon_master.player_score = expected_score
        actual_score = self.dungeon_master.get_score()
        self.assertEqual(expected_score, actual_score)

    def test_get_health(self):
        """Test get_health method"""
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
        actual_health = self.dungeon_master.get_health()
        self.assertEqual(expected_health, actual_health)

    @parameterized.expand([
        ["west", "west location"],
        ["east", LOCKED_DOOR],
        ["down", NO_TIED_ROPE],
        ["down", NO_TIED_ROPE],
        ["", INVALID_DIRECTION]
    ])
    def test_move_player(self, direction, expected_response):
        """Test move_player method"""
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
        mock_location_start.configure_mock(**mock_location_start_attrs)
        self.dungeon_master.all_name_locations.extend([
            ("start location", mock_location_start),
            ("west location", mock_location_west),
            ("east location", mock_location_east),
            ("down location", mock_location_down),
        ])
        self.dungeon_master.player_location = mock_location_start
        actual_response = self.dungeon_master.move_player(direction)
        self.assertEqual(expected_response, actual_response)

    @parameterized.expand([
        [True, True],
        [False, True],
        [True, False]
    ])
    def test_unlock(self, player_has_key: bool, locked: bool):
        """Test unlock method"""
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
        actual_response = self.dungeon_master.unlock(door_name)
        if player_has_key and locked:
            self.assertEqual(door_unlocked(door_name), actual_response)
        elif not player_has_key and locked:
            self.assertEqual(KEY_MISSING, actual_response)
        else:
            self.assertEqual(door_not_locked(door_name), actual_response)

    def test_set_player_location(self):
        """Test set player method"""
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
        self.dungeon_master.set_player_location(mock_player, mock_location)
        self.assertIn(mock_player, mock_location.contents)

    @parameterized.expand([
        ["table", "A quirky test table."],
        ["", "Test location\nYou are in a quirky test location.\nYou look around you and you see:\nA quirky test player.\nA quirky test table."]
    ])
    def test_describe(self, user_input, expected_response):
        """test describe method"""
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
        actual_response = self.dungeon_master.describe(user_input)
        self.assertEqual(expected_response, actual_response)

    def test_describe_location(self):
        """test describe_location method"""
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
        actual_response = self.dungeon_master.describe_location()
        self.assertEqual(expected_response, actual_response)

    def test_describe_element(self):
        """test describe_element method"""
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
        actual_response = self.dungeon_master.describe_element("table")
        self.assertEqual(expected_response, actual_response)

    def test_describe_container(self):
        """test describe_container method"""
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
        actual_response = self.dungeon_master.describe_container(mock_box)
        self.assertEqual(expected_response, actual_response)
