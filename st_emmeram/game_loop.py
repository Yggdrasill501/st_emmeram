# -*- coding: utf-8 -*-
"""Module for the game loop."""

import pygame
import sys
from st_emmeram.dice.dice import Dice


class GameLoop:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Dice Roll Game')

        self.dice1 = Dice((50, 50))
        self.dice2 = Dice((200, 50))
        self.font = pygame.font.Font(None, 36)
        self.sum_of_dice = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dice1.on_click(event.pos) or self.dice2.on_click(event.pos):
                        self.sum_of_dice = Dice.get_sum(self.dice1, self.dice2)

            self.screen.fill((0, 128, 255))
            self.dice1.draw(self.screen)
            self.dice2.draw(self.screen)

            sum_text = self.font.render(f'Sum: {self.sum_of_dice}', True, (0, 0, 0))
            self.screen.blit(sum_text, (50, 150))

            pygame.display.flip()

        pygame.quit()
        sys.exit()