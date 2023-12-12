#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg.startswith("test"):
            fname = "input_%s" % arg

space = []

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        space.append([l for l in line])

def print_space(gxies, steps):
    maxx = 0
    maxy = 0
    for g in gxies:
        maxx = max(maxx, g[0])
        maxy = max(maxy, g[1])

    for s in steps:
        maxx = max(maxx, s[0])
        maxy = max(maxy, s[1])

    for y in range(maxy+1):
        line = ""
        for x in range(maxx + 1):
            if (x,y) in gxies:
                line += "#"
            elif (x,y) in steps:
                line += "-"
            else:
                line += " "
        print(line)

empty_cols = [x for x in range(len(space[0]))]
empty_rows = [x for x in range(len(space))]

for r in range(len(space)):
    for c in range(len(space[r])):
        if space[r][c] == "#":
            if r in empty_rows:
                del empty_rows[empty_rows.index(r)]

            if c in empty_cols:
                del empty_cols[empty_cols.index(c)]


print("empty rows: %s", empty_rows)
print("empty cols: %s", empty_cols)

gxies = []

for r in range(len(space)):
    for c in range(len(space[r])):
        if space[r][c] == "#":
            gxies.append((c, r))

print("%d gxies: %s" % (len(gxies), gxies))

print_space(gxies, [])

print("expand")

empty_rows.sort()

#delta = 1
delta = 1000000 - 1

while empty_rows:
    r = empty_rows.pop()
    
    for i in range(len(gxies)):
        if gxies[i][1] > r:
            gxies[i] = (gxies[i][0], gxies[i][1] + delta)


empty_cols.sort()

while empty_cols:
    c = empty_cols.pop()
    for i in range(len(gxies)):
        if gxies[i][0] > c:
            gxies[i] = (gxies[i][0] + delta, gxies[i][1])

#print_space(gxies, [])

paths = {}
used_cached = 0
used_not_cached = 0

def shortest_path(space, g1, g2):
    global used_cached
    global used_not_cached

    #print("SP between %s and %s" % (g1, g2))
    minx = min(g1[0], g2[0])
    maxx = max(g1[0], g2[0])
    length = maxx - minx + 1

    miny = min(g1[1], g2[1])
    maxy = max(g1[1], g2[1])
    width = maxy - miny + 1

    if (length, width) in paths:
        path = paths[(length, width)]
        used_cached += 1
        return path
    if (width, length) in paths:
        path = paths[(width, length)]
        used_cached += 1
        return path

    used_not_cached += 1

    path = length - 1 + width - 1

    paths[(length, width)] = path
    #print("stoped %s -> %s l:%d w:%d(%x,%d) path %d" % (g1, g2, length, width, x, y, path))
    

    return path


result = 0
counter = 0

visited = {}
for g1 in gxies:
    for g2 in gxies:
        if g1 == g2 or (g1, g2) in visited or (g2, g1) in visited:
            continue
        length = shortest_path(space, g1, g2)
        visited[(g1,g2)] = True
        result += length
        counter += 1

print("sum of %d paths is %d" % (counter, result))
print("cached:%d, not cached %d" % (used_cached, used_not_cached))

