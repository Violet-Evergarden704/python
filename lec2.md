# Lec 2: Control
**Multiple Environments**
For call expressions like square(square(3)), it creates 2 frames, naming f1 and f2.
We bind different values because we have different arguments.
So there're 3 different environments:
1. Global environment
2. f1 environment followed by the global frame
3. f2 environment followed by the global frame
Global frame has no parents and it's always the last frame in an environment
Every expression or name is evaluated in the current environment.

Names can have different meanings in different environments.
The call expression and the body of a function are evaluated in different environment.
eg.
```python
def square(square):
    return square * square
```
When we call square(4), the function name *square* is looked up in the global frame
Then look up for formal parameter *square* in the local frame first, if not found, then global frame.

**Miscellaneous Python Features**
Create a python source file, name it as *try.py* :

```python
def square(square):
    return square * square
"""
>>> square(4)
16
"""
```
To test the code, we can use doctest.
```python
python -m doctest -v try.py
```
Can test the code in *try.py*, if the result is 16, it passes, if wrong, it would throw the error.

**Conditional Statements**
Statements are executed by the interpreter to perform an action
*Compound Statement* :
<header>:
    <statement>
    <statement>
    ...
<separating header>:
    <statement>
    <statement>
    ...
This whole thing can be a statement, and a clause is like
<header>:
    <statement>
    <statement>
    ...
And the statements make up the *suite*
The first header determines a statement's type
The header of a clause controls the following suite.
def statements are compound statements.

a suite is a sequence of statements
to execute a suite means to execute the statements in order

Conditional statements:
if, elif, else
eg.
```python
def abs(x):
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
```
In this example, there're 1 statement, 3 clauses, 3 headers and 3 suites.
*Execution rule for conditional statements:*
1. Evaluate the header expression
2. If the header expression is true, execute the suite and skip the remaining suites
3. If the header expression is false, skip the suite

**Boolean Contexts**
False values in python:
* False
* None
* 0
* ''
* ...
True values in python: anything that is not a false value

**Iteration**
Mans to repeat a block of code multiple times.
*While Loop* :
```python
i, total = 0, 0
while i < 10:
    total += i
    i += 1
```
Execution rule of while statements:
1. Evaluate the header expression
2. If the header expression is true, execute the suite and go back to step 1
3. If the header expression is false, skip the suite

