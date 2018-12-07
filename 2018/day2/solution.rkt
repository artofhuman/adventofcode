#lang racket

(define test-words
  (list "abcdef"
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


(define (part1 input)
  (*
    (length (filter-by-elem 2 input))
    (length (filter-by-elem 3 input))
  ))


;(part1 abc)


(define test-words-part2
  (list "abcde"
        "fghij"
        "klmno"
        "pqrst"
        "fguij"
        "axcye"
        "wvxyz"))

(define (common-letters id1 id2)
  (for/list ([ch1 (in-list (string->list id1))]
             [ch2 (in-list (string->list id2))]
             #:when (eq? ch1 ch2))
    ch1))

(define (differ-by-one? id1 id2)
  (= (-
       (length (string->list id1))
       (length (common-letters id1 id2)))
     1))


(common-letters "abcde" "axcye")
(common-letters "fghij" "fguij")

(differ-by-one? "abcde" "axcye")
(differ-by-one? "fghij" "fguij")

(for*/first ([id1 (in-list words)]
             [id2 (in-list words)]
            #:when (differ-by-one? id1 id2))
  (list->string (common-letters id1 id2)))
