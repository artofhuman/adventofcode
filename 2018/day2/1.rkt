#lang racket

(define test-words (list "abcdef"
                    "bababc"
                    "abbcde"
                    "abcccd"
                    "aabcdd"
                    "abcdee"
                    "ababab"))

(define words (file->lines "./input.txt"))

(define (frequencies lst)
  (define (insert e acc)
    (hash-set
     acc
     e
     (add1
      (hash-ref acc e 0))))
  (foldl insert (hash) lst))


(define (filter-by-elem elem lst)
  (filter
    (lambda (x)
      (member elem x))
    lst))

(define abc
   (map
    (lambda (str)
    (hash-values (frequencies (string->list str))))
  words))


(*
  (length (filter-by-elem 2 abc))
  (length (filter-by-elem 3 abc))
)
