"""test dungeon controller module"""
import unittest
from unittest.mock import Mock
from parameterized import parameterized
from game.controller.dungeon_controller import DungeonController
from game.data.texts import INVALID_DIRECTION, LOCKED_DOOR
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
