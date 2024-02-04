# -*- coding: utf-8 -*-
"""Test module for the GameLoop class."""
import unittest
from src.st_emmeram_original import GameLoop


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game = GameLoop()

    def test_initial_sum(self):
        self.assertEqual(self.game.sum_of_dice, 0, "Initial sum should be 0")

    # Add more tests for other Game methods as needed


if __name__ == '__main__':
    unittest.main()