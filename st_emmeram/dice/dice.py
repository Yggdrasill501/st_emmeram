# -*- coding: utf-8 -*-
"""Module for the dice."""
import pygame
import random


class Dice:
    """Class for the dice."""

    def __init__(self, position, size: tuple = (100, 100)) -> None:
        """Initialize the dice."""
        self.images = [pygame.transform.scale(pygame.image.load(f"assets/dice/{i}.png"), size=size) for i in range(1, 7)]
        self.current_value = 1
        self.rect = self.images[0].get_rect(topleft=position)
        self.rolled = False

    def roll(self):
        """Roll the dice."""
        self.current_value = random.randint(1, 6)
        self.rolled = True

    def draw(self, screen):
        """Draw the dice."""
        screen.blit(self.images[self.current_value - 1], self.rect)

    def get_value(self):
        """Get the value of the dice."""
        return self.current_value

    def has_been_rolled(self):
        """Check if the dice has been rolled."""
        return self.rolled

    def reset(self):
        """Reset the dice."""
        self.rolled = False

    def handle_click(self, event_pos):
        """Handle the click on the dice."""
        if self.rect.collidepoint(event_pos) and not self.rolled:
            self.roll()
            return True
        return False

    @staticmethod
    def calculate_sum(dice1, dice2):
        """Calculate the sum of the dice."""
        if dice1.has_been_rolled() and dice2.has_been_rolled():
            return dice1.get_value() + dice2.get_value()
        return None
