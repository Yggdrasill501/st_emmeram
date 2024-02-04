import pygame
import sys

class GameLoop:
    def __init__(self):
        pass

    def game_loop(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Render Map

                # Render Player

                # if player enters room,
                    # render monster
                    # Combat