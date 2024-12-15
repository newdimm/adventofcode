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

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
            
        # p=0,4 v=3,-3
            
        params = line.split(" ")
        for p in params:
            if p.startswith("p="):
                x,y = [int(x) for x in p[2:].split(",")]
            elif p.startswith("v="):
                dx,dy = [int(x) for x in p[2:].split(",")]
        
        try:
            l = robots[(x,y)]
        except KeyError:
            l = []
        l.append((dx,dy))
        robots[(x,y)] = l

def show(time, rs, mx, my):
    print("==== After %d seconds =============" % time)
    for y in range(my):
        line = ""
        for x in range(mx):
            if (x,y) in rs:
                count = min(9,len(rs[(x,y)]))
                line += "%d" % count
            else:
                line += "."
        print(line)

show(0, robots, mx, my)
    
time = 0
while time < 100:

    new_robots = {}
    for x,y in robots.keys():
        l = robots[(x,y)]
        for dx,dy in l:
            nx = (x + dx) % mx
            ny = (y + dy) % my
            
            try:
                nl = new_robots[(nx,ny)]
            except KeyError:
                nl = []
            nl.append((dx,dy))
            new_robots[(nx,ny)] = nl
            
    robots = new_robots
    time += 1
    
    show(time, robots, mx, my)
    #ignore = input("press enter")

total = 1
for q in ((0,0, mx//2-1,my//2-1),
          (mx//2+1,0, mx-1,my//2-1),
          (0,my//2+1, mx//2-1, my-1),
          (mx//2+1, my//2+1, mx-1, my-1)):
    x1,y1,x2,y2 = q
    t = 0
    for x,y in robots.keys():
        if x >= x1 and y >= y1 and x <= x2 and y <= y2:
            t += len(robots[x,y])
    total *= t
    
print("result: %d" % total) 
