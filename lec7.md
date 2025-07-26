# Lec 7: Sequences and Containers
**Learnt from lab**
In Python, the `and` operator returns the first falsy value it encounters. If all values are truthy, it returns the last value.

In Python, the `or` operator returns the first truthy value it encounters. If all values are falsy, it returns the last value.

In Python, the `not` operator returns the boolean negation of a value. It converts the value to a boolean (using truthiness rules) and then inverts it.
eg. 
```python
True and 13
>>>13

False or 0
>>>0

not 10 
>>> False

True or 1/0
>>> True 
''' 1/0 raises a ZeroDivisionError, 
but the or operator returns the first truthy value it encounters, 
which is True.'''

-1 and 1 > 0
>>> True
'''In this case, -1 is truthy, and 1 > 0 is true, and operator returns the last truthy value, which is True.
```

**Lists**
