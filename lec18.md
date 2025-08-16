# Scheme Lists
## Lists
Lists in scheme is like the linked list class in python, every list is a linked list.
* cons: two-argument procedure that creates a linked list
* car: returns the first element of a list
* cdr: returns the rest of the list
* nil: empty list
(cons 2 nil)
Scheme lists are written with parentheses, with elements separated by spaces.

The second argument of cons should be nil or another list, while the first can be anything.
We can use `null?` to check if a list is empty.
`list` procedure can also create a list from multiple lists.

## Symbolic Programming
Symbols normally refer to values, how do we refer to symbols?
> (define a 1), then a is the symbol and 1 is the value.
Assume that we now have a defined as 1 and b defined as 2, then we can use `cons` to create a list.
When we got the answer list, in fact there is no a and b in the list, only number 1 and 2.

**Quotation** is a way to refer to symbols directly.
> (list 'a 'b)
In this way we build a list (a b)
Actually it is short for (list (quote a) (quote b))
`quote` is a special form that can be used to refer to symbols directly.

We can also use quotes to create lists.
> '(a b c)
> (a b c)

## List Processing
`(append s t)`: list the elements of s and t, and can be called on more than 2 lists.
`(map f s)`: call a procedure f on each element of s and list the results.
`(filter f s)`: filter the elements of s that satisfy the predicate f.
`(apply f s)`: apply the procedure f to the elements of s. f is only called once, which is different from `map`.

```scheme
(define s '(1 2))
(append s s)
; (1 2 1 2)
(list s s)
; ((1 2) (1 2))
(apply + '(1 2 3 4))
; 10
(map + '(1 2 3 4))
; (1 2 3 4), same as list((+ 1) (+ 2) (+ 3) (+ 4))
```

## Example: Even Subsets
A non-empty subset of s list s is a list containing some elements of s and remain the order of s. It can contain all of them, but not none of them.
TODO: implement procedure even-subsets which returns all subsets of s with even sum.

A recursive approach: The even-subsets of s includes:
* all even-subsets of (cdr s)
* the first element of s followed by an (even/odd) subset of (cdr s)
* just the first element of s if it is even

```scheme
(define (even-subsets s)
  (if (null? s) nil ; base case: empty list
      (append (even-subsets (cdr s))
      (map (lambda (x) (cons (car s) x))
      (if (even? (car s))
          (even-subsets (cdr s))
          (odd-subsets (cdr s))))
          (if (even? (car s))
              (list (list (car s)))
              nil))))


(define (odd-subsets s)
  (if (null? s) nil ; base case: empty list
      (append (odd-subsets (cdr s))
      (map (lambda (x) (cons (car s) x))
      (if (odd? (car s))
          (odd-subsets (cdr s))
          (even-subsets (cdr s))))
          (if (odd? (car s))
              (list (list (car s)))
              nil))))
