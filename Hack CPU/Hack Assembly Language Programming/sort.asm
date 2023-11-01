@18 // RAM[18] stores i
M = 0 // i = 0
@19 // hold continue
M = 1
@20 // stores pointer
M = 0
(OUTERLOOP)
    @19
    D = M
    @EXIT
    D;JEQ
    @18
    M = 0
    @20
    M = 0
    @19
    M = 0
    (INNERLOOP)
        @18
        D = M // D = i
        @17 // RAM[17] stores n
        D = M - D // Check for loop bound; D = i - n
        D = D - 1 
        @OUTERLOOP
        D;JEQ // If (i - n) == 0, goto EXIT
        @16 // RAM[16] stores base address of array A
        D = M
        @18
        D = D + M // Absolute address (base + index); our pointer value
        @20
        M = D // store pointer
        A = M
        D = M
        @21 // A[i]
        M = D
        @16 // RAM[16] stores base address of array A
        D = M
        @18
        D = D + M // Absolute address (base + index); our pointer value
        @20
        M = D + 1
        A = M
        D = M
        @22 // A[i+1]
        M = D
        @21 // A[i]
        D = M
        @22 // A[i+1]
        D = D - M
        @DONTSWAP
        D;JLE
        (SWAP)
            @21
            D = M
            @23 // temp
            M = D // temp = A[i]
            @16 // RAM[16] stores base address of array A
            D = M
            @18
            D = D + M // Absolute address (base + index); our pointer value
            @20
            M = D
            @22
            D = M
            @20
            A = M
            M = D
            @16 // RAM[16] stores base address of array A
            D = M
            @18
            D = D + M // Absolute address (base + index); our pointer value
            @20
            M = D + 1
            @23
            D = M
            @20
            A = M
            M = D
            @19
            M = 1
            @DONTSWAP
            0;JMP
        (DONTSWAP)
        @18
        M = M + 1
        @INNERLOOP
        0;JMP
    @OUTERLOOP
    0;JMP
(EXIT)
@EXIT
0;JMP // Terminate program