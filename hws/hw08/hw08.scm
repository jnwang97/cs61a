(define (rle s)
  (if (null? s)
    nil
    (rle-num s (car s) 0))
)

(define (rle-num s num count)
    (if (null? s)
      (if (= count 0)
        nil
        (cons-stream (list num count) nil))
      (if (= (car s) num)
        (rle-num (cdr-stream s) num (+ count 1))
        (cons-stream (list num count) (rle-num s (car s) 0))))
  )

(define (group-by-nondecreasing s)
  (if (null? s)
    nil
    (if (or (null? (cdr-stream s)) (> (car s) (car (cdr-stream s))))
      (cons-stream (list (car s)) (group-by-nondecreasing (cdr-stream s)))
      (cons-stream (cons (car s) (car (group-by-nondecreasing (cdr-stream s)))) (cdr-stream (group-by-nondecreasing (cdr-stream s))))))
  )


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

