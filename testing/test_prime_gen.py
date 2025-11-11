"""Contains test cases for functions in test_prime_gen.py.

Uses pytest for testing. Run tests using 'py -m pytest'

Created by John Lawrey on 11.11.2025."""

# Imports.
from prime_gen import next_prime, random_prime
import pytest


def test_next_prime():
    """Contains testcases for the next_prime function from prime_gen."""
    assert next_prime(2) == 2
    assert next_prime(3) == 3
    assert next_prime(4) == 5
    assert next_prime(20) == 23
    assert next_prime(7588) == 7589
    assert next_prime(7591) == 7591


def test_random_prime():
    """Contains testcases for the random_prime function from prime_gen."""
    assert random_prime(seed=1) != random_prime(seed=2)
    assert random_prime(bits=2) in {2, 3}
    with pytest.raises(ValueError, match="No prime numbers of the provided bit length."):
        random_prime(bits=1)
    with pytest.raises(ValueError, match="No prime numbers of the provided bit length."):
        random_prime(bits=-4)
    assert random_prime(bits=3) in {5, 7}
    assert random_prime() > 2**(1023) - 1


if __name__ == "__main__":
    test_next_prime()
