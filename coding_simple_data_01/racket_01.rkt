;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname racket_01) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(require 2htdp/image)
(+ 1 2) ;3

(sqr 5) ;25
(sqrt 9) ;3

(sqrt (sqr 6)) ;6

"apple" ;"apple"
(string-append "hot" " " "cross" " " "buns") ;hot cross buns
(string-length "plorp") ;5

(substring "boob" 1 3) ;oo
(circle 10 "solid" "red")
(rectangle 15 15 "outline" "blue")
(text "hello" 24 "orange")

(above (circle 10 "solid" "blue") (circle 10 "solid" "red")(circle 10 "solid" "green"))
(beside (circle 10 "solid" "blue") (circle 10 "solid" "red")(circle 10 "solid" "green"))
(overlay (circle 5 "solid" "blue") (circle 10 "solid" "red")(circle 15 "solid" "green"))

(define WIDTH 400)
(define HEIGHT 600)
(define RADIUS 10)
(* WIDTH HEIGHT)
(define MY_CIRCLE (circle 10 "solid" "blue"))

; Function definitions
(define (bulb color)
  (circle RADIUS "solid" color))

(bulb "purple")

(above (bulb "red")
       (bulb "yellow")
       (bulb "green"))

(bulb (string-append "bro" "wn"))
(bulb "brown")
(circle RADIUS "solid" "brown")

; boolean values
true
false
(> WIDTH HEIGHT)
(< WIDTH HEIGHT)
(string=? "apples" "oranges")

(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 10 "solid" "blue"))

(< (image-width I1)(image-width I2))

; if expressions

(if (< (image-width I1)
       (image-height I1))
       "tall" "wide")

(if (< (image-width I2)
       (image-height I2))
       "tall" "wide")