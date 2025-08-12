# Efficiency
## Measuring Efficiency
Focus on how long ur program takes to run.
Take fibonacci as an example.
```python
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted
# We create the function to see how many times fib is called.
```

## Memorization
Idea: remember the results computed before, to increase efficiency.
```python
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized
```
In this example, we make a mapping between the key `n` and its value `f(n)`.
It stores the previous results in the cache, and if the result is computed before, it will return the result from the cache.
`memorized` function has the same effect as `f`, except for cases when f is not a `pure function`, meaning it may cause side effects.

## Exponentiation
Goal: one more multiplication lets us double the problem size.
```python
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)
```

Another implementation:
```python
def exp2(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = exp2(b, n // 2)
        return half * half
    else:
        return b * exp2(b, n - 1)
```
This code executes much faster, especially when we double the n, we have a lot less multiplications.
