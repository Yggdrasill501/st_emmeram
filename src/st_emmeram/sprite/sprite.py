import abc
import random
import json
import logging

ModuleLogger = logging.getLogger(__name__)


class Sprite:

    def __init__(self):
        """Initialize.

        :rtype: None.
        """
        self.sprites_dict = self._get_dict(file="config.json")
        self.sprite_list = self.sprite_list()

    @abc.abstractmethod
    def _get_dict(file: str) -> dict:
        """From config creates Dict.

        :return: config dict,
        :rtype: dict
        """
        try:
            with open(file, 'r') as file:
                return json.load(file)

        except FileNotFoundError as E:
            ModuleLogger.error(msg=f"{file}, {E}")

    def sprite_list(self) -> list:
        return [sprite for sprite, amount in self.sprites_dict.items() for _ in range(amount["Amount"])]

    def render_random_sprite(self) -> int:
        return self.sprite_list[random.randint(0, 50)]
