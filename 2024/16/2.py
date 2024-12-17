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

def show(walls, spath, start, finish, mx, my):
    sx,sy,look = start
    fx,fy = finish
    
    for y in range(my):
        str = ""
        for x in range(mx):
            if (x,y) in walls:
                str += "#"
            elif (x,y) in spath:
                str += "O"
            elif (x,y) == finish:
                str += "E"
            elif (x,y) == (sx,sy):
                str += look
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


heapq.heappush(stack, (cost,x,y,look,x,y, look))

seen = {}
iteration = 0
while stack:
    cost, x,y,look,px,py,plook = heapq.heappop(stack)
        
    prev_path_list = []
    
    if (x,y,look) in seen:
        (old_cost, old_prev) = seen[(x,y,look)]
        if old_cost < cost:
            continue
        if old_cost == cost:
            prev_path_list = old_prev
            
    if (px,py,plook) not in prev_path_list: 
        prev_path_list.append((px,py,plook))
    seen[(x,y,look)] = (cost, prev_path_list)
    
    if (x,y) == finish:
        break
    
    paths = get_paths(walls, x,y, look, cost)
    
    for nx,ny,nlook, ncost in paths:
        if (nx,ny,nlook) not in seen or seen[(nx,ny,nlook)][0] > ncost:
            heapq.heappush(stack, (ncost,nx,ny,nlook,x,y,look))
    
    
    #show(walls, seen, (x,y,look), finish, mx, my)
    #time.sleep(0.1)
    #ignore = input("press enter")

total_cost = cost
spath = {}

sx,sy,slook = start

stack = [(x,y,look)]

while stack:
    x,y,look = stack.pop()
    
    spath[(x,y)] = True
    if (x,y) != (sx,sy):
        cost, path_list = seen[(x,y,look)]
        stack.extend(path_list)
        
    #show(walls, spath, start, finish, mx, my)
    #ignore = input("press enter")

spath[(sx,sy)] = True

show(walls, spath, start, finish, mx, my)
    
print("Result: %d tiles: %d" % (total_cost, len(spath)))
