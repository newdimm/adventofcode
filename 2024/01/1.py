#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

p1 = []
p2 = []

with open(fname) as f:
    for line in f:
        r = [int(x) for x in line.strip().split("   ")]
        p1.append(r[0])
        p2.append(r[1])
        
        
p1.sort()
p2.sort()

diffs = 0
for index in range(len(p1)):
    diffs += abs(p1[index] - p2[index])
    
print(diffs)