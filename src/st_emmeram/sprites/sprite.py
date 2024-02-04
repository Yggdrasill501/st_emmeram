from src.st_emmeram.sprites.stats import sprites_dict
import random

class Sprite:
    def __init__(self):
        self.sprites_dict = sprites_dict

    def sprite_list(self) -> list:
        return [sprite for sprite, amount in self.sprites_dict.items() for _ in range(amount["Amount"])]

    def render_random_sprite(self):

        self.sprite_list()
