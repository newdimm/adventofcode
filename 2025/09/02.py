#!/bin/python3

import sys
import math
 
fname = "test.txt"
debug = False
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2 and sys.argv[2] == "debug":
            debug = True

red = {}
green = {}
x = y = None
ox = oy = None
fx = fy = None
maxx = maxy = 0

def trace(green, ox,oy,x,y):
    if x == ox:
        if oy < y:
            step = 1
        else:
            step = -1
        for ny in range(oy, y, step):
            green[(x,ny)] = 1
    elif y == oy:
        if ox < x:
            step = 1
        else:
            step = -1
        for nx in range(ox, x, step):
            green[(nx,y)] = 1
    else:
        raise("unexpected (%d,%d) -> (%d,%d)" % (ox,oy,x,y))

def draw(red,green,grey, maxx, maxy):
    if not debug:
        return

    for y in range(maxy+2):
        line = ""
        for x in range(maxx+2):
            if (x,y) in red:
                line += "#"
            elif (x,y) in green:
                line += "X"
            elif (x,y) in grey:
                line += "*"
            else:
                line += "."
        print(line)


with open(fname, "rt") as f:
    for line in f:
        line = line.strip()

        [x,y] = [int(c.strip()) for c in line.split(",")]

        maxx = max(x, maxx)
        maxy = max(y, maxy)

        if ox is None:
            fx = x
            fy = y
        else:
            trace(green, ox,oy,x,y)

        red[(x,y)] = 1
        ox = x
        oy = y

    trace(green, x,y,fx,fy)

print("red: %d mats, green: %d mats" % (len(red), len(green)))
start = None
for (x,y) in red.keys():
    if start is None or start[0] > x:
        start = (x,y)

for (x,y) in red.keys():
    if x == start[0] and y < start[1]:
        start = (x,y)

print("top leftmost corner: (%d,%d)" % (start[0], start[1]))

grey = {}
g = [(start[0]-1, start[1])]
while g:
    (x,y) = g.pop()

    for dx in (-1, 0, 1):
        nx = x + dx
        for dy in (-1, 0, 1):
            ny = y + dy
            if (x,y) == (nx,ny):
                continue
            if (nx,ny) in grey:
                continue
            if (nx,ny) in green or (nx,ny) in red:
                continue
            for ddx,ddy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nnx = nx + ddx
                nny = ny + ddy
                if (nnx,nny) in red or (nnx, nny) in green:
                    grey[(nx,ny)] = 1
                    g.append((nx, ny))
                    break

print("grey: %d mats" % len(grey))

draw(red,green,grey, maxx, maxy)

areas = {}
areas_list = []

coos = [x for x in red.keys()]

def get_quatro(x,y, grey):
    x1 = x-1
    while (x1,y) not in grey:
        x1 -= 1
    x2 = x+1
    while (x2,y) not in grey:
        x2 += 1

    y1 = y-1
    while (x,y1) not in grey:
        y1 -= 1
    y2 = y+1
    while (x,y2) not in grey:
        y2 += 1
    return (x1,x2, y1,y2)

for i in range(len(coos)):
    (x,y) = coos[i]
    x1,x2,y1,y2 = get_quatro(x,y,grey)
    for j in range(i+1, len(coos)):
        (nx,ny) = coos[j]
        if nx > x2 or nx < x1 or ny > y2 or ny < y1:
            continue

        area = (abs(x - nx) + 1) * (abs(y - ny) + 1)
        #print("%s : %s = %d" % (b1,b2, area))
        if area in areas:
            areas[area].append(((x,y), (nx,ny)))
        else:
            areas[area] = [((x,y),(nx,ny))]
            areas_list.append(area)

print("%d areas" % len(areas_list))
areas_list.sort(reverse=True)

print("areas sorted")

def check(grey, b1, b2):
    x1,y1 = b1
    x2,y2 = b2
    if x1 > x2:
        dx = -1
    else:
        dx = 1
    if y1 > y2:
        dy = -1
    else:
        dy = 1
    x, y = x1,y1
    for (ddx, ddy, stop) in [(dx,0,(x2,y1)),(0,dy,(x2,y2)),(-dx,0,(x1,y2)),(0,-dy,(x1,y1))]:
        while (x,y) != stop:
            x += ddx
            y += ddy
            if (x,y) in grey:
                return False

    return True

result = None
for a in areas_list:
    print("check %d (%d count)" % (a, len(areas[a])))
    for b1,b2 in areas[a]:
        if check(grey, b1,b2):
            result = a
            break
    if result:
        break

print(result)



