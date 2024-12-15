#!/bin/python3
import sys

fname = "1.txt"
mx = 11
my = 7

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        mx = 101
        my = 103
        
    
robots = {}

read_map = True
robot = []
boxes = {}
walls = {}

y = 0

mx = None

steps = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            read_map = False
            continue
            
        if read_map:
            mx = len(line)
                
            for x in range(len(line)):
                if line[x] == "#":
                    walls[(x,y)] = True
                elif line[x] == "O":
                    boxes[(x,y,)] = True
                elif line[x] == "@":
                    robot = [x,y]
            y += 1
        else: ## not read_map
            for s in line:
                
                if s == ">":
                    step = (1,0)
                elif s == "<":
                    step = (-1, 0)
                elif s == "^":
                    step = (0, -1)
                elif s == "v" or s == "V":
                    step = (0, 1)
                else:
                    raise("Unknown step %s" % s)
                    
                steps.append(step)
my = y

def show(boxes, walls, robot, mx, my):
    for y in range(my):
        line = ""
        for x in range(mx):
            if (x,y) in boxes:
                line += "O"
            elif (x,y) in walls:
                line += "#"
            elif robot == [x,y]:
                line += "@"
            else:
                line += "."
        print(line)
        
def do_step(boxes, walls, robot, dx ,dy):
    print("Do: (%d,%d)" % (dx,dy))
    [x,y] = robot

    stack = [(x,y)]
    can_do = True
    
    nx = x + dx
    ny = y + dy
    
    while True:
        if (nx,ny) in walls:
            can_do = False
            break
        elif (nx,ny) in boxes:
            stack.append((nx,ny))
        else:
            break
        nx += dx
        ny += dy
            
    if not can_do:
        "print don't move"
        return
    while stack:
        x,y = stack.pop()
        if (x,y) in boxes:
            del boxes[(x,y)]
            boxes[(x+dx, y+dy)] = True
        elif [x,y] == robot:
            robot[0] += dx
            robot[1] += dy
        else:
            raise("Unexpected step at (%d,%d)" % (x,y))
    
show(boxes, walls, robot, mx, my)

for dx,dy in steps:
    do_step(boxes, walls, robot, dx, dy)
    #show(boxes, walls, robot, mx, my)
    #ignore = input("press enter")

show(boxes, walls, robot, mx, my)

total = 0
for (x,y) in boxes.keys():
    total += y * 100 + x
    
print("result: %d" % total)