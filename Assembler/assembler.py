# -*- coding: utf-8 -*-
"""Assembler for the Hack processor.

Author: Naga Kandasamy
Date created: August 8, 2020
Date modified: November 9, 2023

Student name(s): Kaleb Lefkowitz
Date modified: November 11, 2023
"""

import os
import sys

"""The comp field is a c1 c2 c3 c4 c5 c6"""
valid_comp_patterns = {'0':'0101010', 
                       '1':'0111111',
                       '-1':'0111010',
                       'D':'0001100',
                       'A':'0110000',
                       '!D':'0001101',
                       '!A':'0110001',
                       '-D':'0001111',
                       '-A':'0110011',
                       'D+1':'0011111',
                       'A+1':'0110111',
                       'D-1':'0001110',
                       'A-1':'0110010',
                       'D+A':'0000010',
                       'D-A':'0010011',
                       'A-D':'0000111',
                       'D&A':'0000000',
                       'D|A':'0010101',
                       'M':'1110000',
                       '!M':'1110001',
                       '-M':'1110011',
                       'M+1':'1110111',
                       'M-1':'1110010',
                       'D+M':'1000010',
                       'M+D':'1000010',
                       'D-M':'1010011',
                       'M-D':'1000111',
                       'D&M':'1000000',
                       'D|M':'1010101'
                       }

"""The dest bits are d1 d2 d3"""
valid_dest_patterns = {'null':'000',
                       'M':'001',
                       'D':'010',
                       'MD':'011',
                       'A':'100',
                       'AM':'101',
                       'AD':'110',
                       'AMD':'111'
                       }

"""The jump fields are j1 j2 j3"""
valid_jmp_patterns =  {'null':'000',
                       'JGT':'001',
                       'JEQ':'010',
                       'JGE':'011',
                       'JLT':'100',
                       'JNE':'101',
                       'JLE':'110',
                       'JMP':'111'
                       }

"""Symbol table populated with predefined symbols and RAM locations"""
symbol_table = {'SP':0,
                'LCL':1,
                'ARG':2,
                'THIS':3,
                'THAT':4,
                'R0':0,
                'R1':1,
                'R2':2,
                'R3':3,
                'R4':4,
                'R5':5,
                'R6':6,
                'R7':7,
                'R8':8,
                'R9':9,
                'R10':10,
                'R11':11,
                'R12':12,
                'R13':13,
                'R14':14,
                'R15':15,
                'SCREEN':16384,
                'KBD':24576
                }

def print_intermediate_representation(ir):
    """Print intermediate representation"""
    for i in ir:
        print()
        for key, value in i.items():
            print(key, ':', value)

        
def print_instruction_fields(s):
    """Print fields in instruction"""
    print()
    for key, value in s.items():
        print(key, ':', value)


def valid_tokens(s):
    """Return True if tokens belong to valid instruction-field patterns"""
    if s['instruction_type'] == '':
        return False
    if s['instruction_type'] == 'C_INSTRUCTION':
        if not((s['dest'] in valid_dest_patterns) and (s['comp'] in valid_comp_patterns)):
            return False
    elif s['instruction_type'] == 'J_INSTRUCTION':
        if not((s['comp'] in valid_comp_patterns) and (s['jmp'] in valid_jmp_patterns)):
            return False
    return True

