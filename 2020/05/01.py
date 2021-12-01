#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:

    highest = 0



    for line in f:
        line = line.strip()

        if not line:
            continue

        r_min = 0
        r_max = 127

        c_min = 0
        c_max = 7

        print("%s: r[%d:%d] c[%d:%d]" % (line, r_min, r_max, c_min, c_max))

        for c in line:
            if c == "F":
                center = (r_min + r_max) / 2
                r_max = center
            elif c == "B":
                center = (r_min + r_max) / 2
                r_min = center + 1
            elif c == "L":
                center = (c_min + c_max) / 2
                c_max = center
            elif c == "R":
                center = (c_min + c_max) / 2
                c_min = center + 1

            print("%c: [%d:%d] c[%d:%d]" % (c, r_min, r_max, c_min, c_max))
                   

        seat = r_min * 8 + c_min
        print("seat: %d\n\n" % seat)

        highest = max(highest, seat)


    print("highest: %d" % highest)


