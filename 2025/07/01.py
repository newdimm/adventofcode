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

streams = {}
counter  = 0
smax = 0

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        if not streams:
            pos = 0
            for c in line:
                if c == "S":
                    smax = len(line) - 1
                    streams[pos] = 1
                pos += 1
            continue


        new_streams = {}

        for s in streams.keys():
            if line[s] == "^":
                counter += 1
                if s > 0:
                    new_streams[s-1] = 1
                if s < smax:
                    new_streams[s+1] = 1
            else:
                new_streams[s] = 1
        streams = new_streams

print(counter)




