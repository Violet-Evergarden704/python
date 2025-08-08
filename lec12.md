# Lec12: Objects and Attributes

## Object-Oriented Programming

Is a method for organizing programs

* Extends data abstraction
* Bundles together information and related behavior

Is a metaphor for computation using distributed state

* Each `object` has its own local state (mutation)
* Each `object` should know how to manage local state
* Interact with an object uses `methods`
* Some objects may be instances of a common `class`
* Different classes may relate to each other

A `class` defines how objects of a particular type behave.
An `object` is an instance of a class, and the class is its type.
A `method` is a function called on an object using a dot expression.

## Class Statement

We can define our own classes.
Example: Bank Account
All bank accounts have a `balance` and a `holder`.
Assuming that we have the class already, and we do this:

```python
a = Account('John')
a.holder
>>>'John'
a.balance
>>>0
```

a is an instance of class `Account`, and `holder` and `balance` are called attributes of a, which can be called by a dot expression.

All bank accounts share a `deposit` and a `withdraw` method.
They are methods of object a, and they change the balance value of a.
`balance` is not a local value but an attribute of a.

```python
class Account:
    """The init is always written in this way, is a special method name to construct a class instance, and also called a constructor method."""
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

    def deposit(self, amount): # self is the instance of class on which the method was invoked
        # a.deposit(10), in this case, self is a.
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
```

## Creating Instances

When a class is called:

1. A new instance of that class is created
2. The `__init_`_ method is called with the new object as its first arg (named `self`), along with any other arguments provided.

**Instance Attributes**
They are accessed and modified using dot expressions.
An attribute can be assigned any value, and we can use dot expressions to add new attributes to an instance.

```python
a.balance = 100
a.balance
>>>100
a.interest = 0.05
a.interest
>>>0.05
b = Account('Jane')
a.backup = b
# a.backup is an attribute of a, and it is an instance of class Account.
a.backup.balance
>>>0
```

**Object Identity**
Every object that is an instance of a user-defined class has a unique identity.
There is only one class `Account` and multiple instances of `Account` class.
Identity operator `is` test if two expressions evaluate to the same object.
Binding an object to a new name does not create a new object.

```python
c = a
c is a
>>>True
```

## Methods

All methods have access to the object via `self` parameter, so they can manipulate the object's attributes.
We don't need to pass self when we call the method.

```python
a.deposit(100)
# a.deposit(a, 100)
# a.deposit(100) is equivalent to a.deposit(a, 100)
```

## Method Calls

Dot expression is evaluated first, then the whole expression is like a call expression.
if we type a.deposit, we get a method object.

```python
a.deposit
<bound method Account.deposit at ...>
```

What does bound method mean?
The bound means that the function is bound to the instance a.
Every time we call it by default we are manipulating on account a.

```python
b = Account('Min')
f = a.deposit
f(100)
# a.deposit(a, 100)
# a.deposit(100) is equivalent to a.deposit(a, 100)
b.balance
>>>0
```

We did not change the balance of b, because f is a method bound to a.
That is, when we call a.deposit, in fact the first parameter `self` is passed with a, and not b, so we can't change b's balance.

## Attribute Lookup

To evaluate a dot expression:
`<expression>.<name>`

1. Evaluate the `<expression>` to the left of the dot, which yields the object of the dot expression.
2. `<name>` is matched against the instance attributes of that object, if an attribute with that name exists, its value is returned.
3. If not, `<name>` is looked up in the class, which yields a class attribute value.
4. Then the value is returned. If the name is bound to a function, a bound method is returned.

Using `getattr` and `hasattr`. Two built-in functions
`getattr` function takes an object and a string as arguments.
It returns the value of the attribute with the name given by the string.

```python
getattr(a, 'balance')
>>>0
```

`hasattr` function takes an object and a string as arguments.
It returns True if the object has an attribute with the name given by the string.

```python
hasattr(a, 'balance')
>>>True
```

## Class Attributes

class `<name>`:
    `<suite>`

A class statement creates a new class and binds the class to `<name>` in the first frame of the current environment.
Assignments and def statements create attributes of the class.

Class attributes are shared across all instances of the class, because they belong to the class, not the attribute.
Instances' attributes can be added at anytime, and can vary from instance to instance.

## Bound Methods

**Terminology**

* Attribute: name-value pairs, all objects have attributes
* Class: a type of objects
* Classes are objects, so they have attributes
* Method: a class attribute that is a function
* Functions are objects
* Bound method: a function that has its first parameter `self` already bound to an instance

Object + Function = Bound Method

```python
type(Account.deposit)
<class 'function'>
type(a.deposit)
<class 'method'>
```

This distinction illustrates 2 ways to call a method:

1. `<object>.<method>`
2. `<class>.<method>(<object>)`

```python
Account.deposit(tom_account, 100)
tom_account.deposit(100)
```

These 2 are equivalent.

## Attribute Assignment

Use dot expressions to affect an instance attribute or a class attribute.

```python
class Account:
    interest = 0.02
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

tom_account = Account('Tom')
```

In this case, if we type:

```python
tom_account.interest = 0.05
```

We are not changing the class attribute `interest`, but we are creating a new instance attribute `interest` for `tom_account`.

```python
Account.interest = 0.04
```

This is going to change the class attribute.
And `holder` and `balance` can be viewed as instance attributes, as they are created in the init function.
