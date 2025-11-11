"""Contains test cases for functions in miller_rabin.py.

Uses pytest for testing. Run tests using 'py -m pytest'

Created by John Lawrey on 11.11.2025."""

# Imports.
from miller_rabin import miller_rabin, generate_basis, is_probable_prime


def large_prime_tests():
    """Contains the large testcases for prime numbers."""
    # 30 digits
    assert is_probable_prime(510902330142512522077310659609)
    assert is_probable_prime(704631141184628849919142099133)
    assert is_probable_prime(154162574860897731673992064837)
    assert is_probable_prime(952708424608300719763020534539)
    assert is_probable_prime(125551492358065600642515859361)
    # 60 digits
    assert is_probable_prime(127636969271454630736132651556332243228732933089851329644463)
    assert is_probable_prime(209053129835265828558508012082991132066138948938769568543697)
    assert is_probable_prime(702718149459886849260296714204423455250561538139186304085491)
    assert is_probable_prime(537252962238275889054108639564449518712498593880535427035829)
    assert is_probable_prime(982428109253227301217193509931489869967897464954227944886051)


def large_composite_tests():
    """Cotains the large testcases for composite numbers."""
    assert not is_probable_prime(582052000981719653423658521159)
    assert not is_probable_prime(493484159746857946856560211479)
    assert not is_probable_prime(916179557547975758944421390521)


def test_miller_rabin():
    """Contains testcases for the miller_rabin function from miller_rabin."""
    assert miller_rabin(1, [2]) is False
    assert miller_rabin(3, [2]) is True
    assert miller_rabin(20, [2]) is False
    assert miller_rabin(19683, [2, 3]) is False
    assert miller_rabin(142389539721, [2, 3, 5, 7, 11, 13, 17]) is False
    assert is_probable_prime(142389539721) is False
    assert is_probable_prime(7589*7417) is False
    large_prime_tests()

    # Test reliability.
    for _ in range(1000):
        assert not is_probable_prime(4)


def test_generate_basis():
    """Contains testcases for the generate_basis function from miller_rabin."""
    for n in range(100):
        assert len(list(generate_basis(basis_size=n))) == n
    assert next(generate_basis(bits=8)) < 2**8


if __name__ == "__main__":
    test_miller_rabin()
