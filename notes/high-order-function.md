# High Order Function

Def: Function which parameters can be other function's names.

eg. iteration method to find a zero-point of a certain function.

```python
def improve(update: function, close: function, guess = 1: float):
    while not (close(guess)):
        guess = update(guess)
    return guess
```
