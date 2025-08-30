"""Test code of Natural class"""

import pytest

from pynumber import Natural, create_natural_from_int


def test_equality() -> None:
    """Test __eq__ and __ne__"""
    zero = Natural(())
    one = Natural(((),))
    assert not Natural() == ()
    assert Natural() == zero
    assert one == Natural().successor
    assert not zero == one
    assert zero != one


def test_inequality() -> None:
    """Test inequality"""
    one = Natural(((),))
    assert one >= Natural()
    assert Natural() <= Natural()
    with pytest.raises(TypeError):
        _ = Natural() < ((),)
    with pytest.raises(TypeError):
        _ = Natural() <= ((),)


def test_successor() -> None:
    """Test successor"""
    one = Natural(((),))
    two = Natural((*tuple(one), tuple(one)))
    assert Natural().successor == one
    assert Natural().successor.successor == two


def test_predecessor() -> None:
    """Test predecessor"""
    one = Natural().successor
    assert one.predecessor == Natural()
    with pytest.raises(ValueError):
        _ = Natural().predecessor


def test_addition() -> None:
    """Test addition"""
    one = Natural().successor
    two = one.successor
    three = two.successor
    assert Natural() + Natural() == Natural()
    assert one + Natural() == one
    assert one + two == three
    with pytest.raises(TypeError):
        _ = Natural() + ()


def test_multiplication() -> None:
    """Test multiplication"""
    one = Natural().successor
    two = one.successor
    three = two.successor
    six = three.successor.successor.successor
    assert Natural() * Natural() == Natural()
    assert Natural() * one == Natural()
    assert two * one == two
    assert two * three == six
    assert three * two == six
    with pytest.raises(TypeError):
        _ = Natural() * ()


def test_unary_arithmetic_operation() -> None:
    """Test unary arithmetic operation"""
    one = Natural().successor
    assert +one == one


def test_int() -> None:
    """Test __int__"""
    assert int(Natural()) == 0
    assert int(Natural().successor) == 1


def test_create_from_int() -> None:
    """Test create_natural_number_from_int"""
    assert create_natural_from_int(0) == Natural()
    assert create_natural_from_int(1) == Natural().successor
    with pytest.raises(ValueError):
        _ = create_natural_from_int(-1)
