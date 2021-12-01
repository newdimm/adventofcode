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


    answer = 1

    patterns = [
            (1,1),
            (1,3),
            (1,5),
            (1,7),
            (2,1)]

    for p in patterns:
        down = 0
        right = 0

        counter = 0

        while down < len(slopes):
            if slopes[down][right] == '#':
                counter += 1
            right = (right + p[1]) % len(slopes[down])
            down += p[0]

        answer *= counter

    print("Tree counter: %d" % answer)


