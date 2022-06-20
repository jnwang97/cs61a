(define (over-or-under num1 num2)
    (if (< num1 num2)
        -1
        (if (= num1 num2)
            0
            1))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst-tail fn lst result)
    (if (equal? (cdr lst) nil)
            (if (fn result)
                (cons result nil)
                nil)
            (if (fn result)
                (cons result (filter-lst-tail fn (cdr lst) (car (cdr lst))))
                (filter-lst-tail fn (cdr lst) (car (cdr lst))))))

(define (filter-lst fn lst)
    (if (equal? lst nil)
        nil
        (filter-lst-tail fn lst (car lst))))

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (make-adder num)
  (define (adder inc) 
    (+ num inc))
  adder
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define lst
  (list (cons 1 nil) 2 (list 3 4) 5)
)


(define (composed f g)
  (define (h x)
    (f (g x)))
  h
)

(define (remove-tail item lst result)
    (if (equal? (cdr lst) nil)
        (if (= item result)
            nil
            (cons result nil))
        (if (= item result)
            (remove-tail item (cdr lst) (car (cdr lst)))
            (cons result (remove-tail item (cdr lst) (car (cdr lst)))))))

(define (remove item lst)
    (if (equal? lst nil)
        nil
        (remove-tail item lst (car lst)))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)



(define (no-repeats s)
    (if (null? s)
        s
        (cons (car s) (no-repeats (filter-lst (lambda (x) (not (= (car s) x))) (cdr s))))
  )
)


(define (substitute s old new)
    (if (equal? s nil)
        nil
        (if (pair? (car s))
            (cons (substitute (car s) old new) (substitute (cdr s) old new))
            (if (equal? (car s) old)
                (cons new (substitute (cdr s) old new))
                (cons (car s)  (substitute (cdr s) old new)))))
)


(define (sub-all s olds news)
    (if (equal? olds nil)
        s
        (if (equal? (cdr olds) nil)
            (substitute s (car olds) (car news))
            (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))) ;这里递归调用应该用sub-all而不是substitute，递归啊递归！
)

