; brainfuck print 1

++++               ; in cell 0 add 4
[                  ; loop until cell 0 = 0
    > +++++ +++++  ; move to cell 1 and add 10
    < -            ; move to cell 0 and remove 1
]
> +++++ ++++       ; add 9 to cell 1
.                  ; print cell 1
