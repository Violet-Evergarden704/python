# Lec 1 : Functions

**Call Expression**
add(1 + 1, 3)
the whole thing is called a *call expression*, with parenthesis
*add*: operator
*1 + 1* and *3*: operands
Process: 1.evaluate the operator and operand expressions
2. apply the function

*function* and *argument* refer to the value of *operator* and *operand* expressions
Big call expression can call small call expression and the rules remain the same, which means recursion

**Names, Assignment, and User-Defined Functions**
*import* can import functions and values

*assignment statements* can define user-defined names, and '=' is referred as assignment operator
When executing an assignment statement, Python evaluates the expression to the right of  =  **before** changing the binding to the name on the left.

*def statements* can define users' functions

**Types of Expressions**
*Primitive Expression* : numbers, strings, names
*Call Expression* : operator, operand
*Import Expression* : import functions or names

**Environment Diagrams**
Visualizes the interpreter process
each frame shows the name and its value
*Assignment statement* changes the names and values
execution rules of assignment statement:

1. evaluate the right-hand side expression
2. bind the name on the left-hand side to that value

**Defining Functions**
A powerful means of abstraction, binding names with expressions
def `<name>`(`<formal parameters>`):
    `<body>`
    return `<value>`
*Formal parameters* indicate the arguments needed for this function
*Execution process for def statements*:
1.create a function with formal parameters
2.set the body of that function
3.bind the `<name>` to the created function in the frame
the body of the function is not executed when the function is defined, but only when the function is called
*Procedure of calling a user-defined function*:
1.add a local frame, forming a new environment, and the local frame is named by the name of the function
2.bind the formal parameters to the actual arguments in the environment
3.execute the body of the function in the new environment, return value

a function's signature has all the info to create a local frame, eg. multiply(x,y) is the signature of multiply

Two kinds of functions: built-in and user-defined

**Looking up names in environment**
so far the environment is either:

* global frame
* local frame followed by the global frame

Two important things:
**An environment is a sequence of frames**
**A name evaluates to the value bound to that name in the earliest frame in the environment where that name is found**
eg., to look up some name in the body of a function, the interpreter first looks up the name in the local frame, if not found, then looks up in the global frame

another example:
from operator import mul
def square(square):
    return mul(square, square)
square(-2)
In this case, the name *square* is bound to the function *mul* in the global frame
In the local frame, there is another name *square* with the value of -2
When looking up *square*, the interpreter first looks up in the local frame, so it finds -2, then execute square function with the actual argument -2, instead of using the square function which lies in the global frame

**Print and None**
*What is None?*
None is a special value in Python, it means nothing
None is not displayed by the interpreter as the value of expression
A function that does not explicit return a value will return None

*Two kinds of functions*
Pure Functions, just return values
Non-pure functions, may have side effects, eg.print function, returns None and output as the side effect
