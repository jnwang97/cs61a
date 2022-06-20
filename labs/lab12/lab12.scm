
(define-macro (def func args body)
    `(define ,func (lambda ,args ,body)))


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) all-three-multiples))
)


(define (compose-all funcs)
  (lambda (x) 
      (if (null? funcs)
          x
          ((compose-all (cdr funcs)) ((car funcs) x))))
)


(define (partial-sums stream)
  (define (helper x stream)
    (if (null? stream) nil
        (cons-stream (+ x (car stream)) (helper (+ x (car stream)) (cdr-stream stream)))
    )
  )
  (helper 0 stream) #helper function defined
)


