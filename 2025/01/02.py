#!/bin/python3
import sys
 
fname = "1.txt"
debug = False
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2 and sys.argv[2] == "debug":
            debug = True

dial = 50
counter = 0

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        delta = int(line[1:])

        if line[0] == "R":
            dial += delta
            rounds = dial // 100
            dial = dial % 100
        else:
            dial = (100 - dial)%100
            dial += delta
            rounds = dial // 100
            dial = dial % 100
            dial = (100 - dial)%100

        counter += rounds

        if debug:
            print(line, dial, rounds, counter)

print(counter)
