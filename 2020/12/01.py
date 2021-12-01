#!/usr/bin/python

test = 1

if test == 0:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

dist = 0

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

angle = EAST
east = 0
north = 0

with open(input_file, "r") as f:

    for line in f:
        line = line.strip()

        if not line:
            continue

        cmd = line[0]
        line = line[1:]

        num = int(line)


        print("%s[%d] %d:%d:%d" % (cmd, num, angle, east, north))

        if cmd == "N":
            north += num
        elif cmd == "S":
            north -= num
        elif cmd == "E":
            east += num
        elif cmd == "W":
            east -= num
        elif cmd == "L":
            angle = (angle + num) % 360
        elif cmd == "R":
            angle = (angle + 360 - num) % 360
        elif cmd == "F":
            if angle == EAST:
                east += num
            elif angle == WEST:
                east -= num
            elif angle == NORTH:
                north += num
            elif angle == SOUTH:
                north -= num



print("Distance: %d + %d == %d" % (east, north, abs(east) + abs(north)))



        
