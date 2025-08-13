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
