def hop():
    """
    Calling hop returns a curried version of the function f(x, y) = y.
    >>> hop()(3)(2) # .Case 1
    2
    >>> hop()(3)(7) # .Case 2
    7
    >>> hop()(4)(7) # .Case 3
    7
    """
    def hop2(x):
        def hop1(y):
            return y
        return hop1
    return hop2
