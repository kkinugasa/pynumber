"""Set-theoretic construction of natural numbers"""

from __future__ import annotations


class Natural(tuple):
    """Natural number

    Natural number includes zero. Tuples are used instead of sets
    to simplify obtaining predessors.
    """

    @property
    def successor(self: Natural) -> Natural:
        """Get a successor number

        Args:
            self (Natural): Natural instance

        Returns:
            Natural: successor
        """
        return Natural((*tuple(self), tuple(self)))

    @property
    def predecessor(self: Natural) -> Natural:
        """Get a predecessor number

        Args:
            self (Natural): Natural Instance

        Raises:
            ValueError: self is zero

        Returns:
            Natural: predecessor
        """
        if self == Natural():
            raise ValueError(f"{self} does not have a predecessor")
        return Natural(self[0:-1])

    def __eq__(self: Natural, other: object) -> bool:
        return isinstance(other, Natural) and tuple(self) == tuple(other)

    def __ne__(self: Natural, other: object) -> bool:
        return not self == other

    def __lt__(self: Natural, other: object) -> bool:
        if not isinstance(other, Natural):
            raise TypeError(f"{other} is not 'Natural'")
        return tuple(self) in tuple(other)

    def __gt__(self: Natural, other: object) -> bool:
        if not isinstance(other, Natural):
            raise TypeError(f"{other} is not 'Natural'")
        return tuple(other) in tuple(self)

    def __ge__(self: Natural, other: object) -> bool:
        return not self < other

    def __le__(self: Natural, other: object) -> bool:
        return not self > other

    def __add__(self: Natural, other: object) -> Natural:
        if not isinstance(other, Natural):
            raise TypeError(f"{other} is not 'Natural'")
        if other == Natural():
            return self
        # m + n = (m + 1) + (n - 1)
        return self.successor + other.predecessor

    def __mul__(self: Natural, other: object) -> Natural:
        if not isinstance(other, Natural):
            raise TypeError(f"{other} is not 'Natural'")
        if other == Natural():
            return other
        # m * n = m * (n - 1) + m
        return self * other.predecessor + self

    def __pos__(self: Natural) -> Natural:
        return self

    def __int__(self: Natural) -> int:
        return len(self)

    def __repr__(self: Natural) -> str:
        return f"pynumber.natural.Natural({repr(tuple(self))})"

    def __str__(self: Natural) -> str:
        return f"Natural: {int(self)}"


def create_natural_from_int(integer: int) -> Natural:
    """Create Natural from integer

    Args:
        integer (int): integer

    Raises:
        ValueError: integer is negative

    Returns:
        Natural: Natural instance that represents an argument integer
    """
    if integer < 0:
        raise ValueError("Arg must be a non-negative integer.")
    return sum([Natural().successor] * integer, Natural())
