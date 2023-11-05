@0
D = A // D <- 0
@18 // c, stores result
M = D // c <- 0
@2
D=A
@20 // holds onto 2
M = D
D = M
(OUTERLOOP)
    @19 // number of times left shifting
    D = M
    @ENDOUTER
    D;JLE
    @18
    M = 0
    (INNERLOOP)
        @20 // b
        D = M; // D <- b
        @ENDINNER
        D; JLE // if B <= 0, goto END
        @16 // a
        D = M // D <- a
        @18 // c
        M = M + D // c <- c + a
        @20 // b
        M = M - 1  // b <- b-1
        @INNERLOOP
        0;JMP // loop again, goto LOOP
    (ENDINNER)
    @18
    D = M
    @16
    M = D
    @19
    M = M - 1
    @2
    D = A
    @20
    M = D
    @OUTERLOOP
    0;JMP
(ENDOUTER)
@ENDOUTER
0;JMP
