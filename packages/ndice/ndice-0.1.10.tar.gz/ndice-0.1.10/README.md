# ndice

A dice rolling library for games.

[![builds.sr.ht status][builds-badge]][builds]
[![ndice on PyPI][pypi-badge]][pypi]
[![ndice docs][docs-badge]][docs]

[builds-badge]: https://builds.sr.ht/~donmcc/ndice.svg
[builds]: https://builds.sr.ht/~donmcc/ndice
[pypi-badge]: https://img.shields.io/pypi/v/ndice
[pypi]: https://pypi.org/project/ndice/
[docs-badge]: https://img.shields.io/badge/ndice-docs-blue
[docs]: https://ndice.donm.cc

`ndice` is a package for rolling dice expressions like **d6+2** or **3d6-3x10**
with a compact API.

    >>> from ndice import d6, d8, d20, d100, plus, minus, times, rng, roll
    
    >>> if roll(rng, d100) <= 25:
    ...     copper = roll(rng, d6, times(1000))

    >>> str_mod = minus(1)
    >>> magic_sword_mod = plus(2)
    >>> ac = 13

    >>> if roll(rng, d20, str_mod, magic_sword_mod) >= ac:
    ...     damage = roll(rng, d8)


## Operations (Op)

The `Op` enum defines the three operations used in dice expressions: `Op.PLUS`
(+), `Op.MINUS` (-) and `Op.TIMES` (x).


## Dice

A `Dice` object represents a single term in a dice expression like **2d6** or
**-2**.  The `Dice` object contains three attributes: `number`, `sides` and `op`. 
The values for `number` and `sides` must be zero or greater.  If not specified,
`op` defaults to `Op.PLUS`.

Rolling zero dice with any number of sides always returns 0.  Rolling any number
of zero-sided dice also always returns 0.

Constant modifiers ("mods") like **-2** or **x10** are defined as `Dice`
instances where `number` is the mod value and `sides` is 1.

`ndice` contains predefined common dice like `d6`, `d20` and `three_d6`.  A single
die type can be defined with the `d()` function, an alias for `Dice.die()`.

    >>> from ndice import d

    >>> d5 = d(5)

A number of dice can be defined with the `nd()` function, an alias for
`Dice.n_dice()`.

    >>> from ndice import nd

    >>> three_d8 = nd(3, 8)

Instances of `Dice` are immutable and cached, so `d(6)` will return the same `Dice`
instance that `d6` refers to.

    >>> from ndice import d, d6

    >>> d(6) is d6  # always true
    True

Individual `Dice` instances are ordered according to (`number`, `sides`, `op`),
where `Op.PLUS` comes first and `Op.TIMES` last.

    >>> from ndice import d6, two_d6, three_d6, minus, times

    >>> assert d6 < minus(d6) < times(d6) < two_d6 < three_d6

A `Dice` object is hashable and can be used in sets or as keys in dicts.


## Random Number Generators (RNG)

Rolling dice requires a "random" number generator.  A number generator is a
function or callable object that takes an `int` with the max die roll (i.e. the
number of sides) and returns an `int` value in the range `[1, sides]`.  The type
alias `RNG` can be used to annotate number generator variables.

The `rng` generator produces actual random numbers.  The `PRNG()` constructor
function creates random number generator functions that return deterministic
pseudo-random number sequences based on a given seed value.

    >>> from ndice import PRNG, roll, three_d6

    >>> prng1 = PRNG(1122334455)
    >>> roll(prng1, three_d6)
    10

    # restart the same pseudo-random sequence
    >>> prng2 = PRNG(1122334455)
    >>> roll(prng2, three_d6)
    10

Fake generators `high` and `low` always roll the highest or lowest values
respectively.  The `mid` generator always rolls the middle value or lower of the
two middle values: when rolling a three-sided die, `mid` returns 2; when rolling
a six-sided die with middle values of 3 and 4, `mid` returns 3.

`AscendingRNG()` and `FixedRNG()` create other fake generators.  Creating a
custom fake generator can be as simple as creating a function or lambda.

    >>> from ndice import d100, RNG

    >>> always_2: RNG = lambda sides: 2
    >>> roll(always_2, d100)
    2


## Rolls

The `roll()` function takes a number generator and zero or more `Dice` instances
making up a _dice expression_.  It returns the total of the dice expression.

    >>> from ndice import minus, PRNG, roll, two_d6

    >>> prng = PRNG(1122334455)
    >>> roll(prng, two_d6, minus(2))
    6

If no dice are given, `roll()` returns zero.

    >>> from ndice import roll, d6, minus, times, rng, high

    >>> roll(rng)
    0

    >>> dice_expression = []
    >>> # oops, forgot to add terms to the dice expression ...
    >>> roll(rng, *dice_expression)
    0

Note that dice expressions are always evaluated from left to right; `times()` or
`Op.TIMES` does not have higher precedence than plus or minus.  This is
different than the equivalent Python numeric expression, where `*` and `/` are
evaluated before `+` and `-`.

    >>> total = roll(high, d6, minus(1), times(10))
    >>> total
    50
    
    >>> assert 6 - 1 * 10 != total
    >>> assert (6 - 1) * 10 == total

The `min_roll()` and `max_roll()` functions are equivalent to `roll(low, ...)`
and `roll(high, ...)` respectively.


### Individual Die Rolls

Sometimes you need the individual die rolls rather than the total.  The
`roll_each_die()` function returns the individual die rolls of a `Dice` object
as a list.

    >>> from ndice import four_d6, PRNG, roll_each_die

    >>> prng = PRNG(1122334455)
    >>> roll_each_die(prng, four_d6)
    [4, 4, 2, 6]
