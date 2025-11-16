"""Miller-Rabin Probabilistic Prime Testing Method

Uses the probabilistic Miller-Rabin primality test. Pseudorandomness is used
from the random module,which makes this prime checking method unsafe
for cryptographic systems, but is sufficient for our purposes.
"""
# Imports.
import random
from math import gcd


def generate_basis(basis_size=-1, bits=5):
    """Yields random integers to be used as bases
    for a Miller-Rabin Primality Test.

    basis_size allows the size of the generated base to be configured.
    If set to -1 it will act as a infinite generator.

    A random basis should be chosen, as for
    particular bases it is possible to generate
    strong pseudoprimes that pass Miller-Rabin.
    (see F. Arnault's paper: https://www.ams.org/journals/mcom/1995-64-209/S0025-5718-1995-1260124-2/S0025-5718-1995-1260124-2.pdf)."""
    count = 0

    while count < basis_size or basis_size == -1:
        yield random.randint(2, 2**bits)
        count += 1


def miller_rabin(candidate, basis):
    """Return True if a candidate positive integer passes
    the Miller-Rabin primality test for a randomly generated
    basis, otherwise False.

    (i.e., returns whether an integer is a probable prime)."""
    # Edgecases.
    if candidate == 2:
        return True
    if candidate == 1:
        return False
    if candidate % 2 == 0:
        return False

    for base in basis:
        # Check coprimality.
        if gcd(base, candidate) != 1:
            if base >= candidate:
                continue
            else:
                return False

        probable = False
        d = candidate - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        x = pow(base, d, candidate)
        if x == 1 or x == candidate - 1:
            probable = True

        for r in range(s):
            x = pow(x, 2, candidate)
            if x == candidate - 1:
                probable = True
        if not probable:
            return False
    return True


def is_probable_prime(candidate):
    """Return True if a candidate positive integer
    is a probable prime."""
    basis = generate_basis(basis_size=15)
    return miller_rabin(candidate, basis)
