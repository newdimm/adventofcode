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
    debug : 0
}

strcombo = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "A",
    5 : "B",
    6 : "C"
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
    
    if regs[debug] > 1:
        print("adv: A(%d) // 2 ^ %s(%d) == %d -> A" % (regs[A], strcombo[operand], value2, value1))

    regs[A] = value1
    
    regs[PC] += 2

def bxl(regs, operand):
    value1 = regs[B]
    value2 = operand
    value1 = value1 ^ value2
    
    if regs[debug] > 1:
        print("bxl: B(%d) ^ %d == %d -> B" % (regs[B], value2, value1))

    regs[B] = value1

    regs[PC] += 2
    
def bst(regs, operand):
    value1 = combo(regs, operand)
    value2 = value1 % 8
    regs[B] = value2
    
    if regs[debug] > 1:
        print("bst: %s(%d) %% 8 == %d -> B" % (strcombo[operand], value1, value2))

    regs[PC] += 2

def jnz(regs, operand):
    value1 = regs[A]

    if regs[debug] > 1:
        print("jnz: A=%d operand %d" % (value1, operand))

    if value1 == 0:
        regs[PC] += 2
    else:
        regs[PC] = operand
    
def bxc(regs, operand):
    value1 = regs[B]
    value2 = regs[C]
    
    value1 = value1 ^ value2

    if regs[debug] > 1:
        print("bxc: B(%d) ^ C(%d) == %d -> B" % (regs[B], regs[C], value1))
    
    regs[B] = value1

    regs[PC] += 2

def out(regs, operand):
    value1 = combo(regs, operand) % 8
    regs[stdout].append(value1)
    
    if regs[debug] > 0:
        print("out: %s %%8 == %d" % (strcombo[operand], value1))
    
    regs[PC] += 2
       

def bdv(regs, operand):
    value1 = regs[A]
    value2 = combo(regs, operand)
         
    value1 //= pow(2, value2)
    
    if regs[debug] > 1:
        print("adv: A(%d) // 2 ^ %s(%d) == %d -> B" % (regs[A], strcombo[operand], value2, value1))

    regs[B] = value1
    
    regs[PC] += 2
    
def cdv(regs, operand):
    value1 = regs[A]
    value2 = combo(regs, operand)
         
    value1 //= pow(2, value2)
    
    if regs[debug] > 1:
        print("adv: A(%d) // 2 ^ %s(%d) == %d -> C" % (regs[A], strcombo[operand], value2, value1))

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

from copy import deepcopy

original_regs = regs
regs[debug] = 0


pos = len(program) - 1

high_a_list = [(pos, 0)]

results = []

while high_a_list:
    
    pos, high_a = high_a_list.pop()
    
    print("[%d] *** %d - %s" % (pos, high_a, bin(high_a)))
    
    variants = []
    
    for low_a in range(8):
        
        new_a = (high_a << 3) + low_a
        regs[A] = new_a
        regs[stdout] = []
        regs[PC] = 0
        
        print("try A=%d == %s + %s" % (new_a,bin(high_a), bin(low_a)))

        while regs[PC] < len(program):
            opcode = program[regs[PC]]
            operand = program[regs[PC]+1]
            
            if regs[debug] > 1:
                print("PC=%d A=%d B=%d C=%d opcode=%d operand=%d" % (regs[PC], regs[A], regs[B], regs[C], opcode, operand))
            
            func = opcodes[opcode]
            func(regs, operand)
        
        #print("finished with %s and need %s" % (regs[stdout], program[pos:]))
        
        if regs[stdout][0] == program[pos]:
            print("FOUND %d" % low_a)
            variants.append(low_a)
            
    if not variants:
        print("no varaints here")
    else:
        for v in variants:
            new_a = (high_a << 3) + v
            
            if pos == 0:
                results.append(new_a)
            else:
                high_a_list.append((pos - 1, new_a))
            
    
    #ignore = input("press_enter")
    print("***************************************")
    print("***************************************")
    

print("results: ", results)
print("lowest: %d" % min(results))


# 37222278756852 - too high