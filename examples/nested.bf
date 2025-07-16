++           ; cell[0] = 2
[            ; outer loop start (runs 2 times)
  > ++++     ; cell[1] += 4
  [          ; inner loop start (runs 4 times)
    > +      ; cell[2] += 1
    < -      ; cell[1] -= 1
  ]          ; inner loop end
  < -        ; cell[0] -= 1
]