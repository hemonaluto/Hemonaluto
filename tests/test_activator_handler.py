"""test activator handler module"""
import unittest

from hemonaluto.activator_handler import ActivatorHandler
from hemonaluto.data.scenario_texts import BUTTON_GOES_DARK, BUTTON_LIGHTS_UP

class TestActivatorHandler(unittest.TestCase):
    """Test ActivatorHandler class"""

    def setUp(self):
        """Set up environment required for tests"""
        self.activator_handler = ActivatorHandler()

    def test_bedroom_button_on(self):
        """Test bedroom button on method"""
        self.assertEqual(self.activator_handler.bedroom_button_on(), BUTTON_LIGHTS_UP)

    def test_bedroom_button_off(self):
        """Test bedroom button off method"""
        self.assertEqual(self.activator_handler.bedroom_button_off(), BUTTON_GOES_DARK)
