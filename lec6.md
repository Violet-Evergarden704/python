# Lec6: Tree Recursion
**Order of Recursive Calls**
A function has to return and then execute the next line of code.
*Example: the Cascade Function*
```python
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
```
*Output:*
```
12345
1234
123
12
1
12
123
1234
12345
```
Look at the environment diagram, taking cascade(123) as an example.
In global frame, define cascade, and when cascade was called, a new frame `f1: cascade` was created, with n bound to 123.
Executing line 5, print(n), which prints 123.
Then calls cascade(12), and a new frame `f2: cascade` was created, with n bound to 12, then prints 12, and calls cascade(1).
When calling cascade(1), a new frame `f3: cascade` was created, with n bound to 1, then prints 1, and returns.
Then frame `f2` resumes, and prints 12, and returns.
Then frame `f1` resumes, and prints 123, and returns.

When a function calls itself, the rest statements won't be executed until the recursive call returns.

Another version:
```python
def cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)
```
When writing recursive functions, put base case first, and the former version has a typical structure:
1. Base case
2. Recursive case
While this version is shorter.

**Inverse Cascade**
```python
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10) # grow first, then print
shrink = lambda n: f_then_g(print, shrink, n // 10) # print first, then shrink
```
*Output:*
```
1
12
123
1234
12345
1234
123
12
1
```
function grow:
1
12
123
1234

function print:
12345

function shrink:
1234
123
12
1

**Tree Recursion**
Tree recursion happens when 1 func makes more than 1 recursive call.

*Example: Fibonacci*
```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) # more than 1 fib is called
```
Base cases: n = 0 and n = 1

Tree structure: 
```
                fib(5)
            /            \
        fib(4)           fib(3)
        /       \        /     \
    fib(3)    fib(2)  fib(2)    fib(1)
    /      \         /      \
 fib(2)    fib(1)  fib(1)    fib(0)
/       \
fib(1)  fib(0)
```
Computational process: 
1. Computes fib(3), which needs fib(1) and fib(2)
2. fib(1) returns 1, which is the first return number, then computes fib(2)
3. fib(2) needs fib(0) and fib(1), getting 0 and 1 respectively and return 1 as fib(2), then adds up to get fib(3) as 2

Similarly, we get fib(4) as 3.

Left branches first, then right branches, last roots.

```python
from ucb import trace

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
```
With trace, we can see the process interpreter executes.
And with trace we can know that fib needs a long time to compute great n and there're a lot of repeated calculations.
For example, when we're calculating fib(5), we calculates fib(3) twice, since we need it for fib(4) as well.

To avoid this, we can use *memoization*.

**Example: Counting Partitions**
The number of partitions of a positive integer n, using parts up to size m, is the number of ways in which n can be expressed as the sum of positive integers not greater than m in increasing order.

*Example: count_partitions(6, 4)*
```
2 + 4 = 6
3 + 3 = 6
1 + 1 + 4 = 6
1 + 2 + 3 = 6
1 + 1 + 1 + 3 = 6
2 + 2 + 2 = 6
1 + 1 + 2 + 2 = 6
1 + 1 + 1 + 1 + 1 + 2 = 6
1 + 1 + 1 + 1 + 1 + 1 + 1 = 6
```
No `1 + 5 = 6 `because size is 4, and 5 is not allowed.

So count_partitions(6, 4) = 9

*But how to compute?*
Recursive decomposition: finding simpler instances
Explore two probabilities:
* Use at least one `4`
* Don't use any `4`

Therefore we only need to solve 2 simpler problems:
* `count_partitions(2, 4)`
* `count_partitions(6, 3)`

And further decompose `count_partitions(6, 3)`

```python
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m # two cases, whether we have used 1 m or not
```