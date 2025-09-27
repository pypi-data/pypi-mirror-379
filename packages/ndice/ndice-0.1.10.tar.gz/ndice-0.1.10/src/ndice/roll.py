from .dice import Dice
from .rng import high, low, RNG


def roll(rng: RNG, *dice_expression: Dice) -> int:
    """Roll a set of dice and apply modifiers.

    An empty dice expression returns zero.

    >>> from ndice import mid
    >>> roll(mid)
    0

    Terms in the dice expression are totalled up from left to right.  (The
    ``Dice.op`` attribute does not change the order of operations.)

    >>> from ndice import d6, minus, times
    >>> roll(mid, d6, minus(1), times(10))
    20

    :param RNG rng: A random number generator.
    :param Dice dice_expression: A list of dice and modifiers.
    :return: The total rolled for the dice expression.
    """
    total = 0
    for dice_term in dice_expression:
        total = dice_term.op(total, sum(roll_each_die(rng, dice_term)))
    return total


def min_roll(*dice_expression: Dice) -> int:
    """The minimum total for a dice expression.

    >>> from ndice import d6, plus, times
    >>> min_roll(d6, plus(2), times(10))
    30

    This is equivalent to ``roll(low, ...)``.

    :param Dice dice_expression: A list of dice and modifiers.
    :return: The minimum total for the dice expression.
    """
    return roll(low, *dice_expression)


def max_roll(*dice_expression: Dice) -> int:
    """The maximum total for a dice expression.

    >>> from ndice import d6, plus, times
    >>> max_roll(d6, plus(2), times(10))
    80

    This is equivalent to ``roll(high, ...)``.

    :param Dice dice_expression: A list of dice and modifiers.
    :return: The maximum total for the dice expression.
    """
    return roll(high, *dice_expression)


def roll_each_die(rng: RNG, dice: Dice) -> list[int]:
    """Roll the given dice or mod, returning each die value rolled.

    >>> from ndice import mid, three_d6
    >>> roll_each_die(mid, three_d6)
    [3, 3, 3]

    If the ``dice`` parameter is a modifier, a list containing the mod value is
    returned.  The ``dice.op`` attribute is not applied to the returned value.

    >>> from ndice import mod, Op, rng
    >>> minus_2 = mod(Op.MINUS, 2)
    >>> roll_each_die(rng, minus_2)
    [2]

    :param RNG rng: A random number generator.
    :param Dice dice: A dice term or mod.
    :return: A list of the rolled die values.
    """
    if dice.is_mod:
        return [dice.number * dice.sides]
    else:
        return [_roll_die(rng, dice.sides) for _ in range(dice.number)]


def _roll_die(rng: RNG, sides: int) -> int:
    roll = rng(sides)
    assert 1 <= roll <= sides
    return roll
