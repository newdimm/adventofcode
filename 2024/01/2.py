#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

p1 = []
p2 = {}

with open(fname) as f:
    for line in f:
        [r1, r2] = [int(x) for x in line.strip().split("   ")]
        p1.append(r1)

        try:
            p2[r2] += 1
        except KeyError:
            p2[r2] = 1
        
    
syscore = 0
    
for d in p1:
    try:
        syscore += d * p2[d]
        print("+ %d * %d = %d" % (d, p2[d], d * p2[d]))
    except KeyError:
        print("0 for %d" % d)
        pass
            
print(syscore)