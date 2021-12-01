#!/usr/bin/python

test = 0 

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:
    num_valid = 0

    slopes = []

    for line in f:
        slopes.append(line.strip())

    down = 0
    right = 0

    counter = 0

    while down < len(slopes):
        if slopes[down][right] == '#':
            counter += 1
        right = (right + 3) % len(slopes[down])
        down += 1

    print("Tree counter: %d" % counter)


