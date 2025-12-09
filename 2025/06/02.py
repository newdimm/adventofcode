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
digits = {} 
commands = []

with open(fname, "rt") as f:
    y = 0
    for line in f:
        print(line)

        if "*" in line or "+" in line:
            commands = [x for x in line.split(" ") if x == "*" or x == "+"]
            continue

        group = -1
        isdigit = False
        for i in range(len(line)):
            if line[i].isdigit():
                if not isdigit:
                    group += 1
                    isdigit = True
                if group in digits and i in digits[group]:
                    num = digits[group][i]
                else:
                    num = 0
                num *= 10
                num += int(line[i])
                if group not in digits:
                    digits[group] = {}

                digits[group][i] = num
            else:
                isdigit = False


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a//b

def mult(a, b):
    return a*b

for group in range(len(commands)):
    func = mult
    if commands[group] == "+":
        result = 0
        func = add
    else:
        result = 1
        func = mult

    print("  %d" % result)

    for key in digits[group]:
        num = digits[group][key]
        print("   %s" % num)
        result = func(result, num)
        print("    %d" % result)

    print("%s %s == %d" % (digits[group], commands[group], result))
    total += result

print(total)



