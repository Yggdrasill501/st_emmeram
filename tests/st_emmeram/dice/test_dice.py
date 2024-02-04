# -*- coding: utf-8 -*-
"""Test module for the Dice class."""

import unittest
from src.st_emmeram.dice.dice import Dice


class TestDice(unittest.TestCase):
    """Test class for the Dice class."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.dice = Dice((0, 0))  # Position is irrelevant for these tests

    def test_initial_value(self):
        """Test the initial value of the dice."""
        self.assertEqual(self.dice.get_value(), 1, "Initial value of dice should be 1")

    def test_roll(self):
        """Test the roll method of the dice."""
        self.dice.roll()
        value = self.dice.get_value()
        self.assertTrue(1 <= value <= 6, "Dice roll should be between 1 and 6")

    def test_calculate_sum(self):
        """Test the sum calculation of two dice."""
        dice1 = Dice((0, 0))
        dice2 = Dice((0, 0))
        dice1.current_value = 3
        dice2.current_value = 4
        self.assertEqual(Dice.get_sum(dice1, dice2), 7, "Sum calculation is incorrect")


if __name__ == '__main__':
    unittest.main()