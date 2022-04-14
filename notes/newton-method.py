'''An Example to use improve iteration method

To calculate n-th root of a
Use Newton iteration method
'''

def improve(update, close, guess: float = 1) -> float:
    while not (close(guess)):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-3) -> bool:
    return abs(x - y) < tolerance

def newton(f, df) -> float:
    '''get the zero point of f(x) by newton method
    
    f: function
    df: derivative of f
    '''
    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def power(x: float, n: int) -> float:
    '''get x^n
    
    n: non-negative integer
    >>> power(3, 3)
    27
    >>> power(2, 10)
    1024
    '''
    product, k = 1, 0
    while (k < n):
        product, k = product * x, k + 1
    return product

def nth_root(n: int, a: float) -> float:
    '''get a^{1/n}
    
    n: positive integer
    >>> approx_eq(nth_root(1, 64), 64)
    True
    >>> approx_eq(nth_root(2, 64), 8)
    True
    >>> approx_eq(nth_root(3, 64), 4)
    True
    >>> approx_eq(nth_root(6, 64), 2)
    True
    '''
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return newton(f, df)

if __name__ == '__main__':
    import doctest
    doctest.testmod()