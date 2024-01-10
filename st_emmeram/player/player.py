# -*- coding: utf-8 -*-
""""Module contains player."""
import pygame


class Player:
    """Class for the player."""

    def __init__(self, screen_size) -> None:
        """Initialize the player."""
        self.size = (50, 50)
        self.screen_width, self.screen_height = screen_size

        middle_position = (self.screen_width // 2 - self.size[0] // 2,
                           self.screen_height // 2 - self.size[1] // 2)

        self.image_centered = pygame.transform.scale(pygame.image.load("/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/player/vales_centered.png"), size=self.size)
        self.image_right = pygame.transform.scale(pygame.image.load("/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/player/vales_right.png"), size=self.size)
        self.image_left = pygame.transform.scale(pygame.image.load("/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/player/vales_left.png"), size=self.size)

        self.image = self.image_centered

        self.rect = self.image.get_rect(topleft=middle_position)
        self.speed = 5

    def move(self, direction) -> None:
        """Move the player."""
        if direction == "up":
            self.rect.y -= self.speed
            self.image = self.image_centered
        elif direction == "down":
            self.rect.y += self.speed
            self.image = self.image_centered
        elif direction == "left":
            self.rect.x -= self.speed
            self.image = self.image_left
        elif direction == "right":
            self.rect.x += self.speed
            self.image = self.image_right

        # self.check_boundaries()

    # def check_boundaries(self) -> None:
    #     if self.rect.left < 0:
    #         self.rect.right = self.screen_width
    #     elif self.rect.right > self.screen_width:
    #         self.rect.left = 0
    #     if self.rect.top < 0:
    #         self.rect.bottom = self.screen_height
    #     elif self.rect.bottom > self.screen_height:
    #         self.rect.top = 0

    def draw(self, screen):
        """Draw the player."""
        screen.blit(self.image, self.rect)