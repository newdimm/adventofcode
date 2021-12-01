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
wp_east = 10
wp_north = 1


def rotate(north, east, angle):
    if angle == 0:
        new_north = north
        new_east == eaest
    elif angle == 90:
        new_north = east
        new_east = -north
    elif angle == 180:
        new_north = -north
        new_east = -east
    elif angle == 270:
        new_north = -east
        new_east = north

    return (new_north, new_east)

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
            wp_north += num
        elif cmd == "S":
            wp_north -= num
        elif cmd == "E":
            wp_east += num
        elif cmd == "W":
            wp_east -= num
        elif cmd == "L":
            (wp_north, wp_east) = rotate(wp_north, wp_east, num)
        elif cmd == "R":
            (wp_north, wp_east) = rotate(wp_north, wp_east, 360-num)
        elif cmd == "F":
            north += wp_north * num
            east += wp_east * num



print("Distance: %d + %d == %d" % (east, north, abs(east) + abs(north)))



        
