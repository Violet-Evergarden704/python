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

Discussion 4 has many examples of recursion, refer to it if necessary.

`range(n, 1, -1)` generates numbers starting from n (inclusive) and decrementing by 1 each step, stopping before reaching 1 (so the last number in the sequence is 2).

## Inheritance
Inheritance is a method for relating multiple classes together.

A common use: Two similar classes differ in their degree of specialization.
The specified class may have the same attributes as the general class, along with some special-case behavior.
The general class is called the superclass, and the specified class is called the subclass.

```python
class <name>(<superclass>):
    <suite>
```
superclass is the class that is being inherited from.

The subclass shares the same attributes as the superclass, and can override them if necessary.

*Example: Checking Account*
```python
"""
A checking account has a lower interest rate.
When withdraw, the account holder has to pay a $1 fee.
"""
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_fee) # Use self to get withdraw_fee
```

To look up a name in a class:
1. If it is an attribute in a class, return the attribute value.
2. Otherwise, look up the name in the superclass if there is one.

## Object-Oriented Design
**Designing for Inheritance:**
* Don't repeat yourself, try to use existing code and avoid copying and pasting.
* Attributes that are overwritten are still accessible via class objects.
* Look on attributes on instances whenever possible.
* If you need to access an attribute on the superclass, use `super()`.

**Inheritance and Composition:**
What's `composition`?
When one object contains another as an attribute, it is called composition.

In object-oriented programming, we view objects as real life things.
Inheritance is best to describe `is-a` relationships.
Composition is best to describe `has-a` relationships.

*Example: Bank*
```python
class Bank:
    """A bank has a list of accounts."""
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account): # To open an account
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)
```

## Attribute Lookup Practice
Do the example followed and answer what python will display.
```python
class A:
    z = -1
    def f(self, x):
        return B(x - 1)

class B(A):
    n = 4
    def _init_(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):
    def f(self, x):
        return x

a = A() # There is no constructor in class definition of A, so no instance attributes are created and we get z in class A.
b = B(1)
b.n = 5

# What will display?

>>>C(2).n
# 4, because C(2) is a subclass of B, and B.n is 4. We only changed the value of n in b, an instance of class B.

>>>a.z == C.z
# True, they all refer to z in superclass A and they are -1

>>>a.z == b.z
# False, a.z is -1, then we are going to figure out what b.z is.

"""
For b.z:
When B(1) is called, constructor works and b.z is B(0).
Then we focus on B(0), whose z is C(1).
When C(1) is called, as there is no constructors in class C, we look for superclass B's constructor, so C(1)'s z will be self.f(1), and self is C so f is found in class C, so C(1)'s z is 1.

To sum it up, b.z is a B instance, and b.z.z is a C instance, and b.z.z.z is 1.
"""
```


## Multiple Inheritance
It's when a subclass has multiple superclasses.
*Example: Saving Account*
```python
class SavingAccount(CheckingAccount, BankAccount):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)
```
Now assume that there's a CleverBank executive who wants:
* Low interest rate of 1%
* A $1 fee for withdrawing
* A $2 fee for depositing
* A free dollar when open a new account

```python
class WantedAccount(SavingAccount, CheckingAccount):
    interest = 0.01
    withdraw_fee = 1
    deposit_fee = 2

    def __init__(self, holder):
        self.holder = holder
        self.balance = 1 # A free dollar!
```

## String Representations
An object value should behave like the kind of data that it is meant to represent.
It can produce a string representation of itself.

In py, there're 2 ways to represent an object as a string:
1. `str()`, legible to human
2. `repr()`, legible to python interpreter
The two are often the same, but not always

**The repr String of an Object**
the built-in function `repr()`
repr(object) -> string
for most types, eval(repr(object)) == object

The result of calling repr on a **value** is what python would print in the interactive shell.

**The str String of an Object**
```python
from fractions import Fraction
half = Fraction(1, 2)
repr(half)
>>> 'Fraction(1, 2)'
str(half)
>>> '1/2'
```
The result of calling str on a **value** is what python would print using the `print` function.

*Example*
```python
s = 'Hello, world!'
str(s)
>>> 'Hello, world!'
repr(s)
>>> "'Hello, world!'"
# In Python, the eval() function evaluates a string as a Python expression and returns the result of that expression.
# eval() is the opposite of repr(), so we have quotes surrounding the helloworld string.

```

## String Interpolation
String Interpolation involves evaluating a string literal that contains expressions.
Using string concatenation:
```python
name = 'John'
age = 25
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')
```
Using string interpolation:
```python
from math import pi
f'pi starts with {pi}...' # f-string, {<sub-expression>}
```

The result of evaluating an f-string is the result of str() on the sub-expression.
Operation on expression might cause side effects.

## Polymorphic Functions
A function applies to many different types of objects.
`str` and `repr` are examples of polymorphic functions.
They invoke zero argument method `__str__` and `__repr__` respectively on its arguments.
```python
half.__str__()
>>> '1/2'
```

**How to implement `repr` and `str` functions using `__repr__` and `__str__` methods?**

The behavior of `repr` is slightly more complicated than invoking `__repr__` method:
* An instance attribute called `__repr__` is ignored, only class attribute `__repr__` is used.
```python
def repr(x):
    return type(x).__repr__(x) # invoke the class attribute, and pass in x because its not a bound method.
    # we don't use x.__repr__() because we want to ignore instance attribute, and we can't bypass it by using this.
```

The behavior of `str` is similar to `repr`, except that:
* An instance attribute called `__str__` is ignored(For Consistency & Reliability).
* If no `__str__` method is found, `__repr__` is used instead. It means that by default they're the same, and if u wanna make it different, create a `__str__` attribute.

**Interfaces**
Objects pass messages to each other.
They interact by looking up attributes on each other(passing messages).

A shared message (attribute name) that elicits similar behavior from different objects is called an interface.
An interface is a set of shared messages, along with specifications of what they mean.

*Example:*
Classes that implement `__repr__` and `__str__` methods implement an interface for producing string representations.
```python
class rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d ## numerator and denominator
    
    def __repr__(self):
        return f'rational({self.n}, {self.d})'

    def __str__(self):
        return f'{self.n}/{self.d}'
```

## Special Method Names
**Special Method Names in Python**
Certain names might be special because they have built-in behaviors.
They always start with two underscores and end with two underscores `__`.
`__init__` : Method invoked automatically when an object is constructed
`__repr__` : Method invoked to produce a string representation of an object as a python expression, when the object is used in the interactive shell, it returns the result of `__repr__` method.
`__str__` : Method invoked to produce a string representation of an object
`__add__` : Method invoked to add two objects
`__bool__` : Method invoked to convert an object to a boolean value
`__float__` : Method invoked to convert an object to a floating point number

`isinstance` : Function that checks if an object is an instance of a class
`isinstance(object, class)` returns true or false.
```python
isinstance(1, int)
>>> True
isinstance(1, float)
>>> False
```

## Examples: Objects
Things to remember: Instance attributes are found before class attributes, and class attributes are inherited.