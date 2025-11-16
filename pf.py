"""(integer) prime factorisation

Outputs the prime factors of a set of positive integers. Accepts integers
on separate lines from standard input. Use redirection to process files
(i.e., 'Get-Content infile | python pf.py > outfile' for Powershell).

Created by John Lawrey on 7.11.2025."""

# Imports.
import sys
import argparse
import time


def pfactors(candidate, timelimit=float('inf')):
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


def parsing():
    """Parses the command line arguments and returns a namespace
       that can be used to get them."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--timelimit', type=float, default=float('inf'),
                        help="Time limit in seconds")
    return parser.parse_args()


def process_line(line):
    """Returns an integer if the line contains a valid integer.
       Otherwise raises a TypeError."""
    line = line.strip("\n ")

    # Allows comments with '#'.
    uncommented = line.split("#", maxsplit=1)[0]
    if uncommented == '':
        # Special case for comment lines.
        return -1
    if not uncommented.isdigit():
        raise TypeError("Input must be a positive integer (e.g., '34')")
    return int(uncommented)


def output_factors(input_lines, args):
    """Prints the factored forms of the input string to stdout."""
    for line in input_lines:
        integer = process_line(line)
        if integer == -1:  # Indicates a comment.
            continue
        for factor, exponent in pfactors(integer, args.timelimit):
            print(f"{factor}^{exponent}, ", end="")
        print()


def main():
    """Reads lines of integers from standard input and outputs the factored
    form of each one.

    Optional arguments:
        --timelimit: places a limit of x seconds on
        computation time for factorisation.

    When entering integers via the terminal use an EOF signal to terminate.

    Raises a TypeError if it encounters a non-integer. Inline Comments can be
    made using the # character."""

    args = parsing()
    output_factors(sys.stdin.readlines(), args)


if __name__ == "__main__":
    main()
