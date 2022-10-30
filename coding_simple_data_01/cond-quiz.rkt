;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname cond-quiz) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Number -> String
;; determine if a number is negative, positive or zero
(check-expect (mag 2) "positive")
(check-expect (mag -7) "negative")
(check-expect (mag 0) "zero")


;;(define (mag x)
;;  (if (> x 0)
;;      "positive"
;;      (if (= x 0)
;;          "zero"
;;          "negative")))

(define (mag x)
  (cond [(> x 0) "positive"]
        [(= x 0) "zero"]
        [else "negative"]))