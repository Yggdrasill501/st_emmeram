# -*- coding: utf-8 -*-
"""Module for the wall class."""
import random
import os
from PIL import Image
from src.st_emmeram.settings import walls_folder


class Wall:
    """Class for the wall."""

    def __init__(self):
        """Initialize the wall."""
        self.walls_folder = walls_folder

    def get_texture(self) -> Image:
        files_and_dirs = os.listdir(self.walls_folder)

        files = [f for f in files_and_dirs if os.path.isfile(os.path.join(self.walls_folder, f))]

        random_texture = random.choice(files)
        file_path = os.path.join(self.walls_folder, random_texture)

        return Image.open(file_path)
