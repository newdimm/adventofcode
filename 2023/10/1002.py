#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg.startswith("test"):
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

    visited[(x,y)] = 1

    return new_x, new_y, False

def get_next(visited, x, y):
    pipe = cs[pipes[y][x]]

    found = False

    for i in [0, 1]:
        new_x = x + pipe[i][0]
        new_y = y + pipe[i][1]

        if visited[(new_x, new_y)] < visited[(x,y)]:
            found = True
            break

    if not found:
        return True, -1, -1

    return False, new_x, new_y

def visited_maxes(visited):
    max_x = 0
    max_y = 0
    for x,y in visited.keys():
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    return max_x, max_y

def print_visited(visited):
    max_x, max_y = visited_maxes(visited)
    for y in range(max_y+1):
        line = ""
        for x in range(max_x+1):
            try:
                v = "%d" % visited[(x,y)]
            except KeyError:
                v = '.'
            line += v
        print(line)

UP =    ( 0, -1)
DOWN =  ( 0,  1)
LEFT =  (-1,  0)
RIGHT = ( 1,  0)
OUTSIDE = 0
INSIDE = 9

vectors = {
        LEFT:"LEFT",
        RIGHT:"RIGHT",
        UP:"UP",
        DOWN:"DOWN",
}

def get_neighbours(x, y, pipe, vector):
    left = []
    right = []

    swap = False

    #print("(%d, %d) pipe <%s> vector %s %s" % (x,y,pipe, vector, vectors[vector]))

    if pipe == "|" and vector in (UP, DOWN):
        left.append((x-1, y))
        right.append((x+1, y))
        if vector == DOWN:
            swap = True

    elif pipe == "-" and vector in (RIGHT, LEFT):
        left.append((x, y-1))
        right.append((x, y+1))
        if vector == LEFT:
            swap = True

    elif pipe == "F" and vector in (DOWN, RIGHT):
        print("pipe f")
        left.append((x-1, y))
        left.append((x-1, y-1))
        left.append((x, y-1))
        right.append((x+1, y+1))
        
        if vector == DOWN:
            swap = True

    elif pipe == "7" and vector in (LEFT, DOWN):
        left.append((x, y-1))
        left.append((x+1, y-1))
        left.append((x+1, y))
        right.append((x-1, y+1))
        
        if vector == LEFT:
            swap = True

    elif pipe == "J" and vector in (LEFT, UP):
        left.append((x+1, y))
        left.append((x+1, y+1))
        left.append((x, y+1))
        right.append((x-1, y-1))
        
        if vector == UP:
            swap = True

    elif pipe == "L" and vector in (UP, RIGHT):
        left.append((x, y+1))
        left.append((x-1, y+1))
        left.append((x-1, y))
        right.append((x+1, y-1))
        
        if vector == RIGHT:
            swap = True

    if not left or not right:
        return None, None

    left = [(x,y) for x,y in left if x >= 0 and y >= 0]
    right = [(x,y) for x,y in right if x >= 0 and y >= 0]

    if swap:
        left,right = right,left

    return left, right

            
def flood_fill(visited):
    stack = []

    for (x,y),value in visited.items():
        if value == 0:
            stack.append((x,y))

    while stack:
        x,y = stack.pop()
            
        for dx in (-1, 1):
            if (x + dx, y) not in visited:
                visited[(x+dx, y)] = 0
                stack.append((x+dx, y))
        for dy in (-1, 1):
            if (x, y + dy) not in visited:
                visited[(x, y+dy)] = 0
                stack.append((x, y + dy))



            



def colour(visited):
    max_x, max_y = visited_maxes(visited)

    print_visited(visited)
    
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in visited:
                start_x = x
                start_y = y
                break
        if (x,y) in visited:
            break

    print("start (%d, %d)" % (start_x, start_y))
    x = start_x
    y = start_y
    visited[(x,y)] += 1
    step = 0
    stop = False
    while not stop:
        #key = input()
        stop, new_x, new_y = get_next(visited, x, y)

        if stop:
            break

        vector = (new_x - x, new_y - y)
        left, right = get_neighbours(x, y, pipes[y][x], vector)

        if left is None or right is None:
            print("error (%d, %d)->(%d,%d) pipe %s vector %s" % (x,y,new_x,new_y, pipes[y][x], vector))
            break

        for lx, ly in left:
            if (lx, ly) not in visited:
                visited[(lx, ly)] = OUTSIDE

        for lx, ly in right:
            if (lx, ly) not in visited:
                visited[(lx, ly)] = INSIDE

        x = new_x
        y = new_y
        visited[(x,y)] += 1
        step += 1
        if step == 2:
            visited[(start_x, start_y)] -= 1
        print("(%d, %d)" % (x,y))
        #print_visited(visited)

    print_visited(visited)

    flood_fill(visited)

    print_visited(visited)

    count = 0
    for (x,y),value in visited.items():
        if value == 0:
            count += 1
    print("result: %d" % count)

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
        visited[(x,y)] = 1

        colour(visited)
        break
    else:
        print("<%s> is NOT good len %d" % (start_pos, steps))

