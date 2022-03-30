"""Test code of NaturalNumber class"""

import pytest

from pynumber import ZERO, NaturalNumber


def test_equality() -> None:
    """Test __eq__ and __ne__"""
    zero = NaturalNumber(())
    one = NaturalNumber(((),))
    assert not ZERO == ()
    assert ZERO == zero
    assert one == ZERO.successor
    assert not zero == one
    assert zero != one


def test_inequality() -> None:
    """Test inequality"""
    one = NaturalNumber(((),))
    assert ZERO < one
    assert ZERO <= ZERO
    with pytest.raises(TypeError):
        _ = ZERO < ((),)
    with pytest.raises(TypeError):
        _ = ZERO <= ((),)


def test_successor() -> None:
    """Test successor"""
    one = NaturalNumber(((),))
    two = NaturalNumber((*tuple(one), tuple(one)))
    assert ZERO.successor == one
    assert ZERO.successor.successor == two


def test_predecessor() -> None:
    """Test predecessor"""
    one = ZERO.successor
    assert one.predecessor == ZERO
    with pytest.raises(ValueError):
        _ = ZERO.predecessor


def test_addition() -> None:
    """Test addition"""
    one = ZERO.successor
    two = one.successor
    three = two.successor
    assert ZERO + ZERO == ZERO
    assert one + ZERO == one
    assert one + two == three


def test_multiplication() -> None:
    """Test multiplication"""
    one = ZERO.successor
    two = one.successor
    three = two.successor
    six = three.successor.successor.successor
    assert ZERO * ZERO == ZERO
    assert ZERO * one == ZERO
    assert two * one == two
    assert two * three == six
    assert three * two == six
