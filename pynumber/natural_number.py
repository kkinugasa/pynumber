"""Set-theoretic construction of natural numbers"""
from __future__ import annotations


class NaturalNumber(tuple):
    """Natural number

    Natural number includes zero. Tuples are used instead of sets
    to simplify obtaining predessors.
    """

    @property
    def successor(self: NaturalNumber) -> NaturalNumber:
        """Get a successor number

        Returns:
            NaturalNumber: successor
        """
        return NaturalNumber((*tuple(self), tuple(self)))

    @property
    def predecessor(self: NaturalNumber) -> NaturalNumber:
        """Get a predecessor number

        Returns:
            NaturalNumber: predecessor
        """
        # if obj == zero
        if not self:
            raise ValueError("ZERO does not have a predecessor")
        return NaturalNumber(self[0:-1])

    def __add__(self: NaturalNumber, obj: object) -> NaturalNumber:
        if not isinstance(obj, NaturalNumber):
            raise TypeError(f"{obj} is not 'NaturalNumber'")
        # if obj == zero
        if not obj:
            return self
        # m + n = (m + 1) + (n - 1)
        return self.successor + obj.predecessor

    def __mul__(self: NaturalNumber, obj: object) -> NaturalNumber:
        if not isinstance(obj, NaturalNumber):
            raise TypeError(f"{obj} is not 'NaturalNumber'")
        # if obj == zero
        if not obj:
            return obj
        # m * n = m * (n - 1) + m
        return self * obj.predecessor + self

    def __eq__(self: NaturalNumber, obj: object) -> bool:
        return isinstance(obj, NaturalNumber) and tuple(self) == tuple(obj)

    def __ne__(self: NaturalNumber, obj: object) -> bool:
        return not self == obj

    def __lt__(self: NaturalNumber, obj: object) -> bool:
        if not isinstance(obj, NaturalNumber):
            raise TypeError(f"{obj} is not 'NaturalNumber'")
        return tuple(self) in tuple(obj)

    def __gt__(self: NaturalNumber, obj: object) -> bool:
        if not isinstance(obj, NaturalNumber):
            raise TypeError(f"{obj} is not 'NaturalNumber'")
        return tuple(obj) in tuple(self)

    def __ge__(self: NaturalNumber, obj: object) -> bool:
        return not self < obj

    def __le__(self: NaturalNumber, obj: object) -> bool:
        return not self > obj


ZERO = NaturalNumber(())
