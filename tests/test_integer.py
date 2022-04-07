"""Test Integer class"""
import pytest

from pynumber import ZERO, Integer, create_integer_from_int


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


def test_unary_arithmetic_operation() -> None:
    """Test unary arithmetic operation"""
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert -one == minus_one
    assert +one == one
    assert abs(minus_one) == one
    assert abs(one) == one


def test_int() -> None:
    """Test __int__"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert int(zero) == 0
    assert int(one) == 1
    assert int(minus_one) == -1


def test_sign() -> None:
    """Test sign"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    minus_two = Integer(ZERO, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert zero.sign == zero
    assert minus_two.sign == minus_one
    assert one.sign == one


def test_create_from_int() -> None:
    """Test create_integer_number_from_int"""
    zero = Integer(ZERO, ZERO)
    minus_one = Integer(ZERO.successor, ZERO.successor.successor)
    one = Integer(ZERO.successor, ZERO)
    assert create_integer_from_int(0) == zero
    assert create_integer_from_int(-1) == minus_one
    assert create_integer_from_int(1) == one