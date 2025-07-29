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
Built-in data type in Python.
```python
list = [1, 2, 3, 4, 5]
print(list[0]) # 1
list[0] and getitem(list, 0) #the same effect
print(list[1:3]) # [2, 3]
print(list[1:]) # [2, 3, 4, 5]
print(list[:3]) # [1, 2, 3]
print(list[::2]) # [1, 3, 5]
len(list) # 5
```
*Example:*
```python
digits = [1, 8, 2, 8]
print([2,7] + digits * 2)
'''
>>>[2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
add & mul functions can also be used
'''
```

**Containers**
Built-in operators to test whether an element appears in another compound value

*Example:*
```python
digits = [1, 8, 2, 8]
print(8 in digits)
'''
>>>True
'''
print(5 not in digits)
'''
>>>True
'''
```

**For Statements**
*Example:*
```python
def count(s, value):
    """
    Count the number of times that value occurs in sequence s
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total
```
A better version:
```python
def count(s, value):
    total = 0
    for item in s:
        if item == value:
            total += 1
    return total
```

for <name> in <expression>:
    <suite>

*For Statement Execution Process*
1.Evaluate the header <expression>, which yields an iterable value(a sequence).
2.For each element in the sequence:
    - Bind the element to the variable <name> in the current frame.
    - Execute the <suite>.

We can also unpack pairs with for statement:
```python
pairs = [[1,2], [2, 2], [3, 4], [4, 4]]
same_count = 0 # to count how many pairs have same first and second element
for a, b in pairs:
    if a == b:
        same_count += 1
```
This unpacking looks like multiple assignment

**Ranges**
Another sequence type, representing consecutive integers.
range(-2, 2): -2, -1, 0, 1

*Length*: right value `-` left value
*Element Selection*: left value `+` index

function list(<sequence>) can return a list of the sequence
range(4): 0, 1, 2, 3 , starting at 0 by default
list(range(4)): [0, 1, 2, 3]

When we need to execute sth for n times:
```python
for _ in range(n):
    <suite>
```

**List Comprehension**
*Example:*
```python
odds = [1, 3, 5, 7, 9]
[x + 1 for x in odds]
>>> [2, 4, 6, 8, 10]
[x for x in odds if 25 % x == 0]
>>> [1, 5]
```
So we can write a devisor function:
```python
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]
```

**Slices and Recursion**
Slicing doesn't affect the original list `s`.
*Example:*
```python
def sum_list(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + sum_list(s[1:])
```

How to solve tree recursion problems using lists:
```python
def large_sum(s, n):
    """Return the sublist of s that has the largest sum that is less than or equal to n.
    """
    if s == []:
        return []
    elif s[0] > n:
        return large_sum(s[1:], n)
    else:
        first = s[0]
        with_s0 = [first] + large_sum(s[1:], n - first)
        without_s0 = large_sum(s[1:], n)
        if sum_list(with_s0) > sum_list(without_s0):
            return with_s0
        else:
            return without_s0
```
When using recursion, think about the first element, and then the rest.

**Box-and-Pointer Notation**
*Closure property for data types*:
A method for combining data types satisfies the closure property if the result of combining itself can be combined using the same method.
Closure permits us to create hierarchical data structures.
Hierarchical structures are made up of parts, which themselves are made up of parts, and so on.

List can contain other list elements.

*Box-and-Pointer Notation in Environment Diagram*
Lists are represented as a row of index-labeled adjacent boxes, one per element.
Each box contains a primitive value or a reference to a compound value.
The index in the box is the label.

**Slicing**
An operator to get the sublist of a sequence.
The same rule as ranges, include the left index but exclude the right index.
```python
odds = [1, 3, 5, 7, 9]
odds[1:4]
>>> [3, 5, 7]
```
And by slicing we create new values.

**Processing Container Values**
*Sequence Aggregation*
Some built-in func take iterable arguments and aggregate them into a value.
`sum(iterable[, start])` #[] means start is an optional parameter, which defaults to 0.
This function returns the sum of the iterable numbers(not string) plus the value of `start`.When iterable is empty, return `start`.
List can also be added.
```python
sum([2,3], [2,4])
>>> [2, 3, 2, 4]
sum([2,3], [4])
>>> TypeError: unsupported operand type for '+': 'int' and 'list'
#python tries to add 2 to [4], and it fails.
#executing sum function, python adds every element in iterable to start.
sum([2,3], [4], [])
>>> [2, 3, 4]
"""We give [] as start value, so interpreter knows we want to add 2 lists.
"""
```

`max(iterable[, key = func])` with single argument, return the largest element in the iterable.
`max(a, b, c, ...[, key = func])` with two or more arguments, return the largest argument.
```python
max(range(10))
>>> 9
max(range(10), key = lambda x: 7-(x - 4) * (x - 2))
>>> 3
```

`all(iterable)` returns True when bool(x) is True for all values x in the iterable(or if the iterable is empty).
bool(x) function: returns whether x is true of false.
```python
all([x < 5 for x in range(5)])
>>> True
all(range(5))
>>> False # Because 0 is not True
```

**String**
exec() function: execute the dynamic code.
```python
exec('print("Hello, world!")')
>>> Hello, world!
```
3 ways to create a string:
1. Using single quotes: `'Hello'`.
2. Using double quotes: `"Hello"`, in which we can use single quotes inside.
3. Using triple quotes: `'''Hello'''` or `"""..."""`, which can span multiple lines.

`\n` means a new line.

*Strings are Sequences*
```python
city = 'New York'
city[0]
>>> 'N'
city[1:3]
>>> 'ew'
city[1:]
>>> 'ew York'
len(city)
>>> 8
'here' in 'where's him'
>>> True
```
An element of a string is a string whose length is 1.

**Dictionaries**
Like hash sets, dictionaries have keys and values.
```python
numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['X']
>>> 10
numerals[0]
>>> KeyError: 0 #Dictionaries don't support indexing, we can only look up the values with the keys, and cannot look up keys with values.
list(numerals)
>>> ['I', 'V', 'X'] #Returns the list of keys.
numerals.values()
>>> dict_values([1, 5, 10]) #This is not a list, but a sequence that u can do anything u do with lists.
list(numerals.values())
>>> [1, 5, 10]
```
Values of dictionaries can also be lists or dictionaries.

2 restrictions:
1. Keys can't appear twice.
```python
numerals = {'I': 1, 'V': 5, 'X': 10, 'I': 8}
# This will overwrite the first 'I' with the second one.
>>> Error: duplicate keys in dictionary literal
```
2. Keys can't be dictionaries or lists.

*Dictionary Comprehensions*
{<key exp>: <value exp> for <name> in <iteration exp> if <filter exp>}
`exp`: expression
This is an expression that evaluates to a dictionary using the procedure:
1.Add a new frame with the current frame as its parent
2.Create an empty *result dictionary* as the value of the exp
3.For each element in <iter exp>: 
    a.Bind <name> to the element in the new frame created in Step 1
    b.If <filter exp> is true, add to the *result dictionary* an entry that pairs the value of <key exp> to the <value exp>

*Example:* {x * x: x for x in [1,2,3,4,5] if x > 2}
evaluates to {9: 3, 16: 4, 25: 5}

*Example: Indexing:*
```python
def index(keys, values, match):
    """Implement index, which takes a sequence of keys, a sequence of values, and a 2-argument func match. It returns a dictionary from keys to lists(meaning the value of dictionary is a list) in which the list for key k contains all values that match(k, v) is true.
    """
    return {k: [v for v in values if match(k, v)] for k in keys}

    index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    >>> {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
```