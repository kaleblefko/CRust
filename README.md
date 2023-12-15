# CRust
This is a repository encompasing the work that went into ECE350 Computer Organization. Computer Org. utilizes a textbook from an online website called [www.nand2tetris.org](https://www.nand2tetris.org/). Nand2Tetris is a online course designed by MIT graduate students which is based off of the book The Elements of Computing Systems: Building a Modern Computer from First Principles; written by those same graduate students: Noam Nisan and Shimon Schocken.

Computer Org. is a class that is comprised of a term long project involving three major goals

# 1) The Hack Computer
The Hack CPU is a 16-bit machine comprised of a single cycle data path. This machine uses Instruction Set Architecture (ISA), and all of the components were designed from Hardware Description Language (HDL). These components functionality was then verified by tools provided by Nand2Tetris.

The Datapath (CPU) involves several components, all which were designed in HDL:
- Arithmetic Logic Unit (ALU)
  - Adder
- Memory/Registers
- Counter (Program Counter)

# 2) Assembler and Virtual Machine
The Assembler takes in a .asm file and converts it into a .hack file. These .hack files serve as machine language (or binary's) files that can be executed on the Hack Computer. The overall process of assembling follows four steps:
1. Parse each command into its underlying fields
2. For each field, generate corresponding bits in machine language
3. Resolve symbols and replace them with numeric addresses of memory locations
4. Assemble binary codes into complete machine instruction

The Virtual Machine translates .vm files into .asm files that are then fed into the assembler. The Virtual Machine is a Stack Based Machine that utilizes Stack Arithmetic to emit the proper assembly code for certain operations found in the HLL code. The Virtual Mcahine Utilizes 4 Memory Segments:
1. Static Variables
2. Constants
3. Support Function Calls (argument and local variables)
4. Support operations on the heap (this and that)

# 3) Compiler
The Compiler used three main components to take .txt files in the CRust syntax to compile and turn the raw text into a .vm file for it to then be procesesed through the previous above steps.
1. Scanner (or a lexical analyzer) to read a line of code and convert it into a list of tokens
2. Parser to fit the tokens into a grammatical model called a parse tree. That parse tree is then turned into an Abstract Syntax Tree (AST).
3. The AST is then broken down into it's corresponding VM commands and the commands are written to the output .vm file

For the sake of my project, the name of my low level language is CRust, and this repository follows the progress and components that went into creating CRust.
