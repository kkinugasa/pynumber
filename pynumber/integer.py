"""Set-theoretic construction of integers"""
from __future__ import annotations

from typing import NamedTuple

from pynumber.natural_number import NaturalNumber, create_natural_number_from_int


class Integer(
    NamedTuple("Integer", [("positive", NaturalNumber), ("negative", NaturalNumber)])
):
    """Integer

        Integer is an equivalence class of NaturalNumber pairs.
        One of a pair is a positive part and the other is a negative part.
        The equivalence relation (a, b) ~ (c, d) is a + d == b + c

    .. _Reference:
        https://math.stackexchange.com/questions/1695198/constructing-integers-as-equivalence-classes-of-pairs-of-natural-numbers
    """

    def __new__(
        cls: type[Integer], positive: NaturalNumber, negative: NaturalNumber
    ) -> Integer:
        """new

        For better performance, a canonical representative is selected,
        but it also works as follows::

            return super().__new__(cls, positive, negative)

        Args:
            cls (type[Integer]): cls
            positive (NaturalNumber): positive part of integer
            negative (NaturalNumber): negative part of integer

        Returns:
            Integer: integer
        """
        integer = int(positive) - int(negative)
        pos = create_natural_number_from_int(max(integer, 0))
        neg = create_natural_number_from_int(max(-integer, 0))
        return super().__new__(cls, pos, neg)

    def __eq__(self: Integer, obj: object) -> bool:
        return (
            isinstance(obj, Integer)
            and self.positive + obj.negative == self.negative + obj.positive
        )

    def __ne__(self: Integer, obj: object) -> bool:
        return not self == obj

    def __lt__(self: Integer, obj: object) -> bool:
        if not isinstance(obj, Integer):
            raise TypeError(f"{obj} is not 'Integer'")
        return self.positive + obj.negative < self.negative + obj.positive

    def __gt__(self: Integer, obj: object) -> bool:
        if not isinstance(obj, Integer):
            raise TypeError(f"{obj} is not 'Integer'")
        return self.positive + obj.negative > self.negative + obj.positive

    def __ge__(self: Integer, obj: object) -> bool:
        return not self < obj

    def __le__(self: Integer, obj: object) -> bool:
        return not self > obj

    def __add__(self: Integer, obj: object) -> Integer:
        if not isinstance(obj, Integer):
            raise TypeError(f"{obj} is not 'Integer'")
        # (a - b) + (c - d) = (a + c) - (b + d)
        return Integer(self.positive + obj.positive, self.negative + obj.negative)

    def __sub__(self: Integer, obj: object) -> Integer:
        if not isinstance(obj, Integer):
            raise TypeError(f"{obj} is not 'Integer'")
        # (a - b) - (c - d) = (a + d) - (b + c)
        return Integer(self.positive + obj.negative, self.negative + obj.positive)

    def __mul__(self: Integer, obj: object) -> Integer:
        if not isinstance(obj, Integer):
            raise TypeError(f"{obj} is not 'Integer'")
        # (a - b) * (c - d) = (a * c + b * d) - (a * d + b * c)
        return Integer(
            self.positive * obj.positive + self.negative * obj.negative,
            self.positive * obj.negative + self.negative * obj.positive,
        )

    def __pos__(self: Integer) -> Integer:
        return self

    def __neg__(self: Integer) -> Integer:
        return Integer(self.negative, self.positive)

    def __abs__(self: Integer) -> Integer:
        return max(self, -self)

    def __int__(self: Integer) -> int:
        return int(self.positive) - int(self.negative)


def create_integer_from_int(integer: int) -> Integer:
    """Create Integer from integer

    Args:
        integer (int): integer

    Returns:
        Integer: Integer instance that represents an argument integer
    """
    pos = create_natural_number_from_int(max(integer, 0))
    neg = create_natural_number_from_int(max(-integer, 0))
    return Integer(pos, neg)
