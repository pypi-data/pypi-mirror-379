from .dice import Dice, mod
from .op import Op


def plus(value: int | Dice) -> Dice:
    """Make an additive dice term.

    >>> plus(1)
    Dice(1, 1)

    >>> from ndice import d4
    >>> plus(d4)
    Dice(1, 4)

    :param int | Dice value: A ``int`` mod value or existing ``Dice`` instance.
    :return: A new dice term with operation ``Op.PLUS``.
    """
    return value.to_plus() if isinstance(value, Dice) else mod(Op.PLUS, value)


def minus(value: int | Dice) -> Dice:
    """Make a subtractive dice term.

    >>> minus(2)
    Dice(2, 1, Op.MINUS)

    >>> from ndice import d6
    >>> minus(d6)
    Dice(1, 6, Op.MINUS)

    :param int | Dice value: A ``int`` mod value or existing ``Dice`` instance.
    :return: A new dice term with operation ``Op.MINUS``.
    """
    return value.to_minus() if isinstance(value, Dice) else mod(Op.MINUS, value)


def times(value: int | Dice) -> Dice:
    """Make a multiplicative dice term.

    >>> times(3)
    Dice(3, 1, Op.TIMES)

    >>> from ndice import d8
    >>> times(d8)
    Dice(1, 8, Op.TIMES)

    :param int | Dice value: A ``int`` mod value or existing ``Dice`` instance.
    :return: A new dice term with operation ``Op.TIMES``.
    """
    return value.to_times() if isinstance(value, Dice) else mod(Op.TIMES, value)
