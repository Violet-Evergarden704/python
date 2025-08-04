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
`zip` returns an iterator over co-indexed tuples.
```python
list(zip([1, 2, 3], [4, 5, 6]))
# [(1, 4), (2, 5), (3, 6)]
```
If one iterable is longer than the other, the result is cut off at the length of the shorter iterable.
```python
list(zip([1, 2, 3], [4, 5, 6, 7]))
# [(1, 4), (2, 5), (3, 6)]
```
More than 2 iterables can be passed to zip.
```python
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

*Example: palindrome, which returns whether s is the same forward and backward.*
```python
def palindrome(s):
    """Return whether s is the same forward and backward."""
    #return s == reversed(s)
    #This is wrong because we're comparing an iterator and a list.
    # return list(s) == list(reversed(s)) # This is 1st way
    return all([a == b for a, b in zip(s, reversed(s))])
```

## Using Iterators
Code that processes an iterator via `next`, or iterable via `for` or `iter`, makes few assumptions about the data itself.
* Changing the data representation from a **list** to a **tuple**, **map** or **dict_keys** do not need to rewrite code.
* Others are more likely to be able to use your code.

An iterator bundles together a **sequence** and a **position** within that sequence as one **object**.
* Passing that object to other functions always retain the position, which is convenient.
* Useful for ensuring that each element of a sequence is processed only once.
* Limits the operations that are performed on the sequence to only requesting `next`.

*Example: Casino Blackjack*
Rules: Try to get close to 21 and not over.
Implement:
```python
import random

points = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

