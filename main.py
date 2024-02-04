# -*- coding: utf-8 -*-
"""Main module where the game is called and run."""
from src.st_emmeram.game_loop import GameLoop

if __name__ == '__main__':
    game = GameLoop()
    game.game_loop()

