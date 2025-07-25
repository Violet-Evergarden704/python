# Lec4 : Environments
**Environments with High-Order Functions**
*High-order function* is a function that takes a function as an argument or returns a function as a result, or both.

Demo:
```python
def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 2)
```
In the environment diagram, the global frame contains the function `apply_twice` and `square`. 
The local frame f1: `apply_twice` contains the parameter `f` bound to the function `square` and the parameter `x` bound to the value `2`. It is to execute the body of apply_twice function.
The local frame f2: `square` contains the parameter `x` bound to the value `2`, and return value `4`.
The local frame f3: `square` contains the parameter `x` bound to the value `4`, and return value `16`.
The Global frame then contains `result` bound to the return value `16`.

**Environments for Nested Definitions**
```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_three = make_adder(3)
result = add_three(4)
```
In the environment diagram, the global frame contains the function `make_adder`.
The local frame f1: `make_adder` contains the parameter `n` bound to the value `3`, and parameter `adder` bound to function`adder`, returning the adder function.

Then the global frame generates a new `add_three` bound to the function adder.

Then when executing line7, a new local frame f2: adder is created, with parameter `k` bound to value `4`, and the parent of f2 is f1

Then execute line3, finds k in f2 and n in f1, returning the result.

The executing of line7 first looks up in f2, then f1, then global, because f2's parent is f1

Every user-defined frame has a parent frame, often the global frame.But when u have nested def, the inner def frame's parent frame will be the outer one, which calls the function.

**How to Draw an Environment Diagram**
*When a function is defined:*
Create a function value： func <name>(<formal parameters>) [parent=<parent>], its parent is the current frame
eg. frame_name:  f1: make_adder
its value: func adder(k) [parent=f1]
Then bind <name> to the function value in the current frame.

*When a function is called:*
1. Add a local frame, titled with the <name> of the function being called.
2. Copy the parent of the func to the local frame: [parent=<label>]
3. Bind the <formal parameters> to the actual arguments in the local frame
4. Execute the body of the function in the environment that starts with the local frame.
When we need to find the value of a name, follow the order of parent -> parent -> parent... in the environment until we find the name.

**Local Names**
```python
def f(x, y):
    return g(x)

def g(a):
    return a + y

result = f(1, 2)
```
This would cause an error, because `y` is not defined in the local frame of `g`.
Take a look in the environment diagram:
In the global frame there's f bound to func f(x,y) and g bound to func g(a).
In local frame f, x is bound to 1, y is bound to 2.
In local frame g, a is bound to 1, but y is not found.
Although y is in frame f, it is not the current environment, and it is not nested, so we can't find y in the current frame.


**Function Composition**
```python
def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
```

In the environment diagram, local frame f4: `compose1` contains the parameter `f` bound to the function `square` and the parameter `g` bound to the function `triple`.

**Lambda Expressions**
```python
square = lambda x: x * x
```
to bind name to a new, never defined function
```python
square = x * x #evaluates to a value
square = lambda x: x * x #evaluates to a function
```
This is a lambda expression
lambda <formal parameter> : <expression>
No return key word in lambda expression, and the expression must be a simple expression

Only def statement gives the function an intrinsic name, when we look up square in the frames, the interpreter will tell us square is a lambda function, but using def is different
In the environment diagram, square is bound to func $\lambda (x)$, and create a local frame called f1:$\lambda (x)$ when the square function is called

**Environment Diagram with Lambda**
A lambda function's parent frame is the current frame in which the lambda function is evaluated
```python
a = 1
def f(g):
    a = 2
    return lambda y: a * g(y)
f(lambda y: a + y)(a)
```
*Which a is used in these places?*
In line5, the lambda function is in the global frame, so the `a` will be global, as `1`.And (a) is `1` as well
And in line4, this lambda expression is in def statement, so its parent would be the def frame, meaning `a` is `2`.

In the environment diagram, we first dram global frame which contains `a` bound to value `1`
Then we create local frame f1: `f` which contains `a` bound to value `2`, and return value bound to a lambda expression $\lambda (x)<line 4>$
Then we create local frame f2: $\lambda (x)<line 4>$ which contains parameter `y` bound to value `1`, and its parent is f1, with a return value.
Then we create local frame f3: $\lambda (x)<line 5>$ which contains parameter `y` bound to value `2`, with a return value `2`.
With f3 return value, we can get f2 return value as the result`4`

**Function Currying**
```python
def make_adder(n):
    return lambda x: x + n
```
make_adder(2)(3) has the same effect as add(2, 3)
```python
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
m = curry2(add)
```
m(2)(3) has the same effect as add(2, 3)
```python
curry2 = lambda f: lambda x: lambda y: f(x, y)
```
Currying: transform a function that takes multiple arguments into a function that takes one argument and is higher-order.

**Errors and Tracebacks**
SyntaxError: not obeying python rules
RuntimeError: when a program is running and something goes wrong, but it is not a syntax error.
*Traceback* : a list of frames that show where the error occurred.