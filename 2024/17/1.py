#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]

A="A"
B="B"
C="C"
PC="PC"
stdout="stdout"
debug="debug"

regs = {
    A : 0,
    B : 0,
    C : 0,
    PC : 0,
    stdout : [],
    debug : False
}

def combo(regs, operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return regs[A]
    elif operand == 5:
        return regs[B]
    elif operand == 6:
        return regs[C]
    else:
        raise("panic reserved operand value for adv")
    

def adv(regs, operand):
    value1 = regs[A]
    value2 = combo(regs, operand)
         
    value1 //= pow(2, value2)
    
    if regs[debug]:
        print("adv: %d // 2^%d == %d" % (regs[A], value2, value1))

    regs[A] = value1
    
    regs[PC] += 2

def bxl(regs, operand):
    value1 = regs[B]
    value2 = operand
    value1 = value1 ^ value2
    
    if regs[debug]:
        print("bxl: %d ^ %d == %d" % (regs[B], value2, value1))

    regs[B] = value1

    regs[PC] += 2
    
def bst(regs, operand):
    value1 = combo(regs, operand)
    value2 = value1 % 8
    regs[B] = value2
    
    if regs[debug]:
        print("bst: %d %% 8 == %d" % (value1, value2))

    regs[PC] += 2

def jnz(regs, operand):
    value1 = regs[A]

    if regs[debug]:
        print("jnz: A=%d operand %d" % (value1, operand))

    if value1 == 0:
        regs[PC] += 2
    else:
        regs[PC] = operand
    
def bxc(regs, operand):
    value1 = regs[B]
    value2 = regs[C]
    
    value1 = value1 ^ value2

    if regs[debug]:
        print("bxc: %d ^ %d == %d" % (regs[B], regs[C], value1))
    
    regs[B] = value1

    regs[PC] += 2

def out(regs, operand):
    value1 = combo(regs, operand) % 8
    regs[stdout].append("%d" % value1)
    
    if regs[debug]:
        print("out: %d" % (value1))
    
    regs[PC] += 2
       

def bdv(regs, operand):
    value1 = regs[A]
    value2 = combo(regs, operand)
         
    value1 //= pow(2, value2)
    
    if regs[debug]:
        print("bdv: %d // 2^%d == %d" % (regs[A], value2, value1))

    regs[B] = value1
    
    regs[PC] += 2
    
def cdv(regs, operand):
    value1 = regs[A]
    value2 = combo(regs, operand)
         
    value1 //= pow(2, value2)
    
    if regs[debug]:
        print("cdv: %d // 2^%d == %d" % (regs[A], value2, value1))

    regs[C] = value1
    
    regs[PC] += 2
    
opcodes = {
    0 : adv,
    1 : bxl,
    2 : bst,
    3 : jnz,
    4 : bxc,
    5 : out,
    6 : bdv,
    7 : cdv
}

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        if line.startswith("Register "):
            line = line[len("Register "):]
            reg, value = [x.strip() for x in line.split(":")]
            regs[reg] = int(value)
        elif line.startswith("Program: "):
            line = line[len("Program: "):]
            program = [int(x) for x in line.split(",")]

print("regs: ", regs)
print("program: ", program)

print("PC=%d" % regs[PC])

regs[debug] = False

while regs[PC] < len(program):
    opcode = program[regs[PC]]
    operand = program[regs[PC]+1]
    
    if regs[debug]:
        print("PC=%d opcode=%d operand=%d" % (regs[PC], opcode, operand))
        #print("regs: ", regs)
    
    func = opcodes[opcode]
    func(regs, operand) 

print(",".join(regs[stdout]))



