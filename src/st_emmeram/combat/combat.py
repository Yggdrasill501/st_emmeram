import pygame
import logging

Module_Logger = logging.getLogger(__name__)


class Combat:
    def __init__(self,
                 players_damage: int,
                 monster_damage: int) -> None:
        """Initialize.

        :param players_damage: int, players damage,
        :param monster_damage: int, monster damage,
        :rtype: None
        """
        self.player_damage = players_damage
        self.monster_damage = monster_damage

    def combat(self):
        """"""
        # render dices take the output
        # self.plater_damage += Dice.result()

        if self.player_damage >= self.monster_damage:
            Module_Logger.info("Player won")
            return True
        else:
            Module_Logger.info("Monster won")
            return False