def hand_score(hand):
    """Return the total score of a hand of cards."""
    total = sum([points.get(card, int(card)) for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

def shuffle_cards(deck):
    deck = (['J', 'Q', 'K', 'A'] + list(range(2, 11))) * 4
    random.shuffle(deck)
    return iter(deck) #We create a deck and then shuffle, then return an iterator of the deck

def player_turn(up_card, cards, strategy, deck):
    while hand_score(cards) <= 21 and strategy(up_card, cards):
        cards.append(next(deck)) #strategy is a function that base on the cards player have and the up card, choose to whether get another more card. It returns bool value.

def dealer_turn(cards, deck):
    while hand_score(cards) < 17:
        cards.append(next(deck))

def blackjack(strategy, announce=print):
    """Play a hand of casino blackjack."""
    deck = shuffle_cards()

    player_cards = [next(deck)]
    up_card = next(deck)
    player_cards.append(next(deck))
    hole_card = next(deck) #dealer has 2 cards in the beginning, one face up and one face down

    player_turn(up_card, player_cards, strategy, deck)
    if hand_score(player_cards) > 21:
        announce('Player busts with', player_cards, 'against a', up_card)
        return -1

    dealer_cards = [up_card, hole_card]
    dealer_turn(dealer_cards, deck)
    if hand_score(dealer_cards) > 21:
        announce('Dealer busts with', dealer_cards)
        return 1
    else:
        announce('Player has', hand_score(player_cards), 'and dealer has', hand_score(dealer_cards))
        diff = hand_score(player_cards) - hand_score(dealer_cards)
        return max(-1, min(1, diff))# A good way to return 1 if positive, -1 if negative and 0 if 0.

def basic_strategy(up_card, cards):
    """A basic strategy for blackjack."""
    if hand_score(cards) < 11:
        return True
    if up_card in [2, 3, 4, 5, 6]:
        return False
    return hand_score(cards) <= 16

def shhh(*args):
    """To replace print function, and do nothing."""

def gamble(strategy, hands = 1000):
    return sum([blackjack(strategy, shhh) for i in range(hands)])
    """Do blackjack game 1000 times if our strategy can help us win, return the total dollars we win."""
```
By using iterator, we can implement the deck as an iterator, which means we can use `next` to get the next card, and we can avoid repetition and running out of cards.

## Generators
Generator is a special type of iterator, what's special is that it is returned by a generator function.
*Example:*
```python
def plus_minus(x):
    yield x
    yield -x
```
The difference between a generator func and a common func is that it uses `yield` to return a value, instead of `return`.
```python
t = plus_minus(3)
next(t)
# 3
next(t)
# -3
t
# <generator object plus_minus at ...>
```
A generator func can yield multiple times.
A generator is created automatically when a generator function is called, and the generator iterates over its yields.
```python
def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

list(evens(2, 10))
# [2, 4, 6, 8]
```
Only when we call `next` on the generator, it will run the code until it hits `yield`, and then it will pause and return the value.

## Generators and Iterators
**Generators can yield from Iterators**
A yield from statement yields all values from an iterator or an iterable.
```python
def a_then_b(a, b):
    """Yield all values from a then all values from b."""
    for x in a:
        yield x
    for x in b:
        yield x
```
Another version using yield from statement:
```python
def a_then_b(a, b):
    yield from a
    yield from b
```
Another example, implement countdown without using loops:
```python
def countdown(x):
    while x > 0:
        yield x
        #yield countdown(x-1)  This is wrong because we're yielding a generator object.
        yield from countdown(x-1) #Using yield from will yield everything from an iterable, so it is right.
```

Another example, get all the prefixes of a string s:
```python
def prefix(s):
    if s:
        yield from prefix(s[:-1]) # Not include the last char
        yield s #s itself would be a prefix
```
If we want to get substrings of a string, need to mention that a substring is either a prefix of s, or a prefix of substring of s.
```python
def substring(s):
    yield from prefix(s)
    yield from substring(s[1:])

list(substring('tops'))
# ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
#for the first 4, they are prefixes of 'tops'.
```

## Example: Partitions
**Yielding Partitions**
partitions are mentioned previously.
partition(n, m), using numbers not bigger than m to sum up to get n.
In previous lessons we done counting partitions, now we try list them out.
```python
def list_partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [m]
        with_m = [p + [m] for p in list_partitions(n-m, m)]
        without_m = list_partitions(n, m-1)
        return with_m + without_m + exact_match
```

What if we wanna get elements in the list as strings in format like 2 + 4?
```python
def print_partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + '+' + str(m) for p in print_partitions(n-m, m)]
        without_m = list_partitions(n, m-1)
        return with_m + without_m + exact_match
```

It would be simpler using `yield`.
```python
def yield_partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partitions(n-m, m):
            yield p + '+' + str(m)
        yield from yield_partitions(n, m-1)
```
If we want just a few partitions, not all the possibilities because there are too many, we can use `next` to get them one by one.
```python
def first_few_partitions(n, m, k):
    for i in range(k):
        print(next(yield_partitions(n, m)))
```

## Example: Iterables and Iterator
**Using Built-in Functions and Comprehensions**

**What are the indices of all elements in a list that have smallest absolute value?**
```python
def min_abs_indices(lst):
    min_abs = min(map(abs, lst))
    return [i for i in range(len(lst)) if abs(lst[i]) == min_abs]
```
Another version:
```python
def min_abs_indices(lst):
    min_abs = min(map(abs, lst))
    return list(filter(lambda x: abs(x) == min_abs, lst))
    # Use filter function to create the list
```

**What's the largest sum of 2 adjacent elements in a list?**
```python
def max_adjacent_sum(lst):
    return max([lst[i] + lst[i+1] for i in range(len(lst)-1)])
    #get all sums to create a list then use max.
```
Another version:
```python
def max_adjacent_sum(lst):
    zip(lst[:-1], lst[1:]) #Then we get a pair of 2 adjacent elements.
    return max([x + y for x, y in zip(lst[:-1], lst[1:])])
```


**Create a dictionary mapping each digit d to the list of elements in s that ends with d.**
```python
def digit_dict(s):
    """digit_dict([5, 8, 13, 21, 34, 55, 89])
    >>>{1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}
    # if any part, we're ensuring that all elements exist are those have a corresponding number in s.
    #Or we can create last_digits function to get all last digits in s, then check if d is in the last_digits list, so that the if any part can be shorter.
```

**Does every element equal to some other elements in s?(return True/False)**
```python
def all_have_equal(s):
    """For s[i], we can create a new list that doesn't include s[i], then check if s[i] is in the new list.
If it is, then return False, otherwise return True.
"""
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
    #s[:i] + s[i+1 :] represents the list without s[i].
```
Or, we can use built-in function `count`, to get the count of each element in s, then check if the min count is greater than 1.
```python
def all_have_equal(s):
    return min([s.count(x) for x in s]) > 1
```