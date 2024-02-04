# -*- coding: utf-8 -*-
"""Package containing tests for module wall."""
import os
import unittest
import logging
from PIL import Image
from src.st_emmeram_original.map.wall import Wall
from src.st_emmeram_original.settings import walls_folder

MODULE_LOGGER = logging.getLogger(__name__)
MODULE_LOGGER.setLevel(logging.INFO)


class TestWall(unittest.TestCase):
    """Test class for class Wall."""

    def setUp(self):
        """Set up the test."""
        MODULE_LOGGER.info('Start test.')
        self.wall_folder = walls_folder

    def test_get_texture(self):
        """Test the method get_texture."""
        wall = Wall()

        # Call the method
        texture = wall.get_texture()

        # Assertions
        self.assertIsInstance(texture, Image.Image)

        self.assertIsInstance(texture, Image.Image)

        # Check if the returned image matches one of the test images
        matches_one_of_the_images = False
        for file_name in os.listdir(self.wall_folder):
            file_path = os.path.join(self.wall_folder, file_name)
            if os.path.isfile(file_path):
                with Image.open(file_path) as test_image:
                    if list(texture.getdata()) == list(test_image.getdata()):
                        matches_one_of_the_images = True
                        break

        self.assertTrue(matches_one_of_the_images)


if __name__ == '__main__':
    unittest.main()
