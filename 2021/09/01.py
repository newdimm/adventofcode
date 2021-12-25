#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

floor = []
for line in f_input:
    line = line.strip()
    row = []
    for char in line:
        row.append(int(char))
    floor.append(row)

counter = 0

max_y = len(floor)

for y in range(max_y):
    max_x = len(floor[y])
    for x in range(max_x):
        if (y == 0 or floor[y][x] < floor[y-1][x]) and \
           (y + 1 == max_y or floor[y][x] < floor[y+1][x]) and  \
           (x == 0 or floor[y][x] < floor[y][x-1]) and \
           (x + 1 == max_x or floor[y][x] < floor[y][x+1]):
           counter += floor[y][x] + 1

print("counter: %d" % counter)




