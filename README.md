# CRust
This is a repository encompasing the work that went into ECE350 Computer Organization. Computer Org. utilizes a textbook from an online website called [www.nand2tetris.org](https://www.nand2tetris.org/). Nand2Tetris is a online course designed by MIT graduate students which is based off of the book The Elements of Computing Systems: Building a Modern Computer from First Principles; written by those same graduate students: Noam Nisan and Shimon Schocken.

Computer Org. is a class that is comprised of a term long project involving three major goals

# 1) The Hack Computer
The Hack CPU is a 16-bit machine comrpised of a single cycle data path. This machine uses Instruction Set Architecture (ISA), and all of the components were designed from Hardware Description Language (HDL). These components functionality was then verified by tools provided by Nand2Tetris.

The Datapath (CPU) involves several components, all which were designed in HDL:
- Arithmetic Logic Unit (ALU)
  - Adder
- Memory/Registers
- Counter (Program Counter)

# 2) Assembler
The Assembler takes in a .asm file and converts it into a .hack file. .hack files serve as machine language (or binary's) files that can be executed on the Hack Computer. The overall process of assembling follows four steps:
1. Parse each command into its underlying fields
2. For each field, generate corresponding bits in machine language
3. Resolve symbols and replace them with numeric addresses of memory locations
4. Assemble binary codes into complete machine instruction

# 3) Compiler
Finally, a compiler was made for our own low level language which converts the low level language into assembly to be processed into Machine Code for the Hack CPU to use.

For the sake of my project, the name of my low level language is CRust, and this repository follows the progress and components that went into creating CRust.

For now some sections of this README will remain empty, however, this repository is living and will be updated as progress is made.
