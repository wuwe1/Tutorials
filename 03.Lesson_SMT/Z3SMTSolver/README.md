# Exercise Z3

- [x] Follow the [Z3 Playground](https://jfmc.github.io/z3-play/) up to Bitvectors (don't read Bitvectors).

> :warning: Some browsers might not run the playground properly. Safari is a browser we know doesn't work well. Chrome, Chromium, Firefox, and Brave browsers have been tested to work fine.

- [ ] Use Z3 to find a solution for the following puzzle:
</br>
<img src="images/Logic_Puzzle1.png" width="350">

```scheme
(declare-const circle Int)
(declare-const square Int)
(declare-const triangle Int)
(assert (= (+ circle circle) 10))
(assert (= (+ (* circle square) square) 12))
(assert (= (- (* circle square) (* triangle circle)) circle))
(check-sat)
(get-model)

;sat
;(
;  (define-fun circle () Int
;    5)
;  (define-fun triangle () Int
;    1)
;  (define-fun square () Int
;    2)
;)
```

- [x] Write a formula to check if the following two equations are equivalent:
</br>
<img src="images/Logic_Puzzle2.png" width="350">

```scheme
(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool 
    (= (= (and p q) p) (=> p q)))
(assert (not conjecture))
(check-sat)

;unsat
```

- [x] A good additional practice will be to try and prove questions in [this file](AdditionalExerciseForSMT.pdf)

## 1. When is the experssion p=>q false? D. None of the above

```scheme
(declare-const p Bool)
(declare-const q Bool)
(push)
(define-fun conjecture () Bool 
  (=> (and (not p) (not q))
      (not (=> p q))
  )
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (and p q)
      (not (=> p q))
  )
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (and (not p) q)
      (not (=> p q))
  )
)
(assert (not conjecture))
(check-sat)
(pop)

;sat
;sat
;sat
```

## 2. Is the following expression true? A. True in all cases

```scheme
(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool 
  (=> (and p q) p)
)
(assert (not conjecture))
(check-sat)

;unsat
```

## 3. Is the following expression true? B. False in all cases

```scheme
(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool 
  (and (and p (or q (not p))) (not q))
)
(assert conjecture)
(check-sat)

;unsat
```

## 4. Is the following expression true? A. True in all cases

```scheme
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(define-fun conjecture () Bool 
  (= (and p q r) (and p q r))
)
(assert (not conjecture))
(check-sat)

;unsat
```

## 5. Is the following expression true? C. True for some cases and false for others

```scheme
(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool 
  (not (and (or (not p) q) (or p (not q))))
)

(push)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(assert conjecture)
(check-sat)
(pop)

;sat
;sat
```

## 6. Is the following expression true?  C. True for some cases and false for others

```scheme
(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool 
  (not (or (and p q) (and (not p) (not q))))
)

(push)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(assert conjecture)
(check-sat)
(pop)

;sat
;sat
```

## 7. A.B.C.D

```scheme
(declare-const p Bool)
(declare-const q Bool)

(push)
(define-fun conjecture () Bool 
  (=> (or p (not p)) 
      (or p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (and p (not p)) 
      (or p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (or (and p (not p)) (not p)) 
      (or p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (and (or (not p) p) (not p)) 
      (or p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

;unsat
;unsat
;unsat
;unsat
```

## 8. B

```scheme
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)

(push)
(define-fun conjecture () Bool 
  (=> (or p (not p)) 
      (and p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (and p (not p)) 
      (and p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (or (and p (not p)) (not p)) 
      (and p (not r)))
)
(assert (not conjecture))
(check-sat)
(pop)

(push)
(define-fun conjecture () Bool 
  (=> (and (or (not p) p) (not p)) 
      (and p (not p)))
)
(assert (not conjecture))
(check-sat)
(pop)

;sat
;unsat
;sat
;sat
```

## 9. C
```scheme
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(define-fun conjecture () Bool 
  (=> (=> p (=> q r)) (=> (=> p q) r))
)

(push)
(assert conjecture)
(check-sat)
(pop)

(push)
(assert (not conjecture))
(check-sat)
(pop)

;sat
;sat
```
## 10. A

```scheme
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(define-fun conjecture () Bool 
  (=> (=> (=> p q) r) (=> p (=> q r)))
)

(push)
(assert conjecture)
(check-sat)
(pop)

(push)
(assert (not conjecture))
(check-sat)
(pop)

;sat
;unsat
```

> :information_source: You might find the [cheat sheet](Cheat_Sheet.md) useful for the exercises and additional explanations of the Z3 principles.
