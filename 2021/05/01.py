#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

def get_line(x1,y1, x2, y2):
    result = []
    if x1 > x2:
        x1,x2 = x2,x1

    if y1 > y2:
        y1,y2 = y2,y1

    x = x1
    while x <= x2:
        result.append((x,y1))
        x += 1 
    y = y1 + 1
    while y <= y2:
        result.append((x1,y))
        y += 1

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
    if x1 != x2 and y1 != y2:
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


