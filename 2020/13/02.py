#!/usr/bin/python

import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
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
                try:
                    buses.append(int(b))
                except ValueError:
                    buses.append("x")

    if timestamp is None:
        exit(1)

    print("Busses: %s" % buses)


    base = buses[0]
    buses = buses[1:]

    offset = 1


    pairs = []

    for b in buses:
        if b == "x":
            offset += 1
            continue

        print("Bus: %d offset %d" % (b, offset))

        cmd = base * b

        base_list = []
        bl = base
        while bl <= cmd:
            base_list.append(bl)
            bl += base

        v = b
        found = False
        while not found:
            for bl in base_list:
                if v >= bl and v - bl == offset:
                    print("Found blo: %d, %d + %d * x" % (v, (v-offset) // base, b))
                    pairs.append( ((v - offset) // base, b, offset) )
                    found = True
                    break
            v += b


        offset += 1

    d = {}

    max_m = 0
    max_index = 0
    index = 0

    for (s,m, o) in pairs:
        if m > max_m:
            max_m = m
            max_index = index
        index += 1


    max_sum = pairs[max_index][0]
    max_o = pairs[max_index][2]

    del pairs[max_index]

    found = False
    while not found:
        max_sum += max_m

        found = True

        for (s,m, o) in pairs:
            if (max_sum - s) % m != 0:
                found = False
                break

    print("Found: %d" % (max_sum * base))

    s = max_sum
    m = max_m
    o = max_o
    print("(%d - %d) / %d == %f => (%d + %d) %% %d == %d" % (max_sum, s, m, (max_sum - s) / m, base * max_sum, o, m, (base * max_sum + o) % m))

    for (s, m, o) in pairs:
        print("(%d - %d) / %d == %f => (%d + %d) %% %d == %d" % (max_sum, s, m, (max_sum - s) / m, base * max_sum, o, m, (base * max_sum + o) % m))

