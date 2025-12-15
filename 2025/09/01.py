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

coos = []

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        [x,y] = [int(c.strip()) for c in line.split(",")]

        coos.append((x,y))

max_area = 0
for i in range(len(coos)):
    b1 = coos[i]
    for j in range(i+1, len(coos)):
        b2 = coos[j]
        area = (abs(b1[0] - b2[0]) + 1) * (abs(b1[1] - b2[1]) + 1)
        #print("%s : %s = %d" % (b1,b2, area))
        max_area = max(area, max_area)

print(max_area)
