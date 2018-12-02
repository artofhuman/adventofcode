#lang racket/base

(require racket/file)

(define  (soultion filepath)
  (apply + (file->list filepath)))

(soultion "./input.txt")
