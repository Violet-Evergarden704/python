# Lec 20: Tail Calls
## Tail Recursion
**Functional Programming**
All functions are pure functions, without side effects.
No reassignment of variables and no mutable data types.
Name-value binding is permanent.
Advantages:
- The value of an expression is independent of the order of sub-expressions.
- Sub-expressions can safely be evaluated in parallel or on demand(lazily).
- **Referential transparency**: an expression can be replaced by its value without changing the program's behavior.

As there are no for/while loops allowed, we use tail recursion to make basic iteration efficient.
Reveiw how we did factorial in Python:
```python
def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iter(n):
    while n > 0:
        n, k = n - 1, n * k
    return k
```
The two ways of implementation has same order of growth, but the recursive one uses O(n) space while the iterative one uses O(1) space.
Space can be viewed as number of frames on the stack.
In functional programming, we can use tail recursion:

## Tail Calls
A procedure call that is not returned is **active**.
Some procedure calls are **tail calls**: they are the last thing to be done in a procedure.
With tail calls, as there is no extra work to do after the call returns, interpreter can reuse the current procedure's stack frame for the called procedure or needn't create a new stack frame at all, thus saving space.
We can skip keeping the many active frames on the stack, cus the last frame can directly return the value of the tail call.
A Scheme interpreter should support an unlimited number of active tail calls using only a constant amount of stack space.

A tail call is a call expression in a *tail* context.
A tail context is:
-  The last body sub-expression in a lambda expression.
-  Sub-expression 2 and 3 in a tail context `if` expression.
-  The last sub-expression in a tail context `and` or `or` expression.
-  All non-predicate sub-expressions in a tail context `cond` expression.
-  The last sub-expression in a tail context `begin` expression.
**Example:**
```scheme
(define (factorial n k)
(if (= n 0)
    k
    (factorial (- n 1) (* n k))))
```
The last body of define is an if expression, so the if expression is in a tail context.
So the expression `(factorial (- n 1) (* n k))` is in a tail context, and it is a tail call.

Example: Length of a list
Linear recursive procedures can often be rewritten to use tail calls.
```scheme
(define (length lst)
  (if (null? lst)
      0
      (+ 1 (length (cdr lst)))))
```
In this case, `(+ 1 (length (cdr lst)))` is in a tail context, but `(length (cdr lst))` is not, so this is not a tail call.
Rewrite it:
```scheme
(define (length-tail s)
    (define (length-iter s n)
    (if (null? s)
        n
        (length-iter (cdr s) (+ n 1))))
    (length-iter s 0))
```
Now `(length-iter s 0)` is in a tail context, so it is a tail call.

## Tail Recursion Examples
If one procedure runs in constant space O(1), then every recursive call in its body must be a tail call.
Examples excluded.

## Map and Reduce
### Example: Reduce
```scheme
(define (reduce procedure s start)
  (if (null? s)
      start
      (reduce procedure (cdr s)
              (procedure (car s) start))))
```
if `procedure` requires constant space, then the `reduce` procedure runs in constant space.

### Example: Map
Natural version:
```scheme
(define (map procedure s)
  (if (null? s)
      '()
      (cons (procedure (car s))
            (map procedure (cdr s)))))
```

Tail recursive version:
```scheme
(define (map-tail procedure s)
  (define (map-iter s acc)
    (if (null? s)
        acc
        (map-iter (cdr s)
                  (cons (procedure (car s)) acc))))
  (map-iter s '()))
```
