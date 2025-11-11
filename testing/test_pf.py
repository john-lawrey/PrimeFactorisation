"""Contains test cases for functions in pf.py.

Uses pytest for testing. Run tests using 'py -m pytest'

Created by John Lawrey on 10.11.2025."""

# Imports.
from pf import pfactors

# Constants.
LARGEST_PRIME = 2 ** (136_279_841) - 1  # Technically the largest KNOWN prime.
TL = 0.1


def test_pfactors():
    """Contains testcases for the pfactors() function from pf.

        We ignore the order in which the prime factors are returned."""
    assert set(pfactors(1)) == set()
    assert set(pfactors(3)) == {(3, 1)}
    assert set(pfactors(20)) == {(2, 2), (5, 1)}
    assert set(pfactors(19683)) == {(3, 9)}
    # For larger test cases we include the timelimit.
    f_142389539721 = {(3, 2), (11, 1), (13, 1), (499, 1), (221717, 1)}
    assert set(pfactors(142389539721, timelimit=TL)) == f_142389539721
    assert set(pfactors(LARGEST_PRIME, timelimit=TL)) == {(LARGEST_PRIME, 1)}
    assert set(pfactors(7589*7417, timelimit=TL)) == {(7589, 1), (7417, 1)}

    # Further tests involving large primes will be implemented when
    # prime generation using probabilistic methods is added.


if __name__ == "__main__":
    test_pfactors()
