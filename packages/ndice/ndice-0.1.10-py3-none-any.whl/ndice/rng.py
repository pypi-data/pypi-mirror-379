from random import randrange, Random
from typing import Callable, TypeAlias


RNG: TypeAlias = Callable[[int], int]


def rng(sides: int) -> int:
    """A truly random number generator.

    >>> assert 1 <= rng(6) <= 6

    Uses the global ``Random.randrange()`` function.
    """
    return randrange(sides) + 1


def high(sides: int) -> int:
    """A fake number generator that always returns the highest roll.

    >>> [high(6) for _ in range(3)]
    [6, 6, 6]
    """
    return sides


def low(sides: int) -> int:
    """A fake number generator that always returns the lowest roll.

    >>> [low(6) for _ in range(3)]
    [1, 1, 1]

    The lowest roll is always 1.
    """
    return 1


def mid(sides: int) -> int:
    """A fake number generator that always returns the middle roll.

    If the number of sides is odd, the middle value in [1, sides] is returned.

    >>> [mid(3) for _ in range(3)]
    [2, 2, 2]

    If the number of sides is even, the lower of the two middle values in
    [1, sides] is returned.

    >>> [mid(6) for _ in range(3)]
    [3, 3, 3]
    """
    return (sides + 1) // 2


def AscendingRNG(initial_value: int) -> RNG:
    """Create a fake number generator that returns ascending values.

    The returned ``RNG`` callable produces an ascending sequence of values,
    starting with ``initial_value``.

    >>> arng = AscendingRNG(2)
    >>> [arng(6) for _ in range(3)]
    [2, 3, 4]

    If the internal value is less than 1, the ``RNG`` will produce 1.

    >>> arng = AscendingRNG(0)
    >>> [arng(6) for _ in range(3)]
    [1, 1, 2]

    If the internal value is greater than the ``sides`` argument, the `RNG` will
    apply the modulus functions so that values wrap around.

    >>> arng = AscendingRNG(6)
    >>> [arng(6) for _ in range(3)]
    [6, 1, 2]

    :param int initial_value:
    :return: a fake number generator that returns ascending values.
    """
    ascending_value = initial_value

    def ascending(sides: int) -> int:
        nonlocal ascending_value
        next_value = (max(ascending_value, 1) - 1) % sides + 1
        ascending_value += 1
        return next_value

    return ascending


def FixedRNG(fixed_value: int) -> RNG:
    """Create a fake number generator that returns a fixed value.

    The returned ``RNG`` callable produces values based a fixed value.

    >>> always_2 = FixedRNG(2)
    >>> [always_2(6) for _ in range(3)]
    [2, 2, 2]

    If the fixed value is less than 1, 1 is returned.

    >>> always_1 = FixedRNG(0)
    >>> [always_1(6) for _ in range(3)]
    [1, 1, 1]

    If the fixed value is greater than the ``sides`` argument, ``sides`` is
    returned.

    >>> always_6 = FixedRNG(6)
    >>> always_6(6)
    6
    >>> always_6(4)
    4

    :param int fixed_value:
    :return: a fake number generator that returns a fixed value.
    """
    return lambda sides: _clamp(1, fixed_value, sides)


def PRNG(seed: int) -> RNG:
    """Create a pseudo-random number generator.

    The returned ``RNG`` callable produces a deterministic sequence of values
    based on the seed value.  The returned number generator is useful when
    reproducibility is needed, such as for testing.

    >>> prng = PRNG(1122334455)
    >>> sides = 6
    >>> [prng(sides) for _ in range(10)]
    [4, 4, 2, 6, 3, 1, 1, 1, 5, 3]

    :param int seed: The seed value that selects a the deterministic sequence.
    :return: a pseudo-random number generator.
    """
    r = Random(seed)
    return lambda sides: r.randrange(sides) + 1


def _clamp(lower: int, value: int, upper: int) -> int:
    return max(lower, min(value, upper))
