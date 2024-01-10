# -*- coding: utf-8 -*-
"""Module for the map."""
import pygame
from st_emmeram.map.map_piece import MapPiece
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Map:
    """Class for the map."""

    def __init__(self, screen_size):
        self.map_pieces = {}
        self.screen_width, self.screen_height = screen_size
        self.map_piece_size = 75
        self.generate_initial_map_piece()

    def generate_initial_map_piece(self):
        initial_x = (self.screen_width // 2) - (self.map_piece_size // 2)
        initial_y = (self.screen_height // 2) - (self.map_piece_size // 2)
        initial_position = (initial_x, initial_y)
        print(f"Initial map piece position: {initial_position}")  # Debug print
        self.add_map_piece(initial_position)

    def add_map_piece(self, position, piece_type=None):
        if position not in self.map_pieces:
            self.map_pieces[position] = MapPiece(position, size=(self.map_piece_size, self.map_piece_size),
                                                 piece_type=piece_type)

    def update_map(self, player_position):
        grid_x = player_position[0] - (player_position[0] % self.map_piece_size)
        grid_y = player_position[1] - (player_position[1] % self.map_piece_size)
        map_piece_position = (grid_x, grid_y)

        if map_piece_position not in self.map_pieces:
            print(f"Adding new map piece at: {map_piece_position}")  # Debug print
            self.add_map_piece(map_piece_position)

    def draw(self, screen):
        for map_piece in self.map_pieces.values():
            map_piece.draw(screen)

    def get_piece_type_at_position(self, position):
        return self.map_pieces.get(position)
        # piece = self.map_pieces.get(position, None)
        # if piece is None:
        #     logging.debug(f"No map piece at position: {position}")
        # else:
        #     logging.debug(f"Map piece at position: {position}, type: {piece.get_type()}")
        # return piece
