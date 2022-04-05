"""Test code of Natural class"""
import pytest

from pynumber import ZERO, Natural, create_natural_from_int


def test_equality() -> None:
    """Test __eq__ and __ne__"""
    zero = Natural(())
    one = Natural(((),))
    assert not ZERO == ()
    assert ZERO == zero
    assert one == ZERO.successor
    assert not zero == one
    assert zero != one


def test_inequality() -> None:
    """Test inequality"""
    one = Natural(((),))
    assert one >= ZERO
    assert ZERO <= ZERO
    with pytest.raises(TypeError):
        _ = ZERO < ((),)
    with pytest.raises(TypeError):
        _ = ZERO <= ((),)


def test_successor() -> None:
    """Test successor"""
    one = Natural(((),))
    two = Natural((*tuple(one), tuple(one)))
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
    with pytest.raises(TypeError):
        _ = ZERO + ()


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
    with pytest.raises(TypeError):
        _ = ZERO * ()


def test_unary_arithmetic_operation() -> None:
    """Test unary arithmetic operation"""
    one = ZERO.successor
    assert +one == one


def test_int() -> None:
    """Test __int__"""
    assert int(ZERO) == 0
    assert int(ZERO.successor) == 1


def test_create_from_int() -> None:
    """Test create_natural_number_from_int"""
    assert create_natural_from_int(0) == ZERO
    assert create_natural_from_int(1) == ZERO.successor
    with pytest.raises(ValueError):
        _ = create_natural_from_int(-1)
