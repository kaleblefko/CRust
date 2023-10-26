@13
D = A // D <- A
@16 // a
M = D // a <- D
@2
D = A // D <- A
@17 // b
M = D // b <- D
@0
D = A // D <- 0
@18 // q
M = D // q <- 0
@16
D = M // D <- a
@19 // r
M = D // r <- a 
(LOOP)
@19 // r
D = M // D <- r
@17 // b
D = D - M // D <- r-b
@END
D; JLT // if r-b < 0, goto END
@18 // q
M = M + 1// q <- q+1
@17 // b
D = M
@19 // b
M = M - D // r <- r - b
@LOOP
0;JMP // loop again, goto LOOP
(END)
@END
0;JMP