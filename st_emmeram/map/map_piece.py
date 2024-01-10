# -*- coding: utf-8 -*-
"""Module containing the map piece class."""
import pygame


class MapPiece:
    """Class for the map piece."""

    def __init__(self, position, size=(75, 75)) -> None:
        """Initialize the map piece."""
        self.image = pygame.transform.scale(pygame.image.load("/st_emmeram/assets/map/road1.png"), size)
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen):
        """Draw the map piece."""
        screen.blit(self.image, self.rect)

