#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

obstacles = {}
map = []
guard = (0,0,(1,0))
                
xx = 0
yy = 0
mx = 0
my = 0
with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        xx = 0
        mx = max(mx, len(line))
        for l in line:
            if l == '>':
                start = (xx,yy,1,0)
            elif l == '<':
                start = (xx,yy,-1,0)
            elif l == '^':
                start = (xx,yy,0,-1)
            elif l == 'v' or l == 'V':
                start = (xx,yy,0,1)
            elif l == '#':
                obstacles[(xx,yy)] = True
            xx += 1
        yy += 1
my = yy

def find_obstacle(obs, x, y, dirx, diry, maxx, maxy):
    found = False
    
    while True:
        new_x = x + dirx
        new_y = y + diry
        if new_x < 0 or new_x == maxx or new_y < 0 or new_y == maxy:
            break
        if (new_x, new_y) in obs:
            found = True
            break
        
        x = new_x
        y = new_y 
        
    return found, x, y

def rotate(dx, dy):
    if dx < 0:
        dx = 0
        dy = -1
    elif dx > 0:
        dx = 0
        dy = 1
    elif dy < 0:
        dx = 1
        dy = 0
    elif dy > 0:
        dx = -1
        dy = 0
    return dx, dy


def print_progress(obs, x,y, dx, dy, mx, my, visited, new_obs, last_track, q):
    if dx < 0:
        g = '<'
    elif dx > 0:
        g = '>'
    elif dy < 0:
        g = '^'
    elif dy > 0:
        g = 'v'
    
    map = []
    for j in range(my):
        line = []
        for i in range(mx):
            line.append(".")
        map.append(line)
    
    for (ox,oy) in obs.keys():
        map[oy][ox] = "#"
    
    for (vx,vy) in visited.keys():
        map[vy][vx] = "x"
        
    for (nox,noy) in new_obs.keys():
        map[noy][nox] = "O"
        
    for (ltx,lty) in last_track.keys():
        map[lty][ltx] = "+"
        
    if q:
        map[q[1]][q[0]] = "?"
    
    #map[y][x] = g
    
    print("---------------------")
    print("..|0123456789abcdef")
    
    y = 0
    for l in map:
        str = "%02x|" % y
        for s in l:
            str += s
        print(str)
        y += 1
    
    #ignore = input("press enter")

x,y,dx,dy = start
    
visited = {}
visited[(x,y)] = True 

new_obstacles = {}


print("(%d,%d) d(%d,%d) m(%d,%d)" % (x,y,dx,dy,mx,my))

while True:
    nx = x + dx
    ny = y + dy
    
    if nx < 0 or nx == mx or ny < 0 or ny == my:
        break

    if (nx, ny) in obstacles:
        dx, dy = rotate(dx,dy)
        continue

    seen = {}
    last_track = {}
    ldx,ldy = rotate(dx,dy)
    lx,ly = x,y
    seen[(lx,ly,dx,dy)] = True
    while True:
        lnx = lx + ldx
        lny = ly + ldy
         
        if lnx < 0 or lnx == mx or lny < 0 or lny == my:
            break

        if (lnx, lny) in obstacles or (lnx,lny) == (nx,ny):
            seen[(lx,ly,ldx,ldy)] = True             
            ldx,ldy = rotate(ldx,ldy)
            continue

        if (lnx,lny,ldx,ldy) in seen:
            new_obstacles[(nx,ny)] = True
            break

        lx = lnx
        ly = lny
        
    x = nx
    y = ny
    visited[(x,y)] = True
    
print_progress(obstacles, x,y,dx,dy, mx,my, visited, new_obstacles, {}, ())

print("visited: ", len(visited))
print("new obstacles: ", len(new_obstacles))


print("re-checking")

finals = []

for o in new_obstacles.keys():
    nox, noy = o
    x,y,dx,dy = start

    seen = {}
    while True:
        nx = x + dx
        ny = y + dy
        
        if nx < 0 or nx == mx or ny < 0 or ny == my:
            break
    
        if (nx, ny) in obstacles or (nx,ny) == (nox,noy):
            seen[(x,y,dx,dy)] = True
            dx, dy = rotate(dx,dy)
            continue
        
        if (nx,ny,dx,dy) in seen:
            finals.append((nox,noy))
            break
            
        x = nx
        y = ny
        
print("final answer: ", len(finals))

## 440 was too low
# 1578 too high
# 1594 not right

