# -*- coding: utf-8 -*-
"""Package containing tests for module wall."""
import unittest
import logging
from PIL import Image
from st_emmeram.map.wall import Wall

MODULE_LOGGER = logging.getLogger(__name__)
MODULE_LOGGER.setLevel(logging.INFO)


class WallTest(unittest.TestCase):
    """Test class for class Wall."""

    def get_texture_test(self):
        """Test the method get_texture."""
        wall = Wall()
        texture = wall.get_texture()
        self.assertIsInstance(texture, Image.Image)


if __name__ == '__main__':
    unittest.main()
