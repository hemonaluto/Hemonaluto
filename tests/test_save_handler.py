"""test save handler module"""
import unittest
from location import Location
from save_handler import SaveHandler

class TestSaveHandler(unittest.TestCase):
    """Test SaveHandler class"""

    def setUp(self):
        """Set up environment required for tests"""
        self.save_handler = SaveHandler()
        self.names_locations, self.player_location = self.save_handler.load("test_world.json")

    def test_load_names_locations(self):
        """Test if it loads names_locations correctly"""
        name = self.names_locations[0][0]
        location: Location = self.names_locations[0][1]
        self.assertEqual("test", name)
        self.assertEqual("test", location.name)
        self.assertEqual("test", location.description)
        self.assertEqual("Location", location.class_name)
        self.assertEqual("test", location.brief)
        self.assertEqual(True, location.has_light)
        self.assertEqual(True, location.needs_rope)
        self.assertEqual(10, len(location.contents))
        self.assertEqual("test", location.exits.get["test"])
