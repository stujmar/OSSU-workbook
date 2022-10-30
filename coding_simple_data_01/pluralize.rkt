;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname pluralize) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Design a function that pluralizes a given word.

; HtDF
; signature -> purpose -> stub -> example/tests -> template -> function body -> test and debug

; 1. Signature
; String -> String

; 2. Purpose
; Add an 's' to a word if it doesn't already end in 's'

; 3. Stub
; (define (pluralize str) "cats")

; 4. Example/Tests
(check-expect (pluralize "cat") "cats")
(check-expect (pluralize "dogs") "dogs")

; 5. Template
; (define (pluralize str) (... str))

; 6. Function Body
(define (pluralize string)
  (if (string=? (substring string (- (string-length string) 1)) "s")
      string
      (string-append string "s")))

(pluralize "house")
(pluralize "pines")