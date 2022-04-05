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

        Returns:
            Natural: successor
        """
        return Natural((*tuple(self), tuple(self)))

    @property
    def predecessor(self: Natural) -> Natural:
        """Get a predecessor number

        Returns:
            Natural: predecessor
        """
        # if obj == zero
        if not self:
            raise ValueError("ZERO does not have a predecessor")
        return Natural(self[0:-1])

    def __eq__(self: Natural, obj: object) -> bool:
        return isinstance(obj, Natural) and tuple(self) == tuple(obj)

    def __ne__(self: Natural, obj: object) -> bool:
        return not self == obj

    def __lt__(self: Natural, obj: object) -> bool:
        if not isinstance(obj, Natural):
            raise TypeError(f"{obj} is not 'Natural'")
        return tuple(self) in tuple(obj)

    def __gt__(self: Natural, obj: object) -> bool:
        if not isinstance(obj, Natural):
            raise TypeError(f"{obj} is not 'Natural'")
        return tuple(obj) in tuple(self)

    def __ge__(self: Natural, obj: object) -> bool:
        return not self < obj

    def __le__(self: Natural, obj: object) -> bool:
        return not self > obj

    def __add__(self: Natural, obj: object) -> Natural:
        if not isinstance(obj, Natural):
            raise TypeError(f"{obj} is not 'Natural'")
        # if obj == zero
        if not obj:
            return self
        # m + n = (m + 1) + (n - 1)
        return self.successor + obj.predecessor

    def __mul__(self: Natural, obj: object) -> Natural:
        if not isinstance(obj, Natural):
            raise TypeError(f"{obj} is not 'Natural'")
        # if obj == zero
        if not obj:
            return obj
        # m * n = m * (n - 1) + m
        return self * obj.predecessor + self

    def __pos__(self: Natural) -> Natural:
        return self

    def __int__(self: Natural) -> int:
        return len(self)


ZERO = Natural(())


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
    return sum([ZERO.successor] * integer, ZERO)
