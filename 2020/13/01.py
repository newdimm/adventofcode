#!/usr/bin/python

import sys

if len(sys.argv) > 1:
    test = int(sys.argv[1])
else:
    test = 1


if test == 0:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

print("Test file: %s" % input_file)


timestamp = None
buses = []

with open(input_file, "r") as f:

    for line in f:
        line = line.strip()

        if not line:
            continue

        if timestamp is None:
            timestamp = int(line)
        else:
            for b in line.split(","):
                if b != "x":
                    buses.append(int(b))




    if timestamp is None:
        exit(1)

    print("Time: %d" % timestamp)
    print("Busses: %s" % buses)

    best_bus = None
    best_time = None

    for b in buses:
        rem = (timestamp-1) // b
        next_time = (rem+1) * b

        if best_bus is None or best_time > next_time:
            best_bus = b
            best_time = next_time

    print("Best bus is %d leaving at %d diff %d result %d" % (best_bus, best_time, best_time - timestamp, best_bus * (best_time - timestamp)))



    



        
