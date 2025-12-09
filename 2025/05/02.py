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

with open(fname, "rt") as f:
    y = 0
    for line in f:
        line = line.strip()

        if not line:
            break
        f1,f2 = line.split("-")
        f1 = int(f1)
        f2 = int(f2)
        if f2 >= f1:
            fresh.append([f1, f2])


total_count = 0

fresh.sort()

while True:
    made_progress = False

    i = 0
    while i < len(fresh) - 1:
        if fresh[i][1] >= fresh[i+1][0]:
            fresh[i][1] = max(fresh[i][1], fresh[i+1][1])
            del fresh[i+1]
            made_progress = True
            continue
        i += 1

    if not made_progress:
        break


for [f1,f2] in fresh:
    print("(%d,%d)=%d" % (f1,f2, f2-f1+1))
    total_count += f2 - f1 + 1

print(total_count)








