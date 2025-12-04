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

def find_max(digits):
    print(digits)
    number = [9]*12
    level=0
    poses=[]
    while level != 12:
        digit = number[level]
        found = False
        for p in digits[digit]:
            if p not in poses and (not poses or p > poses[-1]):
                poses.append(p)
                level+=1
                if (level < 12):
                    number[level]=9
                found = True
                break
        if not found:
            if digit == 0:
                level -= 1
                number[level] -= 1
                del poses[-1]
            else:
                number[level] -= 1
    result = number[0]
    for n in number[1:]:
        result *= 10
        result += n

    return result




    number = 0
    for i in range(9, -1, -1):
        for pos in digits[i]:
            for j in range(9,-1,-1):
                for pos2 in digits[j]:
                    if pos2 > pos:
                        return i*10+j
total = 0

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        digits = []
        for i in range(10):
            digits.append([])

        pos = 0
        for d in line:
            digit = int(d)
            digits[digit].append(pos)
            pos += 1

        subres = find_max(digits)

        print(line,subres)

        total += subres

print(total)





