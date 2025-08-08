class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> for elem in s:
    ...     print(elem)
    5
    25
    10
    >>> m = ScaleIterator([1, 2, 3, 4, 5, 6], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        "*** YOUR CODE HERE ***"
        self.s = s
        self.iterator = iter(s) # In __init__, we create a single iterator from s and store it in self.iterator.
        self.k = k

    def __iter__(self):
        return self  # __iter__ Method: Now returns self because the class itself is the iterator (it implements __next__).

    def __next__(self):
        "*** YOUR CODE HERE ***"
        item = next(self.iterator)
        return item * self.k


def scale(it, multiplier):
    """Yield elements of the iterable it multiplied by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale([1, 2, 3, 4, 5, 6, 7, 8], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for item in it:
        yield item * multiplier


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    yield n


def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m

    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    def gener(x):
        for e in g():  # Iterate over a generator limited to x, g(x) is assumed to be a generator that produces elements up to and including x (e.g., g(3) would produce 0, 3; g(6) would produce 0, 3, 6).
            yield e     # Yield each element in this limited generator
            if e == x:  # Stop when we reach x
                return
    for e in g():       # Iterate over all elements from the original generator, g() is the original generator (e.g., every_3_ints_to_10()), which produces elements like 0, 3, 6, 9.
        yield gener(e)  # For each e, we yield a new sub-generator: gener(e).


def partial_reverse(s, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    i = start
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1



# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

