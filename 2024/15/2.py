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
            mx = len(line)*2
                
            for x in range(len(line)):
                if line[x] == "#":
                    walls[(2*x,   y)] = True
                    walls[(2*x+1, y)] = True
                elif line[x] == "O":
                    boxes[(2*x,   y)] = 0
                    boxes[(2*x+1, y)] = 1
                elif line[x] == "@":
                    robot = [2*x, y]
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
    print("   01234567890")
    for y in range(my):
        line = "%02d|" % y 
        for x in range(mx):
            if (x,y) in boxes and boxes[(x,y)] == 0:
                line += "["
            elif (x,y) in boxes and boxes[(x,y)] == 1:
                line += "]"
            elif (x,y) in walls:
                line += "#"
            elif robot == [x,y]:
                line += "@"
            else:
                line += "."
        print(line)
        
    print("   01234567890")
        
def old_do_step(boxes, walls, robot, dx ,dy):
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
            b = boxes[(x,y)]
            del boxes[(x,y)]
            boxes[(x+dx, y+dy)] = b
        elif [x,y] == robot:
            robot[0] += dx
            robot[1] += dy
        else:
            raise("Unexpected step at (%d,%d)" % (x,y))


def do_step(boxes, walls, robot, dx ,dy):
    
    if dy == 0:
        old_do_step(boxes, walls, robot, dx ,dy)
        return
        
    print("Do: (%d,%d)" % (dx,dy))
    [x,y] = robot

    stack = [(x,y)]
    can_do = True
    
    nx = x + dx
    ny = y + dy
    
    front = [(nx,ny)]
    stop = False
    
    print("front: (%d,%d)" % (nx,ny))
    
    while not stop:
        new_front = []
        for (nx,ny) in front:
            if (nx,ny) in walls:
                can_do = False
                stop = True
                print("wall at (%d,%d)"%(nx,ny))    
                break
            elif (nx,ny) in boxes:
                if boxes[(nx,ny)] == 0:
                    if (nx,ny) not in stack:
                        stack.append((nx,ny))
                    if (nx+1,ny) not in stack:
                        stack.append((nx+1,ny))
                    if (nx,ny) not in new_front:
                        new_front.append((nx,ny))
                    if (nx+1,ny) not in new_front:
                        new_front.append((nx+1,ny))
                else: # == 1
                    if (nx,ny) not in stack:
                        stack.append((nx,ny))
                    if (nx-1,ny) not in stack:
                        stack.append((nx-1,ny))
                    if (nx,ny) not in new_front:
                        new_front.append((nx,ny))
                    if (nx-1,ny) not in new_front:
                        new_front.append((nx-1,ny))
        if not new_front:
            print("stop")
            break

        front = []
        for x,y in new_front:
            nx = x + dx
            ny = y + dy
            front.append((nx,ny))
        print("new_front:", front)
        
    if not can_do:
        "print don't move"
        return
    while stack:
        x,y = stack.pop()
        if (x,y) in boxes:
            b = boxes[(x,y)]
            del boxes[(x,y)]
            boxes[(x+dx, y+dy)] = b
        elif [x,y] == robot:
            robot[0] += dx
            robot[1] += dy
        else:
            print("(%d,%d) is neither robot nor a box" % (x,y))
            raise("Unexpected step at (%d,%d)" % (x,y))
    
show(boxes, walls, robot, mx, my)
ignore=input("press enter")

for dx,dy in steps:
    do_step(boxes, walls, robot, dx, dy)
    #show(boxes, walls, robot, mx, my)
    #ignore = input("press enter")

show(boxes, walls, robot, mx, my)

total = 0
for (x,y) in boxes.keys():
    if boxes[(x,y)] == 0:
        total += y * 100 + x
    
print("result: %d" % total)