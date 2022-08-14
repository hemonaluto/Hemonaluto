"""test activator controller module"""
# pylint: disable=no-name-in-module
import unittest

from game.controller.activator_controller import ActivatorController
from game.data.scenario_texts import BUTTON_GOES_DARK, BUTTON_LIGHTS_UP

class TestActivatorController(unittest.TestCase):
    """Test ActivatorController class"""

    def setUp(self):
        """Set up environment required for tests"""
        self.activator_handler = ActivatorController()

    def test_bedroom_button_on(self):
        """Test bedroom button on method"""
        self.assertEqual(self.activator_handler.bedroom_button_on(), BUTTON_LIGHTS_UP)

    def test_bedroom_button_off(self):
        """Test bedroom button off method"""
        self.assertEqual(self.activator_handler.bedroom_button_off(), BUTTON_GOES_DARK)
