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


fresh = []
ingredients = []

do_fresh = True

with open(fname, "rt") as f:
    y = 0
    for line in f:
        line = line.strip()

        if not line:
            do_fresh = False
            continue

        if do_fresh:
            f1,f2 = line.split("-")
            fresh.append((int(f1), int(f2)))
        else:
            ingredients.append(int(line))

total_count = 0

for i in ingredients:
    for (f1,f2) in fresh:
        if i >= f1 and i <= f2:
            total_count += 1
            break

print(total_count)








