#lang racket/base

(require racket/file racket/set)

(define seq (file->list "./input.txt"))

(let ([seen (mutable-set)]
      [last-sum 0])
  (for ([i (in-cycle seq)]
        #:break (set-member? seen last-sum))
       (set-add! seen last-sum)
       (set! last-sum (+ i last-sum)))
  (print last-sum))
