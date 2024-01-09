# -*- coding: utf-8 -*-
""""Module contains player."""
import pygame


class Player:
    """Class for the player."""

    def __init__(self, position, size=(50, 50)) -> None:
        """Initialize the player."""
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.color = (0, 255, 0)
        self.speed = 5

    def move(self, direction) -> None:
        """Move the player."""
        if direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed
        elif direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

    def draw(self, screen):
        """Draw the player."""
        pygame.draw.rect(screen, self.color, self.rect)
