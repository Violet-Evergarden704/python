# Lec10: Iterators and Generators
## Iterators
A container can provide an iterator that provides access to its elements.
`iter(iterable)`: Returns an iterator over the elements of an iterable value
`next(iterator)`: Returns the next element from the iterator
We can view the iterator as a pointer. Once we call `next`, the pointer advances.
```python
s = [3, 4, 5]
it = iter(s)
print(next(it))  # 3
print(next(it))  # 4
u = iter(s)
print(next(u))  # 3
```
u and it are 2 different iterators, they act independently on same value s. When we call next(it) again, it returns 5 and points to the end of s, and calling next once more will return an error, `StopIteration`.

If we want to get elements in a list, we can call list(it), and it returns the rest elements that the iterator has yet reached in a list.

## Dictionary Iteration
An *iterable* value is any value that u can pass to the `iter` function to produce an iterator.
All iterators are mutable objects.
They mutate to next element when next is called.

A dictionary, its keys, its values and its items are all iterable.
* The order of items is the order in which they are added
* Historically, in old versions items appear in an arbitrary order.

An `item` of a dictionary is a tuple of the form (key, value).

If dict is changed when iterating, the iteration is invalid.
But if we merely change the key or value instead of adding a new one, it's okay.
We can't use old iterator if we change the structure of dict already.

## For Statements
For statements iterate over iterable values, but they can also iterate over iterator themselves.

*Example:*
```python
r = range(3, 6)
ri = iter(r)
for i in ri:
    print(i)
# 3
# 4
# 5
"""For statements also advances the iterator all the way to the end of the sequence. This is different from iterating over sequences where we can iterate again and again, like if we call for i in range(3, 6) for many times it will still work."""
for i in ri:
    print(i)  # No output, because ri is already at the end
```

## Built-In Iterator Functions
Many built-in python sequence operations return iterators that compute results *lazily*, meaning that a result is only computed when it has been requested. The interpreter gets ready to compute, but only gets to compute unless that value is going to be used.

`map(func, iterable)`: Returns an iterator that applies func to each element of the iterable. Iterate over func(x) for x in iterable.
`filter(func, iterable)`: Returns an iterator that contains only the elements of the iterable for which func(x) is true.
`zip(iterable1, iterable2)`: Returns an iterator which iterates over co-indexed (x, y) pairs
`reversed(iterable)`: Returns an iterator that iterates over the elements of the iterable in reverse order.

All these functions return an iterator, and if u wanna view the contents of an iterator, place the resulting elements into a container:
`list(iterable)`: Returns a list of all the elements of the iterable.
`tuple(iterable)`: Returns a tuple of all the elements of the iterable.
`sorted(iterable)`: Returns a sorted list of all the elements of the iterable.

*Example:*
```python
bcd = ['b', 'c', 'd']
m = map(lambda x: x.upper(), bcd)
next(m)  # 'B'
next(m)  # 'C'
next(m)  # 'D'
next(m)  # StopIteration
```
```python
def double(x):
    print('**', x, '=>', 2 * x, '**')
    return 2*x

m = map(double, [3, 5, 7])
next(m)  # ** 3 => 6 **
# 6
next(m)  # ** 5 => 10 **
# 10
next(m)  # ** 7 => 14 **
# 14
"""`double` func is not applied to 3, 5, 7 immediately, but only when we ask for the next element."""

m = map(double, range(3, 7))
f = lambda y: y >= 10
t = filter(f, m) # maps can also be passed into another sequence processing func, like filter in this case.
next(t) 
"""
>>>** 3 => 6 **
>>>** 4 => 8 **
>>>** 5 => 10 ** #print function effect
10 #return value when we call next()
"""
next(t)
# ** 6 => 12 **
# 12

list(filter(f, m)) # If we use list function, it will run exhausted until it reaches the end, execute print functions and then return [10, 12]
```

Need to mention that as these functions return iterators, doing comparison between iterators and sequences will return false.
```python
t = [1, 2, 3, 2, 1]
it = reversed(t)
it == t
>>>False
list(it) == t
>>>True
```

## Zip
