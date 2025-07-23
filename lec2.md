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
