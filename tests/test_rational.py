"""Test Integer class"""
import pytest

from pynumber import Integer, Rational, create_integer_from_int


def test_new() -> None:
    """Test new"""
    Rational(Integer(), Integer().successor)
    with pytest.raises(ValueError):
        _ = Rational(Integer(), Integer())


def test_equality() -> None:
    """Test __eq__ and __ne__"""
    zero = Rational(create_integer_from_int(0), create_integer_from_int(1))
    zero2 = Rational(create_integer_from_int(0), create_integer_from_int(-1))
    two_over_four = Rational(create_integer_from_int(2), create_integer_from_int(4))
    one_over_two = Rational(create_integer_from_int(1), create_integer_from_int(2))
    assert not zero == Integer()
    assert zero == zero2
    assert two_over_four == one_over_two
    assert zero != two_over_four


def test_inequality() -> None:
    """Test inequality"""
    zero = Rational(create_integer_from_int(0), create_integer_from_int(1))
    one_over_two = Rational(create_integer_from_int(1), create_integer_from_int(2))
    minus_one_over_three = Rational(
        create_integer_from_int(1), create_integer_from_int(-3)
    )
    assert one_over_two >= zero
    assert minus_one_over_three <= zero
    with pytest.raises(TypeError):
        _ = zero < Integer()
    with pytest.raises(TypeError):
        _ = zero <= Integer()


def test_addition() -> None:
    """Test addition"""
    zero = Rational(create_integer_from_int(0), create_integer_from_int(1))
    minus_one_over_two = Rational(
        create_integer_from_int(-1), create_integer_from_int(2)
    )
    two_over_three = Rational(create_integer_from_int(2), create_integer_from_int(3))
    assert zero + zero == zero
    assert minus_one_over_two + zero == minus_one_over_two
    assert minus_one_over_two + two_over_three == Rational(
        create_integer_from_int(1), create_integer_from_int(6)
    )
    with pytest.raises(TypeError):
        _ = zero + Integer()


def test_subtraction() -> None:
    """Test subtraction"""
    zero = Rational(create_integer_from_int(0), create_integer_from_int(1))
    minus_one_over_two = Rational(
        create_integer_from_int(-1), create_integer_from_int(2)
    )
    two_over_three = Rational(create_integer_from_int(2), create_integer_from_int(3))
    assert zero - zero == zero
    assert two_over_three - zero == two_over_three
    assert zero - minus_one_over_two == Rational(
        create_integer_from_int(1), create_integer_from_int(2)
    )
    with pytest.raises(TypeError):
        _ = zero - Integer()


def test_multiplication() -> None:
    """Test multiplication"""
    zero = Rational(create_integer_from_int(0), create_integer_from_int(1))
    minus_one_over_two = Rational(
        create_integer_from_int(-1), create_integer_from_int(2)
    )
    two_over_three = Rational(create_integer_from_int(2), create_integer_from_int(3))
    assert zero * zero == zero
    assert zero * two_over_three == zero
    assert minus_one_over_two * two_over_three == Rational(
        create_integer_from_int(-1), create_integer_from_int(3)
    )
    with pytest.raises(TypeError):
        _ = zero * Integer()
