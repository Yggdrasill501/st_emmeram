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
        self.rolled = False

    def roll(self):
        self.current_value = random.randint(1, 6)
        self.rolled = True

    def draw(self, screen) -> None:
        """Draw the dice."""
        screen.blit(self.images[self.current_value - 1], self.rect)

    def get_value(self) -> int:
        """Return the current value of the dice."""
        return self.current_value

    def has_been_rolled(self) -> bool:
        """Return True if the dice has been rolled, False otherwise."""
        return self.rolled

    def reset(self) -> None
        """Reset the dice."""
        self.rolled = False

    @staticmethod
    def calculate_sum(dice1, dice2) :
        """Calculate the sum of two dice."""
        if dice1.has_been_rolled() and dice2.has_been_rolled():
            return dice1.get_value() + dice2.get_value()
        return None
