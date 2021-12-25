#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

floor = []
marked= []
for line in f_input:
    line = line.strip()
    row = []
    for char in line:
        row.append(int(char))
    floor.append(row)
    marked.append([0] * len(row))

max_y = len(floor)
max_x = len(floor[0])

counter = 0

def find_lowest():
    lowest = 9
    min_x = 0
    min_y = 0
    for y in range(max_y):
        for x in range(max_x):
            if not marked[y][x] and floor[y][x] < lowest:
                lowest = floor[y][x]
                min_x = x
                min_y = y
    return (lowest, min_x, min_y)

(lowest, x, y) = find_lowest()

largest = [0,0,0]

while lowest != 9:
    counter += 1
    marked[y][x] = counter
    stack = []
    stack.append((x,y,lowest))
    size = 1
    while stack:
        (x,y,level) = stack.pop()
        for new_x, new_y in [(x-1,y), (x+1,y), (x,y+1), (x,y-1)]:
            if new_x >= 0 and new_y >= 0 and new_x < max_x and new_y < max_y \
                    and not marked[new_y][new_x] and floor[new_y][new_x] != 9 and floor[new_y][new_x] >= level:
                stack.append((new_x,new_y,floor[new_y][new_x]))
                marked[new_y][new_x] = counter
                size += 1

    largest.append(size)
    largest.sort()
    largest = largest[1:]
    
    (lowest, x, y) = find_lowest()

for y in range(len(floor)):
    line = ""
    for x in range(len(floor[y])):
        line += "%d" % floor[y][x]
    print(line)

print("")

for y in range(len(marked)):
    line = ""
    for x in range(len(marked[y])):
        line += "%d" % marked[y][x]
    print(line)

print("%d * %d * %d = %d" % (largest[0], largest[1], largest[2],
    largest[0] * largest[1] * largest[2]))




