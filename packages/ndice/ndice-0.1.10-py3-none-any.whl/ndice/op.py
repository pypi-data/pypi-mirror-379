from enum import Enum
from functools import total_ordering
from typing import Any, Callable


type BinaryFunction = Callable[[int, int], int]


@total_ordering
class Op(Enum):
    """Operations applied to terms in dice expressions.

    An ``Op`` is a binary operation applied to two ``int`` values.  Three ``Op`` cases
    are defined: ``PLUS``, ``MINUS``, and ``TIMES``.  ``Op`` cases are sortable and
    ordered, with ``PLUS`` first and ``TIMES`` last.

    >>> Op.PLUS < Op.MINUS < Op.TIMES
    True

    Each ``Op`` case has two attributes: ``symbol`` and ``f``.

    The ``symbol`` attribute is a ``str`` containing a single character: ``'+'``,
    ``'-'`` or ``'x'`` respectively.  Note that the symbol for ``Op.TIMES`` is the
    letter ``x`` rather than the symbol ``*``.

    The ``f`` attribute contains a function that implements the binary operation.

    ``Op`` cases are also callable, executing ``f`` on the provided arguments.

    >>> Op.PLUS(1, 2)
    3
    """

    PLUS = '+', int.__add__  #: The addition operation
    MINUS = '-', int.__sub__  #: The subtraction operation
    TIMES = 'x', int.__mul__  #: The multiplication operation

    def __init__(self, symbol: str, f: BinaryFunction):
        self.symbol = symbol
        self.f = f

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}.{self.name}'

    def __str__(self) -> str:
        return self.symbol

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Op):
            return self.symbol < other.symbol
        else:
            return NotImplemented

    def __call__(self, a: int, b: int) -> int:
        return self.f(a, b)
