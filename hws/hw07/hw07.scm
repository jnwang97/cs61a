(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign num)
  (cond ((< 0 num) 1)
        ((= 0 num) 0)
        ((> 0 num) -1))
)


(define (square x) (* x x))

(define (pow x y)
    (if (= y 1)
        x
        (if (even? y)
            (square (pow x (/ y 2)))
            (* x (square (pow x (/ (- y 1) 2))))))
)


(define (unique s)
    (if (equal? s nil)
        nil
        (cons (car s) (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)


(define (replicate x n)
  (define (replicate-tail x n sublist)
      (if (= n 0)
          sublist
          (replicate-tail x (- n 1) (append sublist (list x)))))
    (replicate-tail x n nil)
  )


(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term)))
)


(define (accumulate-tail combiner start n term)
  (define (tail-accumulate combiner start n term result)
      (if (= n 0)
          result
          (tail-accumulate combiner start (- n 1) term (combiner result (term n)))))
    (tail-accumulate combiner start n term start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

