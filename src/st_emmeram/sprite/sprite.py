from src.st_emmeram.sprite.stats import sprites_dict
import random


class Sprite:
    def __init__(self):
        self.sprites_dict = sprites_dict
        self.sprite_list = self.sprite_list()

    def sprite_list(self) -> list:
        return [sprite for sprite, amount in self.sprites_dict.items() for _ in range(amount["Amount"])]

    def render_random_sprite(self) -> int:
        return self.sprite_list[random.randint(0, 50)]


