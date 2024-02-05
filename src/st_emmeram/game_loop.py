import pygame
import src.st_emmeram.inventory.inventory
import src.st_emmeram.health_bar.health_bar
import sys


class GameLoop:
    def __init__(self):
        pygame.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

    def game_loop(self):
        running = True
        while running:

            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Render health bar
                # Render Inventory

                # Render Map

                # Render Player

                # if player enters room,
                    # render monster
                    # Combat


        pygame.quit()
        sys.exit()