"""Set-theoretic construction of integers"""

from __future__ import annotations

from typing import NamedTuple, TypeVar

from pynumber.natural import Natural, create_natural_from_int

TInteger = TypeVar("TInteger", bound="Integer")


class Integer(NamedTuple("Integer", [("positive", Natural), ("negative", Natural)])):
    """Integer

        Integer is an equivalence class of Natural pairs.
        One of a pair is a positive part and the other is a negative part.
        The equivalence relation (a, b) ~ (c, d) is a + d == b + c

    .. _Reference:
        https://math.stackexchange.com/questions/1695198/constructing-integers-as-equivalence-classes-of-pairs-of-natural-numbers
    """

    def __new__(
        cls: type[TInteger],
        positive: Natural | None = None,
        negative: Natural | None = None,
    ) -> TInteger:
        """new

        For better performance, a canonical representative is selected,
        but it also works as follows::

            return super().__new__(cls, positive, negative)

        Args:
            cls (type[Integer]): cls
            positive (Natural): positive part of integer
            negative (Natural): negative part of integer

        Returns:
            Integer: integer
        """
        # Avoid mutable/call defaults; compute here when None
        pos_in = positive if positive is not None else create_natural_from_int(0)
        neg_in = negative if negative is not None else create_natural_from_int(0)

        value = int(pos_in) - int(neg_in)
        pos = create_natural_from_int(max(value, 0))
        neg = create_natural_from_int(max(-value, 0))
        return tuple.__new__(cls, (pos, neg))

    def __eq__(self: Integer, other: object) -> bool:
        return (
            isinstance(other, Integer)
            and self.positive + other.negative == self.negative + other.positive
        )

    def __ne__(self: Integer, other: object) -> bool:
        return not self == other

    def __lt__(self: Integer, other: object) -> bool:
        if not isinstance(other, Integer):
            raise TypeError(f"{other} is not 'Integer'")
        return self.positive + other.negative < self.negative + other.positive

    def __gt__(self: Integer, other: object) -> bool:
        if not isinstance(other, Integer):
            raise TypeError(f"{other} is not 'Integer'")
        return self.positive + other.negative > self.negative + other.positive

    def __ge__(self: Integer, other: object) -> bool:
        return not self < other

    def __le__(self: Integer, other: object) -> bool:
        return not self > other

    def __add__(self: Integer, other: object) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError(f"{other} is not 'Integer'")
        # (a - b) + (c - d) = (a + c) - (b + d)
        return Integer(self.positive + other.positive, self.negative + other.negative)

    def __sub__(self: Integer, other: object) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError(f"{other} is not 'Integer'")
        # (a - b) - (c - d) = (a + d) - (b + c)
        return Integer(self.positive + other.negative, self.negative + other.positive)

    def __mul__(self: Integer, other: object) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError(f"{other} is not 'Integer'")
        # (a - b) * (c - d) = (a * c + b * d) - (a * d + b * c)
        return Integer(
            self.positive * other.positive + self.negative * other.negative,
            self.positive * other.negative + self.negative * other.positive,
        )

    def __pos__(self: Integer) -> Integer:
        return self

    def __neg__(self: Integer) -> Integer:
        return Integer(self.negative, self.positive)

    def __abs__(self: Integer) -> Integer:
        return max(self, -self)

    def __int__(self: Integer) -> int:
        return int(self.positive) - int(self.negative)

    @property
    def successor(self: Integer) -> Integer:
        """Get a successor number

        Args:
            self (Integer): Integer instance

        Returns:
            Integer: successor
        """
        return Integer(self.positive.successor, self.negative)

    @property
    def predecessor(self: Integer) -> Integer:
        """Get a predecessor number

        Args:
            self (Integer): Integer instance

        Returns:
            Integer: predecessor
        """
        return Integer(self.positive, self.negative.successor)

    @property
    def sign(self: Integer) -> Integer:
        """sign of integer

        Args:
            self (Integer): Integer instance

        Returns:
            Integer: +1, -1, or 0
        """
        if self.positive == self.negative:
            return Integer()
        if self.positive > self.negative:
            return Integer().successor
        return Integer().predecessor


def create_integer_from_int(integer: int) -> Integer:
    """Create Integer from integer

    Args:
        integer (int): integer

    Returns:
        Integer: Integer instance that represents an argument integer
    """
    pos = create_natural_from_int(max(integer, 0))
    neg = create_natural_from_int(max(-integer, 0))
    return Integer(pos, neg)
