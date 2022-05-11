"""Set-theoretic construction of rational numbers"""
from __future__ import annotations

import math
from typing import NamedTuple

from pynumber.integer import Integer, create_integer_from_int


class Rational(
    NamedTuple("Rational", [("numerator", Integer), ("denominator", Integer)])
):
    """Rational number

        Rational is defined by localization of Integer.

    .. _Reference:
        https://en.wikipedia.org/wiki/Localization_(commutative_algebra)
    """

    def __new__(
        cls: type[Integer],
        numerator: Integer = Integer(),
        denominator: Integer = Integer.successor,
    ) -> Rational:
        """new

        change denominator to be positive

        Args:
            cls (type[Integer]): cls
            numerator (Integer): numerator
            denominator (Integer): denominator

        Raises:
            ValueError: denominator is zero

        Returns:
            Rational: rational number
        """
        if denominator == Integer():
            raise ValueError("denominator is zero")

        #### For better performance, a canonical representative is selected,
        #### but it also works as follows::
        #    sign = (numerator.sign * denominator.sign).sign
        #    return super().__new__(cls, sign*abs(numerator), abs(denominator))

        # Change a denominator to be positive
        sign = int((numerator.sign * denominator.sign).sign)
        int_numerator = sign * abs(int(numerator))
        int_denominator = abs(int(denominator))
        gcd = math.gcd(int_numerator, int_denominator)
        return super().__new__(
            cls,
            create_integer_from_int(int_numerator // gcd),
            create_integer_from_int(int_denominator // gcd),
        )

    def __eq__(self: Rational, other: object) -> bool:
        return (
            isinstance(other, Rational)
            and self.numerator * other.denominator == self.denominator * other.numerator
        )

    def __ne__(self: Rational, other: object) -> bool:
        return not self == other

    def __lt__(self: Rational, other: object) -> bool:
        if not isinstance(other, Rational):
            raise TypeError(f"{other} is not 'Rational'")
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self: Rational, other: object) -> bool:
        if not isinstance(other, Rational):
            raise TypeError(f"{other} is not 'Rational'")
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self: Rational, other: object) -> bool:
        return not self < other

    def __le__(self: Rational, other: object) -> bool:
        return not self > other

    def __add__(self: Rational, other: object) -> Rational:
        if not isinstance(other, Rational):
            raise TypeError(f"{other} is not 'Rational'")
        # (a / b) + (c / d) = (a * d + b * c) / (b * d)
        return Rational(
            self.numerator * other.denominator + self.denominator * other.numerator,
            self.denominator * other.denominator,
        )

    def __sub__(self: Rational, other: object) -> Rational:
        if not isinstance(other, Rational):
            raise TypeError(f"{other} is not 'Rational'")
        # (a / b) - (c / d) = (a * d - b * c) / (b * d)
        return Rational(
            self.numerator * other.denominator - self.denominator * other.numerator,
            self.denominator * other.denominator,
        )

    def __mul__(self: Rational, other: object) -> Rational:
        if not isinstance(other, Rational):
            raise TypeError(f"{other} is not 'Rational'")
        # (a / b) * (c / d) = (a * c) / (b * d)
        return Rational(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    # TODO: div, unary operator
