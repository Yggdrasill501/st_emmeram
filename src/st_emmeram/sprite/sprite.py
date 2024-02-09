import random
from src.utilities.file_managment.json_to_dict import get_dict


class Sprite:

    def __init__(self):
        """Initialize.

        :rtype: None.
        """
        self.sprites_dict = get_dict(file="config.json")
        self.sprite_list = self.sprite_list()

    def sprite_list(self) -> list:
        return [sprite for sprite, amount in self.sprites_dict.items() for _ in range(amount["Amount"])]

    def render_random_sprite(self) -> int:
        return self.sprite_list[random.randint(0, 50)]
