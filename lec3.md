# Lec 3: Higher-Order Functions
**Fibonacci Sequence**
```python
def fib(n):
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr
```
a better version:
```python
def fib(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr
```
it can solve the situation when $n = 0$

**Control**
let's write a function to serve as if-statement and see what's different
```python
def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    return if_(x >= 0, sqrt(x), 0)
```
Then by running this we can see that when x < 0, if does not return 0 but throw an error
This is because serving as a function, we're using a *call expression*, and call expressions don't allow u to skip evaluating a part of the call expression, so when interpreter computes the formal parameter it gets an error and exits

**Control Expressions**
*Logical Operator*
* and operator
* or operator

**Higher-Order Function**
*Assert Statement* assert <value>, <message>
<message> is optional, but the comma is needed
when value is false, it throws AssertionError: <message>

when we want to sum the first n numbers' square or cube or else, we need to create a term function
```python
def square(k):
    return pow(k, 2)

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """
    >>>summation(5,cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
```
So term is a parameter that is bound to a function

A *higher-order function* is a function that takes another function as a formal parameter

**Function as Return Values**
```python
def make_adder(n):
    """return a function that takes 1 argument k and return k + N
    >>>add_three = make_adder(3)
    >>>add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
```

When function is defined in another function, its body is bound to names in a local frame, and both parameters are available in the inner function

eg. make_adder(1)(2)
make_adder(1) is an operator, and 2 is operand
together they make up a call expression

Functions are first-class, which means they can be manipulated as *values*