#!/bin/python3

import sys
import math
 
fname = "test.txt"
debug = False
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2 and sys.argv[2] == "debug":
            debug = True

total = 0
numbers = []
commands = []

with open(fname, "rt") as f:
    y = 0
    for line in f:
        line = line.strip()

        snums = [x for x in line.split(" ") if x]

        if not snums[0][0].isdigit():
            commands = snums
        else:
            nums = [int(n) for n in snums]
            numbers.append(nums)

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a//b

def mult(a, b):
    return a*b


for i in range(len(commands)):
    func = mult
    if commands[i] == "+":
        func = add
    elif commands[i] == "/":
        func == div
    elif commands[i] == "-":
        func = sub

    result = numbers[0][i]
    nums = []
    for j in range(1, len(numbers)):
        nums.append(numbers[j][i])
        result = func(result, numbers[j][i])

    print("%s %s == %d" % (nums, commands[i], result))
    total += result
        

print(total)



