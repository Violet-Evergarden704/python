# Lec21 Programs as Data
## Programs as Data
### A Scheme Expression is a Scheme List
The built in Scheme data structure can present any Scheme expression.
The built-in procedure `eval` can take in a Scheme list and evaluate the Scheme expression.

In Python `eval` takes a string and evaluate it.
While in Scheme, it is straightforward to write a program that writes a program.
```scheme
(define (fact n)
    (if (= n 0) 1 
        (* n (fact (- n 1)))))
; This is a normal version computing factorial.
(define (fact-exp n)
    (if (= n 0) 1
        (list '* n (list 'fact-exp (- n 1)))))
; In this case, we can use eval to evaluate the expression.
; This is a procedure that returns an expression instead of number.
(eval (fact-exp 5))
; The result is 120.
```

## Generating Code
### Quasiquotation
Quote: '(a b) $\Rightarrow$ (a b)
Quasiquote: `(a b) $\Rightarrow$ (a b)
Parts of a quasiquote can be unquoted using `,` symbol.
```scheme
(define b 4)
'(a ,(+ b 1)) $\Rightarrow$ (a (unquote (+ b 1)))
`(a ,(+ b 1)) $\Rightarrow$ (a 5) ; unquote mark is used, b+1 is evaluated and resulting in 5 in place.
```
Quasiquotatiion is convenient for generating expressions:
```scheme
(define (make-adder n)
    `(lambda (x) (+ x ,n)))

(make-adder 5)
; The result is (lambda (x) (+ x 5))
```