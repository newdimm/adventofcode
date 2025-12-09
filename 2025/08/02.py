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

box = []

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        b = [int(x.strip()) for x in line.split(",")]
        box.append(tuple(b))

dist = {}

def get_dist(b1, b2):
    return pow(b1[0] - b2[0], 2) + \
           pow(b1[1] - b2[1], 2) + \
           pow(b1[2] - b2[2] ,2)

print("%d boxes" % len(box))

for i in range(len(box)):
    b1 = box[i]
    for j in range(i+1, len(box)):
        b2 = box[j]

        d = get_dist(b1,b2)

        l = []
        if d in dist:
            l = dist[d]
        if b1 < b2:
            l.append((b1,b2))
        else:
            l.append((b2,b1))
        dist[d] = l

print("%d distances" % len(dist))

dist_list = [x for x in dist.keys()]
dist_list.sort()

print("Shortest 10: %s" % dist_list[:10])

connected = []
count = 0

for d in dist_list:
    for b in dist[d]:
        b1,b2 = b
        print("%s == %s" % (b1,b2))
        i1 = None
        i2 = None
        for i in range(len(connected)):
            if b1 in connected[i]:
                i1 = i
            if b2 in connected[i]:
                i2 = i

        if i1 == None and i2 == None:
            if debug:
                print("  new")
            connected.append([b1,b2])
        elif i2 is None:
            if debug:
                print("  add %d" % (i1))
            connected[i1].append(b2)
        elif i1 is None:
            if debug:
                print("  add %d" % (i2))
            connected[i2].append(b1)
        elif i1 != i2:
            if debug:
                print("  merge %d %d" % (i1,i2))
            connected[i1].extend(connected[i2])
            del connected[i2]
        else:
            if debug:
                print("  ignore")

        print("    len(connected)=%d" % len(connected))

        count += 1

        if len(connected) == 1 and len(connected[0]) == len(box):
            break

    if len(connected) == 1 and len(connected[0]) == len(box):
        break

print("stopped after %d connections" % count)
print(b1,b2)

print(b1[0] * b2[0])
