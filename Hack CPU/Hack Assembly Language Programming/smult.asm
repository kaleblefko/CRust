@0
D = A // D <- 0
@18 // c
M = D // c <- 0
(POSLOOP)
@17 // b
D = M; // D <- b
@BNEGLOOP  
D; JLT // if b < 0 goto BNEGLOOP
@END
D; JLE // if B <= 0, goto END
@16 // a
D = M // D <- a
@18 // c
M = M+D // c <- c + a
@17 // b
M = M-1 // b <- b-1
@POSLOOP
0;JMP // loop again, goto POSLOOP
(BNEGLOOP)
@16 // a
D = M; // D <- a
@BOTHNEGLOOP
D; JLT // if a < 0 goto BOTHNEGLOOP
@17
D = M
@END
D; JGE // if B <= 0, goto END
@16 // a
D = M // D <- a
@18 // c
M = M-D // c <- c + a
@17 // b
M = M+1 // b <- b-1
@BNEGLOOP
0;JMP // loop again, goto LOOP
(BOTHNEGLOOP)
@17 // b
D = M; // D <- b
@END
D; JGE // if B <= 0, goto END
@16 // a
D = M // D <- a
@18 // c
M = M-D // c <- c + a
@17 // b
M = M+1 // b <- b-1
@BOTHNEGLOOP
0;JMP // loop again, goto LOOP
(END)
@END
0;JMP
