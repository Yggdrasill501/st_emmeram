# -*- coding: utf-8 -*-
"""Module for the game loop."""
import logging
import pygame
import sys
from st_emmeram.dice.dice import Dice
from st_emmeram.player.player import Player
from st_emmeram.map.map import Map

logging.basicConfig(level=logging.INFO)


class GameLoop:
    """Class for the game loop."""

    def __init__(self) -> None:
        """Initialize the game loop."""
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Saint Emmeram')

        # self.background_image = pygame.image.load("/Users/yggdrasill501/Projects/code/python/st_emmeram/st_emmeram/assets/background/pixel.png")

        self.dice1 = Dice((50, 50))
        self.dice2 = Dice((200, 50))

        self.game_map = Map((self.width, self.height))

        self.map_piece_size = 75

        self.player = Player((self.width, self.height))

        self.font = pygame.font.Font(None, 36)
        self.sum_of_dice = 0

        self.clock = pygame.time.Clock()

    # def draw_background(self):
    #     """Draw the background."""
    #     for y in range(0, self.height, self.background_image.get_height()):
    #         for x in range(0, self.width, self.background_image.get_width()):
    #             self.screen.blit(self.background_image, (x, y))

    # def draw_debug_grid(self):
    #     for x in range(0, self.width, self.map_piece_size):
    #         for y in range(0, self.height, self.map_piece_size):
    #             pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.map_piece_size, self.map_piece_size), 1)

    def run(self) -> None:
        """Run the game loop."""
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dice1.handle_click(event.pos):
                        if self.dice2.has_been_rolled():
                            self.dice2.reset()
                    if self.dice2.handle_click(event.pos):
                        if self.dice1.has_been_rolled():
                            self.dice1.reset()

                    sum_of_dice = Dice.calculate_sum(self.dice1, self.dice2)
                    if sum_of_dice is not None:
                        self.sum_of_dice = sum_of_dice

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.player.move("up")
            if keys[pygame.K_s]:
                self.player.move("down")
            if keys[pygame.K_a]:
                self.player.move("left")
            if keys[pygame.K_d]:
                self.player.move("right")

            # player_center_x, player_center_y = self.player.rect.center
            # grid_x = player_center_x - (player_center_x % 70)
            # grid_y = player_center_y - (player_center_y % 70)
            # player_map_piece_position = (grid_x, grid_y)
            #
            # current_map_piece = self.game_map.get_piece_type_at_position(player_map_piece_position)
            #
            # if current_map_piece:
            #     if keys[pygame.K_w] and current_map_piece.is_move_allowed("up"):
            #         self.player.move("up")
            #     if keys[pygame.K_s] and current_map_piece.is_move_allowed("down"):
            #         self.player.move("down")
            #     if keys[pygame.K_a] and current_map_piece.is_move_allowed("left"):
            #         self.player.move("left")
            #     if keys[pygame.K_d] and current_map_piece.is_move_allowed("right"):
            #         self.player.move("right")

            # self.draw_background()
            self.screen.fill((255, 255, 255))

            self.game_map.update_map((self.player.rect.x, self.player.rect.y))
            self.game_map.draw(self.screen)

            self.dice1.draw(self.screen)
            self.dice2.draw(self.screen)

            self.player.draw(self.screen)

            sum_text = self.font.render(f'Sum: {self.sum_of_dice}', True, (0, 0, 0))
            self.screen.blit(sum_text, (50, 150))

            pygame.display.flip()

        pygame.quit()
        sys.exit()


