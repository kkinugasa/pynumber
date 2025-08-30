"""Set-theoretic construction of numbers"""

# Explicit re-exports for public API (sorted)
from pynumber._version import __version__ as __version__
from pynumber.integer import Integer as Integer
from pynumber.integer import create_integer_from_int as create_integer_from_int
from pynumber.natural import Natural as Natural
from pynumber.natural import create_natural_from_int as create_natural_from_int
from pynumber.rational import Rational as Rational

__all__ = [
    "__version__",
    "Natural",
    "create_natural_from_int",
    "Integer",
    "create_integer_from_int",
    "Rational",
]
