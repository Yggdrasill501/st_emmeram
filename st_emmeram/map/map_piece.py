# -*- coding: utf-8 -*-
"""Module containing the map piece class."""
import pygame
import random


class MapPiece:
    """Class for the map piece."""

    def __init__(self, position, size=(75, 75), piece_type=None) -> None:
        """Initialize the map piece."""
        self.images = [pygame.transform.scale(pygame.image.load(f"/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/map/road{i}.png"), size) for i in range(1, 5)]
        self.piece_type = piece_type if piece_type is not None else random.randint(1, 4)
        self.image = self.images[self.piece_type - 1]
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        # if self.piece_type == 1:
        #     self.allowed_moves = {'up': True, 'down': True, 'left': True, 'right': True}
        # elif self.piece_type == 2:
        #     self.allowed_moves = {'up': True, 'down': True, 'left': False, 'right': False}
        # elif self.piece_type == 3:
        #     self.allowed_moves = {'up': True, 'down': False, 'left': False, 'right': False}
        # elif self.piece_type == 4:
        #     self.allowed_moves = {'up': True, 'down': False, 'left': False, 'right': True}

    def is_move_allowed(self, direction):
        """Check if the move is allowed."""
        # return self.allowed_moves.get(direction, False)
        return True

    def draw(self, screen):
        """Draw the map piece."""
        screen.blit(self.image, self.rect)

    def get_type(self):
        return self.piece_type
