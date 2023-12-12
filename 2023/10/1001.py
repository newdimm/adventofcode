#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test1" or arg == "test2":
            fname = "input_%s" % arg

result = 0

pipes = []
start_y = None
start_x = None

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        s = line.find("S")
        if s >= 0:
            start_x = s
            start_y = len(pipes)

        pipes.append([l for l in line])

## connections
cs = {
         # (x, y)
        "|" : (( 0, -1), ( 0,  1)),
        "J" : (( 0, -1), (-1,  0)),
        "F" : (( 0,  1), ( 1,  0)),
        "-" : ((-1,  0), ( 1,  0)),
        "L" : (( 1,  0), ( 0, -1)),
        "7" : ((-1,  0), ( 0,  1))
}

def do_step(x, y, visited, pipes):
    curr = cs[pipes[y][x]]

    loop = True
    for i in [0, 1]:
        new_x = x + curr[i][0]
        new_y = y + curr[i][1]

        if (new_x, new_y) not in visited:
            loop = False
            break

    if loop:
        print("loop")
        return new_x, new_y, True

    if new_x < 0 or new_x >= len(pipes[0]) \
            or new_y < 0 or new_y >= len(pipes):
        print("left the map")
        return new_x, new_y, True

    new_curr = pipes[new_y][new_x]

    if new_curr == ".":
        print("hit ground")
        return new_x, new_y, True

    #print("new_curr %s" % new_curr)
    new_curr = cs[new_curr]

    back = False
    for i in [0,1]:
        back_x = new_x + new_curr[i][0]
        back_y = new_y + new_curr[i][1]
        #print("[%d] back %d,%d" % (i, back_x, back_y))
        if back_x == x and back_y == y:
            back = True
            break

    if not back:
        print("hit not matching")
        return new_x, new_y, True

    visited[(x,y)] = True

    return new_x, new_y, False

for start_pos in ["|", "-", "J", "L", "F", "7"]:
    x = start_x
    y = start_y
    stop = False
    pipes[y][x] = start_pos
    visited = {}
    steps = 0
    print("===================")
    print("try <%s>" % start_pos)
    while not stop:
        if steps == 2:
            del visited[(start_x, start_y)]

        print("(%d, %d) %s" % (x,y,pipes[y][x]))
        new_x, new_y, stop = do_step(x, y, visited, pipes)
        #print("--> (%d, %d) %s stop %d" % (x,y,pipes[y][x], stop))
        
        if stop or steps != 0 and x == start_x and y == start_y:
            break
    
        x = new_x
        y = new_y
        steps += 1

    if steps > 0 and x == start_x and y == start_y:
        print("<%s> is good len %d steps / 2 = %d" % (start_pos, steps, (steps + 1) // 2))
    else:
        print("<%s> is NOT good len %d" % (start_pos, steps))



