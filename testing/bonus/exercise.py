"""
This is the "example" module.

The example module supplies one function, adj_sqrt().  For example,

>>> adj_sqrt(169)
13.0
"""

def adj_sqrt(a):
    """Return the sqrt of number..

    >>> [adj_sqrt(n) for n in [4, 9,25,144]]
    [2.0, 3.0, 5.0, 12.0]
    >>> adj_sqrt(64)
    8.0
    >>> adj_sqrt(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()