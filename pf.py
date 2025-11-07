"""(integer) prime factorisation

Outputs the prime factors of a set of positive integers. Accepts integers
on separate lines from standard input. Use redirection to process files
(i.e., 'Get-Content infile | python pf.py > outfile' for Powershell).

Created by John Lawrey on 7.11.2025."""

# Imports.
import sys
import argparse
import time  # Used for setting maximum computation time.


def pfactors(candidate: int, timelimit: float = float('inf')):
    """Yields tuples of the form (prime, exponent) for each prime factor of
    candidate as it finds them. If computation is ended early
    it will yield (remainder, 1) as the final tuple.

    Candidate: a positive integer to be factored."""

    stime = time.time()
    remainder = candidate
    # Trial Division.
    divisor = 2
    while divisor * divisor <= remainder:  # math.sqrt would be inefficient.
        exp = 0
        while remainder % divisor == 0:
            exp += 1
            remainder //= divisor
        if exp > 0:
            yield (divisor, exp)
        divisor += 1

        # Check time limit.
        if time.time() - stime > timelimit:
            break

    if remainder != 1:
        yield (remainder, 1)


def main():
    """Reads lines of integers from standard input and outputs the factored
    form of each one.

    Optional arguments:
        --timelimit: places a limit of x seconds on
        computation time for factorisation.

    When entering integers via the terminal use an EOF signal to terminate.

    Raises a TypeError if it encounters a non-integer."""

    # Argument parsing.
    parser = argparse.ArgumentParser()
    parser.add_argument('--timelimit', type=float, default=float('inf'),
                        help="Time limit in seconds")
    args = parser.parse_args()

    # Input processing.
    lines = sys.stdin.readlines()
    for line in lines:
        val = line.strip('\n')
        if not val.isdigit():
            raise TypeError("Input must be a positive integer (e.g., '34')")
        int_val = int(val)
        # Output generation.
        for factor, exponent in pfactors(int_val, args.timelimit):
            print(f"{factor}^{exponent}, ", end="")
        print()


if __name__ == "__main__":
    main()
