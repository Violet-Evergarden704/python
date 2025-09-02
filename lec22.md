# Lec22: Macros
## Macros
A feature of scheme that allows you to define new special forms.
Macros perform code transformation.
Scheme has `define-macro` special form to define a source code transformer.
```scheme
(define-macro (twice expr)
  `(begin ,expr ,expr))
```
It evaluates the body of the macro on the given expression before evaluating it.

Evaluation procedure of a macro call expression:
1. Evaluate the operator sub-expression, which evaluates to a macro.
2. Call the macro procedure on the operand expression **before** evaluating it.
3. Evaluate the expression returned from the macro procedure.
