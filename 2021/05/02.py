#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

def get_line(x1,y1, x2, y2):
    result = []

    if x1 != x2:
        delta_x = (x2 - x1) / abs(x2 - x1)
    if y1 != y2:
        delta_y = (y2 - y1) / abs(y2 - y1)

    if x1 != x2 and y1 != y2:
        # diagonal
        #print("[%d,%d] -> [%d,%d] diagonal delta x %d y %d" % (x1,y1,x2,y2, delta_x, delta_y))
        x = x1
        y = y1
        while x != x2 and y != y2:
            result.append((x,y))
            x += delta_x 
            y += delta_y

        result.append((x2,y2))

    elif x1 != x2:
        #print("[%d,%d] -> [%d,%d] horizontal delta %d" % (x1,y1,x2,y2, delta_x))
        # horizontal
        x = x1
        while x != x2:
            result.append((x,y2))
            x += delta_x
        result.append((x2, y2))

    elif y1 != y2:
        # vertical
        #print("[%d,%d] -> [%d,%d] vertixal delta %d" % (x1,y1,x2,y2, delta_y))
        y = y1
        while y != y2:
            result.append((x1,y))
            y += delta_y
        result.append((x1, y2))

    return result

vents = []

max_x = 0
max_y = 0

for line in f:
    line = line.split(" -> ")
    x1,y1 = line[0].split(",")
    x2,y2 = line[1].split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 != x2 and y1 != y2 and abs(x1-x2) != abs(y1-y2):
        #print("[(%d,%d);(%d,%d) skip" % (x1,y1,x2,y2))
        continue

    vent = get_line(x1,y1,x2,y2)
    print("[(%d,%d);(%d,%d) ==> %s" % (x1,y1,x2,y2, vent))

    vents.append(vent)
    
    max_x = max(x1,x2,max_x)
    max_y = max(y1,y2,max_y)

floor = []
for y in range(max_y+1):
    floor.append([0] * (max_x+1))

def print_floor(floor):
    for row in floor:
        line = ""
        for x in row:
            if x > 0:
                line += str(x)
            else:
                line += '-'
        print(line)

for vent in vents:
    for x,y in vent:
        floor[y][x] += 1

count = 0
for x in range(max_x + 1):
    for y in range(max_y + 1):
        if floor[y][x] >= 2:
            count += 1
        

#print_floor(floor)
print(count)


