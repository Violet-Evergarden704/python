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
