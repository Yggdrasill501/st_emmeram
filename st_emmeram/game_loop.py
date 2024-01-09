# -*- coding: utf-8 -*-
"""Module for the game loop."""

import pygame
import sys
from st_emmeram.dice.dice import Dice
from st_emmeram.player.player import Player


class GameLoop:
    """Class for the game loop."""

    def __init__(self) -> None:
        """Initialize the game loop."""
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Saint Emmeram')

        # self.background_image = pygame.image.load("/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/background/pixel.png")

        self.dice1 = Dice((50, 50))
        self.dice2 = Dice((200, 50))

        self.player = Player((80, 80), (self.width, self.height))

        self.font = pygame.font.Font(None, 36)
        self.sum_of_dice = 0

    # def draw_background(self):
    #     """Draw the background."""
    #     for y in range(0, self.height, self.background_image.get_height()):
    #         for x in range(0, self.width, self.background_image.get_width()):
    #             self.screen.blit(self.background_image, (x, y))

    def run(self) -> None:
        """Run the game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dice1.on_click(event.pos) or self.dice2.on_click(event.pos):
                        self.sum_of_dice = Dice.get_sum(self.dice1, self.dice2)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.player.move("up")
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.player.move("down")
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.player.move("left")
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.player.move("right")
            self.draw_background()

            self.dice1.draw(self.screen)
            self.dice2.draw(self.screen)

            self.player.draw(self.screen)

            sum_text = self.font.render(f'Sum: {self.sum_of_dice}', True, (0, 0, 0))
            self.screen.blit(sum_text, (50, 150))

            pygame.display.flip()

        pygame.quit()
        sys.exit()
