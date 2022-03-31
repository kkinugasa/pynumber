"""Test Integer class"""

import pytest

from pynumber import ZERO, Integer


def test_equality() -> None:
    """Test __eq__ and __ne__"""
    zero = Integer(ZERO, ZERO)
    zero2 = Integer(ZERO.successor, ZERO.successor)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    assert not zero == ZERO
    assert zero == zero2
    assert minus_one != zero


def test_inequality() -> None:
    """Test inequality"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert one >= zero
    assert minus_one <= zero
    with pytest.raises(TypeError):
        _ = zero < ZERO
    with pytest.raises(TypeError):
        _ = zero <= ZERO


def test_addition() -> None:
    """Test addition"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert zero + zero == zero
    assert one + zero == one
    assert one + minus_one == zero
    with pytest.raises(TypeError):
        _ = zero + ZERO


def test_subtraction() -> None:
    """Test subtraction"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert zero - zero == zero
    assert one - zero == one
    assert zero - one == minus_one
    with pytest.raises(TypeError):
        _ = zero - ZERO


def test_multiplication() -> None:
    """Test multiplication"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert zero * zero == zero
    assert zero * one == zero
    assert minus_one * one == minus_one
    assert minus_one * minus_one == one
    with pytest.raises(TypeError):
        _ = zero * ZERO


def test_int() -> None:
    """Test __int__"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert int(zero) == 0
    assert int(one) == 1
    assert int(minus_one) == -1
