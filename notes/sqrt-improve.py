'''An Example to use improve iteration method

To calculate sqrt(a)
x = 1 / 2 * (a + a / x)
'''

def improve(update, close, guess: float = 1):
    while not (close(guess)):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-3):
    return abs(x - y) < tolerance

def sqrt(a):
    '''squart root of a positive real number
    
    >>> approx_eq(sqrt(1), 1)
    True
    >>> approx_eq(sqrt(3), 1.732)
    True
    >>> approx_eq(sqrt(100), 10)
    True
    '''
    def sqrt_update(x):
        return 1 / 2 * (x + a / x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
