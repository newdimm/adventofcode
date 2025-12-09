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

def print_streams(streams, smax):
    line = ""
    for x in range(smax):
        if x in streams:
            line += "%d" % streams[x]
        else:
            line += " "
    print(line)

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        if debug:
            print(line)

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
            c = streams[s]

            if line[s] == "^":
                counter += 1
                for news in [s-1, s+1]:
                    if news >= 0 and news <= smax:
                        newc = c
                        if news in new_streams:
                            newc += new_streams[news]
                        new_streams[news] = newc
            else:
                if s in new_streams:
                    c += new_streams[s]
                new_streams[s] = c
        streams = new_streams

        if debug:
            print_streams(streams, smax)

total = 0
for s in streams:
    total += streams[s]
print(total)




