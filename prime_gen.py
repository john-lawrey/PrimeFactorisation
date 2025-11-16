"""Prime Generation

Allows for the generation of large primes.

Created by John Lawrey on 11.11.2025."""

# Imports.
from miller_rabin import is_probable_prime
import random


def next_prime(n):
    """Returns the next prime number sequentially after
    a given integer n, including n if n is prime. """

    while not is_probable_prime(n):
        n += 1
    return n


def random_prime(bits=1024, seed=None):
    """Returns a random prime number with the
    provided number of bits."""
    if bits <= 1:
        raise ValueError("No prime numbers of the provided bit length.")
    if seed is not None:
        random.seed(seed)
    n = random.randint(2**(bits-1), 2**bits - 1)
    while not is_probable_prime(n):
        n = random.randint(2**(bits-1), 2**bits - 1)
    return n
