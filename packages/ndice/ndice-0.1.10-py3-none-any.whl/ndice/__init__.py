"""ndice - A dice rolling library for games."""

from .constants import d2, d3, d4, d6, d8, d10, d12, d20, d100
from .constants import four_d6, three_d6, two_d6
from .dice import d, Dice, mod, nd
from .mods import plus, minus, times
from .op import Op
from .rng import AscendingRNG, FixedRNG, high, low, mid, PRNG, RNG, rng
from .roll import max_roll, min_roll, roll, roll_each_die


__version__ = '0.1.10'
__author__ = 'Don McCaughey'
__email__ = 'don@donm.cc'


# fmt: off
__all__ = [
    # constants
    'd2', 'd3', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100',
    'four_d6', 'three_d6', 'two_d6',
    # dice
    'd', 'Dice', 'mod', 'nd',
    # mods
    'plus', 'minus', 'times',
    # op
    'Op',
    # rng
    'AscendingRNG', 'FixedRNG', 'high', 'low', 'mid', 'PRNG', 'RNG', 'rng',
    # roll
    'max_roll', 'min_roll', 'roll', 'roll_each_die',
]
# fmt: on
