#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]

walls = {}

looks = {
    # direction : (dx,dy)
    ">" : (1, 0),
    "<" : (-1, 0),
    "^" : (0, -1),
    "v" : (0, 1)
}

rotation_cost = 1000
step_cost = 1

rotate = {
    ">" : "^",
    "^" : "<",
    "<" : "v",
    "v" : ">"
}

y = 0
with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
      
        mx = len(line)      
        for x in range(len(line)):
            if line[x] == "#":
                walls[(x,y)] = True
            elif line[x] == "S":
                start = (x,y, ">")
            elif line[x] == "E":
                finish = (x,y)
        y += 1
                
my = y

print("s=%s f=%s max(%d,%d)" % (start, finish, mx, my))

def show(walls, seen, start, finish, mx, my):
    sx,sy,look = start
    fx,fy = finish
    
    for y in range(my):
        str = ""
        for x in range(mx):
            if (x,y) in walls:
                str += "#"
            elif (x,y) == finish:
                str += "E"
            elif (x,y) == (sx,sy):
                str += look
            elif (x,y) in seen:
                str += "-"
            else:
                str += "."
        print(str)
        
def get_paths(walls, x,y,look, cost):
    paths = []
    
    rot_cost = {
        0 : 0,
        1 : rotation_cost,
        2 : 2 * rotation_cost,
        3 : rotation_cost
    }
    
    for i in range(4):
        dx,dy = looks[look]
        nx = x + dx
        ny = y + dy
        if (nx,ny) not in walls:
            paths.append((nx,ny,look, cost + rot_cost[i] + 1))
        
        look = rotate[look]
        
    return paths
    
show(walls, {}, start, finish, mx, my) 

stack = []

x,y,look = start
cost = 0


heapq.heappush(stack, (cost,x,y,look))

seen = {}
iteration = 0
while stack:
    cost, x,y,look = heapq.heappop(stack)
    
    if (x,y) == finish:
        break
    
    if (x,y,look) in seen:
        old_cost = seen[(x,y,look)]
        if old_cost < cost:
            continue
    seen[(x,y,look)] = cost
    
    paths = get_paths(walls, x,y, look, cost)
    
    for nx,ny,nlook, ncost in paths:
        if (nx,ny,nlook) not in seen or seen[(nx,ny,nlook)] > ncost:
            heapq.heappush(stack, (ncost,nx,ny,nlook))
            
    
    
    #show(walls, seen, (x,y,look), finish, mx, my)
    #time.sleep(0.1)
    #ignore = input("press enter")
    
print("Result: %d" % cost)

            