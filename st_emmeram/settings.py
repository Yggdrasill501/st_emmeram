# -*- coding: utf-8 -*-
"""Module for the settings of the game St. Emmeram."""
import numpy

# Plyer settings

# Rooms


# Hallway
_ = 0
HALLWAY_STRAIGHT = numpy.array([
    [_, _, _],
    [1, 1, 1],
    [_, _, _]
])

HALLWAY_CORNER = numpy.array([
    [_, 1, _],
    [1, 1, _],
    [_, _, _]
])

HALLWAY_CROSS = numpy.array([
