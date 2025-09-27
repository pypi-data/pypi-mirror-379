from __future__ import annotations

from dataclasses import dataclass

from .interned import interned
from .op import Op


@interned
@dataclass(frozen=True, order=True, slots=True)
class Dice:
    """A single term in a dice expression like **2d6** or **-2**.

    Instances of `Dice` are immutable.  `Dice` instances are also interned,
    meaning each unique instance is cached and reused instead of creating
    duplicates.
    """

    number: int  #: The number of dice to roll; must be zero or greater.
    sides: int  #: The number of sides of each die; must be zero or greater.
    op: Op = Op.PLUS  #: The operation before this term in a dice expression.

    def __post_init__(self) -> None:
        assert self.number >= 0
        assert self.sides >= 0

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        if Op.PLUS == self.op:
            return f'{cls_name}({self.number}, {self.sides})'
        else:
            return f'{cls_name}({self.number}, {self.sides}, {self.op!r})'

    def __str__(self) -> str:
        if self.is_mod:
            mod = self.number * self.sides
            return f'{self.op}{mod}'
        else:
            op = '' if Op.PLUS == self.op else self.op
            number = '' if 1 == self.number else self.number
            return f'{op}{number}d{self.sides}'

    @property
    def is_mod(self) -> bool:
        """Is this dice term a modifier?

        A modifier (mod) will always evaluate to a constant value.  Mods are
        represented as `Dice` instances where `number` is the constant value of
        the mod and `sides` is 1.
        """
        return 0 == self.number or 0 == self.sides or 1 == self.sides

    def to_plus(self) -> Dice:
        """Return a new `Dice` instance with the operation set to `Op.PLUS`."""
        return self.__class__(self.number, self.sides, Op.PLUS)

    def to_minus(self) -> Dice:
        """Return a new `Dice` instance with the operation set to `Op.MINUS`."""
        return self.__class__(self.number, self.sides, Op.MINUS)

    def to_times(self) -> Dice:
        """Return a new `Dice` instance with the operation set to `Op.TIMES`."""
        return self.__class__(self.number, self.sides, Op.TIMES)

    @classmethod
    def die(cls, sides: int) -> Dice:
        """Return a `Dice` instance that represents a single die.

        :param int sides: The number of sides on the die.  Must be >= 0.

        >>> Dice.die(12)
        Dice(1, 12)

        ``d()`` is an alias for ``Dice.die()``.

        >>> d(8)
        Dice(1, 8)
        """
        return cls(1, sides)

    @classmethod
    def mod(cls, op: Op, value: int) -> Dice:
        """Return a `Dice` instance that represents a modifier.

        :param Op op: The operation of the modifier.
        :param int value: The magnitude of the modifier.  Must be >= 0.

        Mods are represented as `Dice` instances where `number` is the constant
        value of the mod and `sides` is 1.

        >>> Dice.mod(Op.MINUS, 2)
        Dice(2, 1, Op.MINUS)

        ``mod()`` is an alias for ``Dice.mod()``.

        >>> mod(Op.TIMES, 10)
        Dice(10, 1, Op.TIMES)
        """
        return cls(value, 1, op)

    @classmethod
    def n_dice(cls, number: int, sides: int | Dice) -> Dice:
        """Return a `Dice` instance that represents a number of dice.

        :param int number: The number of dice.  Must be >= 0.
        :param int | Dice sides: The number of sides on each die.  Must be >= 0.

        >>> Dice.n_dice(2, 8)
        Dice(2, 8)

        If the ``sides`` argument is a `Dice` instance, its ``sides`` attribute is
        used for the returned `Dice` but its other attributes are ignored.

        >>> from ndice import d4
        >>> Dice.n_dice(2, d4)
        Dice(2, 4)

        ``nd()`` is an alias for ``Dice.n_dice()``.

        >>> nd(4, 6)
        Dice(4, 6)

        """
        sides_value = sides.sides if isinstance(sides, Dice) else sides
        return cls(number, sides_value, Op.PLUS)


d = Dice.die
mod = Dice.mod
nd = Dice.n_dice
