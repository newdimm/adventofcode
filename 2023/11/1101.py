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

def print_space(space):
    for r in space:
        line = ""
        for c in r:
            line += c
        print(line)

print_space(space)

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

print("expand")

empty_rows.sort()

while empty_rows:
    r = empty_rows.pop()
    line = ["." for x in range(len(space[0]))]
    space.insert(r, line)

empty_cols.sort()

while empty_cols:
    c = empty_cols.pop()
    for r in range(len(space)):
        space[r].insert(c, ".")


print_space(space)

gxies = []

for r in range(len(space)):
    for c in range(len(space[r])):
        if space[r][c] == "#":
            gxies.append((c, r))

print("%d gxies: %s" % (len(gxies), gxies))

def get_sub_space(space, g1, g2):
    minx = min(g1[0], g2[0])
    miny = min(g1[1], g2[1])

    maxx = max(g1[0], g2[0])
    maxy = max(g1[1], g2[1])
    #print("subspace: %d, %d -> %d, %d" % (minx,miny, maxx, maxy))

    sub_space = []
    for r in range(miny, maxy+1):
        sub_space.append(space[r][minx : maxx+1])
    
    return sub_space

lengths = {}
used_cached = 0
used_not_cached = 0

def shortest_path(space, g1, g2):
    global used_cached
    global used_not_cached

    #print("SP between %s and %s" % (g1, g2))
    sub_space = get_sub_space(space, g1, g2)
    dims = []
    dims.append(len(sub_space))
    dims.append(len(sub_space[0]))
    dims.sort()
    if (dims[0], dims[1]) in lengths:
        length = lengths[(dims[0], dims[1])]
        #print("cached: %d" % length)
        used_cached += 1
        return length

    used_not_cached += 1

    length = 0
    
    x = 0
    y = 0
    paths = {}
    paths[(0,0)] = 0
    stack = []
    stack.append((0,0))
    max_x = len(sub_space[0]) - 1
    max_y = len(sub_space) - 1
    #print("max_x %d max_y %d" % (max_x, max_y))
    while stack:
        x, y = stack.pop()
        length = paths[(x,y)]

        if x + 1 <= max_x:
            if not (x+1,y) in paths or paths[(x+1, y)] > length + 1:
                paths[(x+1, y)] = length + 1
                stack.append((x+1,y))

        if y + 1 <= max_y:
            if not (x,y+1) in paths or paths[(x, y+1)] > length + 1:
                paths[(x, y+1)] = length + 1
                stack.append((x,y+1))

    length = paths[(max_x, max_y)]

    lengths[(dims[0], dims[1])] = length
    return length


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

