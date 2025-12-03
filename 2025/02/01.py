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

def gen_and_add(start, stop):
    s1 = int(start[:len(start)//2])
    s2 = int(start[len(start)//2:])
    if s2 > s1:
        s1 += 1

    e1 = int(stop[:len(stop)//2])
    e2 = int(stop[len(stop)//2:])
    if e2 < e1:
        e1 -= 1

    if debug:
        print("    s=(%d,%d) e=(%d,%d)" % (s1, s2, e1, e2))
    
    if e1 < s1:
        return 0

    count = e1 - s1 + 1
    total = 0
    for num in range(s1, e1+1):
        total += num + num * pow(10, (int(math.log10(num)) + 1))
    
    if debug:
        print("    %d nunbers with sum %d" % (count, total))

    return total


total = 0

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()
        ranges = line.split(",")
        for r in ranges:
            [start ,stop] = [x.strip() for x in r.split("-")]

            if len(stop) < 2:
                continue

            if len(start) % 2:
                start = "1" + "0"*len(start)
            if len(stop) % 2:
                stop = "9"*(len(stop)-1)

            range_sum = gen_and_add(start, stop)

            if debug:
                print("%s (%s-%s): %d" % (r, start, stop, range_sum))

            total += range_sum

print(total)
