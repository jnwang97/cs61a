(define (split-at lst n)
    (define (split lst n num)
        (if (> n (length lst))
            (list lst)
            (if (null? lst)
                nil
                (if (= n 0)
                    (cons nil lst)
                    (if (< num n)
                        (cons (cons (car lst) (car (split (cdr lst) n (+ num 1)))) (cdr (split (cdr lst) n (+ num 1))))
                        (cons (list (car lst)) (cdr lst)))))))
  (split lst n 1)
)

(define (length lst)
    (define len 0)
    (if (null? lst)
        len
        (+ 1 (length (cdr lst)))))

(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons (equal? (eval expr) (car case)) (cdr case)))
    			cases))
)

(cond (map (lambda (case) ((equal? (eval expr) (car case)) (cdr case))) cases))