def parse(command):
    # Data structure to hold the parsed fields for the command
    s = {}
    s['instruction_type'] = ''
    s['value'] = ''
    s['value_type'] = ''
    s['dest'] = ''
    s['comp'] = ''
    s['jmp'] = ''
    s['status'] = 0
      
    
    # Valid operands and operations for C-type instructions
    valid_operands = '01DMA'
    valid_operations = '+-&|'
    
    state = 0
    A_type = False
    C_type = False
    token = ''
    #Finite automota that parses command
    for char in command:
        if state == -1:
            state = -1 
        elif not(A_type) and not(C_type):
            if state == 0:
                if char == ' ':
                    state = 0
                elif char == '\n':
                    state = 0 
                elif char == '@':
                    A_type = True
                    s['instruction_type'] = 'A_INSTRUCTION'
                    state = 3
                elif char in valid_operands:
                    C_type = True
                    token = char
                    state = 9
                elif char == '(':
                    s['instruction_type'] = 'PSUEDO_INSTRUCTION'
                    s['value_type'] = 'SYMBOL'
                    state = 3
                elif char == '/':
                    state = 1
                else:
                    state = -1 
            elif state == 1:
                if char == '/':
                    state = 2
                else:
                    state = -1
            elif state == 2:
                state = 2 
            elif state == 3:
                if char.isalpha() or char.isdigit() or (char in '_.$:'):
                    s['value'] += char
                    state = 3
                elif char == '\n':
                    state = 0
                elif char == '/':
                    state = 1
            else:
                state = -1
        elif A_type:
            if state == 3:
                if char == ' ':
                    state = 3 
                elif char.isalpha():
                    s['value_type'] = 'SYMBOL'
                    token = char
                    state = 4
                elif char.isdigit():
                    s['value_type'] = 'NUMERIC'
                    token = char
                    state = 5
            elif state == 4:
                if char.isalpha() or char.isdigit() or (char in '_.$:'):
                    state = 4
                    token += char
                elif char == '\n':
                    state = 8
                elif char == ' ':
                    state = 6
            elif state == 5:
                if char.isdigit():
                    token += char
                    state = 5
                elif char == ' ':
                    state = 7
                else:
                    state = -1
            elif state == 6:
                if char == ' ':
                    state = 6
                elif char == '/':
                    state = 8
            elif state == 7:
                if char ==  ' ':
                    state = 7
                elif char == '/':
                    state = 8
                else:
                    state = -1
            elif state == 8:
                state = 8
        elif C_type:
            if state == 9:
                if char == '=':
                    s['instruction_type'] = 'C_INSTRUCTION'
                    s['dest'] = token
                    s['jmp'] = 'null'
                    state = 10
                elif char == ';':
                    s['instruction_type'] = 'J_INSTRUCTION'
                    s['comp'] = token
                    s['dest'] = 'null'
                    state = 11
                elif char == ' ':
                    state = 9
                elif char in valid_operands:
                    token += char
                    state = 9
                else:
                    state = -1
            elif state == 10:
                if (char in valid_operands) or (char in valid_operations):
                    s['comp'] += char
                    state = 10
                elif char == ' ':
                    state = 12
                else:
                    state = -1
            elif state == 11:
                if char.isalpha():
                    s['jmp'] += char
                    state = 11
                elif char ==  ' ':
                    state = 11
                elif char == '/':
                    state = 13
            elif state == 12:
                if (char in valid_operands) or (char in valid_operations):
                    s['comp'] += char
                    state = 10
                elif char == ' ':
                    state = 12
                elif char == '/':
                    state = 13
                else:
                    state = -1
            elif state == 13:
                state = 13
    if s['instruction_type'] == 'A_INSTRUCTION':
        s['value'] = token
    # Check if token is valid
    if not(valid_tokens(s)):
        return -1
    return s
   
def generate_machine_code(s):
    """Generate machine code from intermediate data structure"""
    
    machine_code = []
    
    if s['instruction_type'] == 'A_INSTRUCTION':
        machine_code += '0'
        if s['value_type'] == 'SYMBOL':
            machine_code += format(symbol_table[s['value']], 'b').zfill(15)
        else:
            machine_code += format(int(s['value']), 'b').zfill(15)
    else:
        machine_code += '111'
        machine_code += valid_comp_patterns[s['comp']]
        machine_code += valid_dest_patterns[s['dest']]
        machine_code += valid_jmp_patterns[s['jmp']]

    return ''.join(machine_code)
    

def print_machine_code(machine_code):
    """Print generated machine code"""
    
    rom_address = 0
    for code in machine_code:
        print(rom_address, ':', code)
        rom_address = rom_address + 1


def run_assembler(file_name):      
    """Pass 1: Parse the assembly code into an intermediate data structure.
    The intermediate data structure can be a list of elements, called ir, where 
    each element is a dictionary with the following structure: 
    
    s['instruction_type'] = ''
    s['value'] = ''
    s['value_type'] = ''
    s['dest'] = ''
    s['comp'] = ''
    s['jmp'] = ''
    s['status'] = 0
    
    The symbol table is also generated in this step.    
    """
    ir = []
    address = 0
    # Pass 1 of the assembler to generate the intermediate data structure
    with open(file_name, 'r') as f:
        for command in f:  
            s = parse(command)
            if s != -1:
                if (s['instruction_type'] == 'A_INSTRUCTION') or (s['instruction_type'] == 'C_INSTRUCTION') or (s['instruction_type'] == 'J_INSTRUCTION'):
                    address += 1
                else:
                    symbol_table[s['value']] = address
                ir.append(s)

    # Pass 2 of assembler to generate the machine code from the intermediate data structure
    machine_code = []
    address = 16
    for s in ir:
        if s['value_type'] == 'SYMBOL':
            if not(s['value'] in symbol_table):
                symbol_table[s['value']] = address
                address += 1
        if s['instruction_type'] != 'PSUEDO_INSTRUCTION':
            m = generate_machine_code(s)
            machine_code.append(str(m))
    return machine_code
    
  
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: Python assembler.py file-name.asm")
        print("Example: Python assembler.py mult.asm")
    else:
        print("Assembling file:", sys.argv[1])
        print()
        file_name_minus_extension, _ = os.path.splitext(sys.argv[1])
        output_file = file_name_minus_extension + '.hack'
        machine_code = run_assembler(sys.argv[1])
        if machine_code:
            print('Machine code generated successfully')
            print('Writing output to file:', output_file)
            f = open(output_file, 'w')
            for s in machine_code:
                f.write('%s\n' %s)
            f.close()
        else:
            print('Error generating machine code')
            
        

    
    
    
    
