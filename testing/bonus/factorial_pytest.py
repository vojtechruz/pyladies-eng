import pytest

from factorial import factorial


def test_factorial():
    assert factorial(5) == 120

def test_factorial_exvpetion():
    with pytest.raises(ValueError):
        factorial(-1)

if __name__ == "__main__":
    test_factorial()