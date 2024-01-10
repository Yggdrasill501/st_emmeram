# -*- coding: utf-8 -*-
"""Module for the map."""
import pygame
from st_emmeram.map.map_piece import MapPiece


class Map:
    """Class for the map."""

    def __init__(self, screen_size):
        self.map_pieces = {}
        self.screen_width, self.screen_height = screen_size
        self.map_piece_size = 75
        self.generate_initial_map_piece()

    def generate_initial_map_piece(self):
        initial_position = (self.screen_width // 2 - self.map_piece_size // 2,
                            self.screen_height // 2 - self.map_piece_size // 2)
        self.add_map_piece(initial_position)

    def add_map_piece(self, position):
        if position not in self.map_pieces:
            self.map_pieces[position] = MapPiece(position, size=(self.map_piece_size, self.map_piece_size))

    def update_map(self, player_position):
        map_piece_position = (player_position[0] - player_position[0] % self.map_piece_size,
                              player_position[1] - player_position[1] % self.map_piece_size)
        self.add_map_piece(map_piece_position)

    def draw(self, screen):
        for map_piece in self.map_pieces.values():
            map_piece.draw(screen)
