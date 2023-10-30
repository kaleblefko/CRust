@0
D = A // D <- 0
@18 // c
M = D // c <- 0
(LOOP)
@17 // b
D = M; // D <- b
@END
D; JLE // if B <= 0, goto END
@16 // a
D = M // D <- a
@18 // c
M = M+D // c <- c + a
@17 // b
M = M - 1 // b <- b-1
@LOOP
0;JMP // loop again, goto LOOP
(END)
@END
0;JMP
