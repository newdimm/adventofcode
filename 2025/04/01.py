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


paper = {}

def do_count(paper, x, y, mx, my):
    count = 0
    for dx in (-1, 0, 1):
        nx = x + dx
        if nx < 0 or nx > mx:
            continue

        for dy in (-1, 0, 1):
            ny = y + dy
            if ny < 0 or ny > my or (x,y) == (nx,ny):
                continue
            if (nx,ny) in paper:
                count += 1
    return count

mx = my = 0

with open(fname, "rt") as f:
    y = 0
    for line in f:
        line = line.strip()

        if debug:
            print(line)

        x = 0
        for c in line:
            if c == "@":
                paper[(x,y)] = 1
            x += 1
        mx = x - 1

        y += 1
my = y-1

total_count = 0

if debug:
    print(paper)

for (x,y) in paper.keys():
    count = do_count(paper, x,y, mx,my)
    print("(%d,%d) = %d" % (x,y,count))
    if count < 4:
        total_count += 1

print(total_count)








