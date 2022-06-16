import pytest
from testing.bonus.excercise_doctest import adj_sqrt


def test_adj_sqrt( ):
    for m , n in zip([4, 9, 25, 144], [2.0, 3.0, 5.0, 12.0]):
        assert  adj_sqrt(m) == n
    assert adj_sqrt(64) == 8.0
    with pytest.raises(ValueError):
        adj_sqrt(-1)


if __name__ == "__main__":
    test_adj_sqrt( )