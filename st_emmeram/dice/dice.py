# -*- coding: utf-8 -*-
"""Module for the dice."""
import pygame
import random


class Dice:
    """Class for the dice."""

    def __init__(self, position, size: tuple = (100, 100)) -> None:
        """Initialize the dice."""
        self.images = [pygame.transform.scale(pygame.image.load(f"/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/dice/{i}.png"), size=size) for i in range(1, 7)]
        self.current_value = 1
        self.rect = self.images[0].get_rect(topleft=position)

    def roll(self) -> None:
        """Roll the dice."""
        self.current_value = random.randint(1, 6)

    def draw(self, screen) -> None:
        """Draw the dice."""
        screen.blit(self.images[self.current_value - 1], self.rect)

    def get_value(self) -> int:
        """Get the value of the dice."""
        return self.current_value

    def on_click(self, event_position) -> bool:
        """Check if the dice was clicked."""
        if self.rect.collidepoint(event_position):
            self.roll()
            return True
        return False

    @staticmethod
    def get_sum(dice1, dice2) -> int:
        """Get the sum of two dice."""
        return dice1.get_value() + dice2.get_value()