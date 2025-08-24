# Lec17: Scheme
## Scheme
Scheme is a Dialect of `Lisp`
`Lisp` is one of the oldest programming languages
The beauty of lisp is its simplicity

**Scheme Fundamentals**
Scheme programs consist of expressions, which can be:
* Primitive expressions: 2, 3.3, true, +, quotient,...
* Combinations: (quotient 10 3), (not true),...

Numbers are self-evaluating, and symbols are bound to values.
Call expressions include an operator inside the parenthesis and followed by 0 or more operands.

```scheme
> (quotient 10 2)
5 ; quotient names the built-in procedure for integer division, in py we call this function and in scheme we call it procedure.
> (quotient(+ 8 7) 3)
5 ; we can nest expressions
;Combinations can span multiple lines, and spacing doesn't matter, all matters is the closing parenthesis.

> (number? 3)
#t
> (number? 'a)
#f ;use procedures like this and a question mark, and will return t or f. integer, symbol, etc.
> (zero? (- 2 2))
#t
```

## Special Forms
A special form in scheme is a combination that is not a call expression.
* If expression: (if <test> <consequent> <alternative>)
(1) Evaluate the `test` expression.
(2) Evaluate either the consequent or the alternative, depending on the value of the test.

* and and or: (and <expr1> <expr2> ...) (or <expr1> <expr2> ...)
* Binding symbols: (define <symbol> <expression>)
* New procedures: (define (<name> <formal-parameters>) <body>)
```scheme
> (define (abs x)
  (if (< x 0)
    (- x)
    x))

> (abs -3)
3
```

## Lambda Expressions
Lambda expressions are a way to create anonymous procedures.
**(lambda (<formal-parameters>) <body>)**
(define plus1 (lambda (x) (+ x 1)))
equivalent to
(define (plus1 x) (+ x 1))

## More Special Forms
**Cond and Begin**
The `cond` special form behaves like if-elif-else statements in python.
```scheme
> (cond ((> x 10) (print 'big))
        ((< x 5) (print 'small))
        (else (print 'medium)))
```
A cond expression can have a value.
```scheme
> (print(cond ((> x 10) 'big)
        ((< x 5) 'small)
        (else 'medium)))
```
This has the same effect as the former one.

If we use if expression we can do the same thing, but nested ifs are not as readable as cond.
So when we have multiple elifs it's better to use cond.

The `begin` special form is used to combine expressions together.
The value of a begin special form is the value of the last expression in the begin.
```scheme
> (cond ((> x 10) (begin (print 'big) (print 'guy))
        (else (begin (print 'small)) (print 'fry))))
```
This is equivalent to the python code followed:
```python
if x > 10:
    print('big')
    print('guy')
else:
    print('small')
    print('fry')
```

**Let Expressions**
The `let` special form is used to bind symbols to values temporarily, just for 1 expression.
```scheme
(define c (let ((a 1) (b 2))
    (+ a b)))
; we define c to be the value of the let expression, which is the last expression (+ a b)
```
This is similar to the following python code:
```python
a = 1
b = 2
c = a + b
```
Yet there's a bit of a difference.
In let, the a and b are not bound permanently, but just used to compute c, and then those bindings are gone.
Like when we need to call a and b again later, in python we can do it, but in `let` we can't.

In scheme `define` is often used to create permanent things, like procedures or constant(eg. pi).

In fact, we can add multiple expressions in a let, and only the **last** expression will be the value of the let.

## Example: Sierpinski's Triangle
We can use built-in draw functions in scheme to draw pictures.
Common commands:
* (fd <distance>)
* (bk <distance>)
* (rt <angle>)
* (lt <angle>)

```scheme
(define (line) (fd 50))
(define (repeat k fn) (fn) (if (> k 1) (repeat (- k 1) fn)))
(define (triangle fn)
    (repeat 3 (lambda () (fn) (rt 120))))
(define (sierpinski d k)
    (triangle (lambda () (if (= d 1) (fd k)(leg d k)))))
(define (leg d k)
  (sierpinski (- d 1) (/ k 2))
  (penup) (fd k) (pendown))
```

Or and And expressions:
`Or`: return the first true value, or the last value if all are false.
`And`: return the first false value, or the last value if all are true.