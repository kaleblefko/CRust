@0
D = A // D <- 0
@18 // c
M = D // c <- 0
@17
D = M // for inner loop
@19 
M = D // for outer loop
@20
M = D // to keep lshift value
(OUTERLOOP)
    @19
    D = M
    @ENDOUTER
    D;JLE
    (INNERLOOP)
        @17 // b
        D = M; // D <- b
        @ENDINNER
        D; JLE // if B <= 0, goto END
        @16 // a
        D = M // D <- a
        @18 // c
        M = M+D // c <- c + a
        @17 // b
        M = M-1 // b <- b-1
        @INNERLOOP
        0;JMP // loop again, goto LOOP
    (ENDINNER)
    @19
    M=M-1
    @20
    D = M
    @17
    M = D
    @OUTERLOOP
    0;JMP
(ENDOUTER)
@ENDOUTER
0;JMP
