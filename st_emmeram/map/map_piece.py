# -*- coding: utf-8 -*-
"""Module containing the map piece class."""
import pygame
import random


class MapPiece:
    """Class for the map piece."""

    def __init__(self, position, size=(75, 75)) -> None:
        """Initialize the map piece."""
        self.images = [pygame.transform.scale(pygame.image.load(f"/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/map/road{i}.png"), size) for i in range(1, 5)]

        self.image = random.choice(self.images)
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen):
        """Draw the map piece."""
        screen.blit(self.image, self.rect)

