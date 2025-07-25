# Lec5: Recursion
**Self-Reference**
A function can refer its own name within its body.
*Example*
```python
def print_all(x):
    print(x)
    return print_all
```
With this function, we can call `print_all(1)(2)(3)` to print 1, 2, 3.

*Another Example*
```python
def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x + y)
    return next_sum

print_sum(1)(2)(3)
```
1. `print_sum(1)` prints `1` and returns `next_sum(1 + y)`
2. `next_sum(1 + 2)` returns `print_sum(3)` and prints `3`
3. `print_sum(3)(3)` returns `print_sum(3 + 3)` and prints the sum `6`.

In the environment diagram, we can see that there're 3 print_sum frames and 2 next_sum frames.
In the print_sum frame, we can see that `x` is 1, 3, and 6, which are the sums.
In the next_sum frame, we can see that `y` is 2 and 3, which are the next number to be added.
The print_sum and next_sum frames are called recursively, serving as one another's return values and bring called back and forth.

**Recursive Functions**
A recursive function is a function that calls itself, either directly or indirectly.
*Example* : how to sum digits without using `while` or `for`
```python
def split(n):
    return n % 10, n // 10

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit, rest = split(n)
        return last_digit + sum_of_digits(rest)
```
This is a recursive function.
Conditional statement checks for *base cases*
Base cases are evaluated without `recursive calls`
Recursive cases are evaluated with `recursive calls`

**Recursion in Environment Diagrams**
*Example* :
```python
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

fact(3)
```
In the environment diagram, firstly in global frame defines a function fact and then calls it, creating a local frame.
In local frame f1: fact [parent = global], `n` is bound to `3`, since `3` is not `0`, another call of fact is generated.
In local frame f2: fact [parent = global], `n` is bound to `2`, since `2` is not `0`, another call of fact is generated.
In local frame f3: fact [parent = global], `n` is bound to `1`, since `1` is not `0`, another call of fact is generated.
In local frame f4: fact [parent = global], `n` is bound to `0`, since `0` is the base case, it returns `1`.
Then f3 returns `1 * 1 = 1`
f2 returns `2 * 1 = 2`
f1 returns `3 * 2 = 6`
So `fact(3) = 6`

The same func is called multiple times, and each call creates a new frame.
Different frames have different local variables and keep track of different arguments in each call.
What n evaluates depends on the current environment.
Each call of fact solves a subproblem of the original problem, and it's easier.

**Iteration vs Recursion**
*Iteration version* :
```python
def fact_iter(n):
    result, k = 1, 1
    while k <= n:
        result *= n
        k += 1
    return result
```
Iteration:
$$
\Pi_{i=1}^n i = n!
$$
Recursion:
$$
n! = n \times (n-1)!
$$
And recursion use less names than iteration, iteration requires 4 names: `n`, `fact_iter`, `k`, `result`, while recursion requires 2 name: `n` and `fact`.

**Verifying Recursive Functions**
Is `fact` implemented correctly?
1. Base case is correct.
2. Treat `fact` as a functional abstraction.
3. Assume `fact(n - 1)` is correct.
4. Verify that `fact(n)` is correct, assuming that `fact(n - 1)` is correct.

**Mutual Recursion**
When 2 different functions call each other, we call it *mutual recursion*.
The Luhn algorithm is a checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

1.From the rightmost digit, which is the check digit, moving left, double the value of every second digit.If the result is greater than 9, sum the digits of the result.
2. Sum all the digits.
3. If the sum is divisible by 10, the number is valid.
*Example* : 138743
   1. 4 * 2 = 8
   2. 8 * 2 = 16, sum the digits of 16 = 1 + 6 = 7
   3. 1 * 2 = 2
   4. 2 + 3 + 7 + 7 + 8 + 3 = 30
   5. 30 is divisible by 10, so 138743 is valid.

```python
    def luhn_sum(n):
        if n < 10:
            return n
        else:
            last_digit, rest = split(n)
            return last_digit + luhn_sum_double(rest)

    def luhn_sum_double(n):
        last_digit, rest = split(n)
        luhn_digit = sum_of_digits(last_digit * 2)
        if n < 10:
            return luhn_digit
        else:
            return luhn_digit + luhn_sum(rest)
```
luhn_sum calls luhn_sum_double, and luhn_sum_double calls luhn_sum.
luhn_some_double is to evaluate when the current digit is the every 2 digit from the last one, which is the luhn algorithm.

**Recursion and Iteration**
Converting recursive function to iteration function.
Figure out what's the base case.
Replace the recursive call with an iteration.
```python
def sum_digits_iter(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result
```
