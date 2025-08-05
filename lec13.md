# Inheritance and Representation
## Learnt from lab
```python
s = [1, 2]
a = s
s = [3]
#what is a now?
# a is still [1, 2]
```
s is reassigned, and s is different from a now.

The append() method returns None.
```python
s = [3, 4, 5]
s.extend([s.append(9), s.append(10)])
#what will display?
# [3, 4, 5, 9, 10, None, None]
```

```python
s = [1, 2, 3]
b = s[:]
b is s
# False
```

`list.append(element)`
Adds a single element to the end of the list.

`list.extend(iterable)`
Adds all elements of an iterable to the end of the list.

`list.pop(index)`
Removes and returns the element at the specified index. By default, it removes and returns the last element of the list.
