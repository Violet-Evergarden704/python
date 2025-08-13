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
A **linear** recursive function like `exp1` require another big unit of time when we double n.
The **logarithmic** function like `exp2` requires only one more multiplication when we double n, and 10 more times when executing 1024*n.
Linear and Logarithmic describes the shape of curves when execute different values of n.

## Orders of Growth
The general category a function falls in regarding its time to execute, such as linear and logarithmic, is called the order of growth.
Two functions of a same category scale in the same way, with their curve roughly the same.
**Quadratic Time**
Functions that process all pairs of values in a sequence of length n require quadratic time.
```python
def overlap(a, b):
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count
```
The func compares all pairs, and its execute time depends on length n.
If we double n, we need 4 times of time to execute.
The curve is in the shape of a parabola.

**Exponential Time**
Tree-recursive functions can take exponential time, like the fib function which has yet been memorized.

**Constant Time**
When we look up a dict with a key, the time has no relation with the size of the dict.
It is a constant time operation.

All of the orders of growth reveals how time scales with input size.
They all describe a certain trend, and have certain shapes of curve.
We can use math expressions to see how time scales with input size, and whether the impact is great compared to other orders.

## Orders of Growth Notation
**Big Theta and Big O Notation for Orders of Growth**
Big Theta notation: 
Exponential growth: $\Theta(b^{n})$
Quadratic growth: $\Theta(n^{2})$
Linear growth: $\Theta(n)$
Logarithmic growth: $\Theta(log n)$
Constant growth: $\Theta(1)$
Big O notation looks the same as Big Theta notation, like $O(b^{n})$
But the two notations are different. Big O notation illustrates the most time an order of growth might take, while Big Theta describes both the least and the most time.

## Space
**The Consumption of Space**
Which environment frames do we need to keep during evaluation?
Values and frames in active environment consume memory.
Memory can be recycled.

`Active environments`: For any function calls currently being evaluated, or the parent environments of functions named in active environments.
