#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

obstacles = []
map = []
guard = (0,0,(1,0))
                
x = 0
y = 0
maxx = 0
maxy = 0
with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        x = 0
        maxx = max(maxx, len(line))
        for l in line:
            if l == '>':
                guard = (x,y,(1,0))
            elif l == '<':
                guard = (x,y,(-1,0))
            elif l == '^':
                guard = (x,y,(0,-1))
            elif l == 'v' or l == 'V':
                guard = (x,y,(0,1))
            elif l == '#':
                obstacles.append((x,y))
            x += 1
        y += 1
maxy = y

print("obstacles: ", obstacles)
print("gurard: ", guard)
print("maxx=%d maxy=%d" % (maxx, maxy))


def find_min_o(obs, x, y, dirx, diry, maxx, maxy):
    steps = None
    
    stepsx = x
    stepsy = y
    if dirx < 0:
        stepsx = 0
    elif dirx > 0:
        stepsx = maxx - 1
    if diry < 0:
        stepsy = 0
    elif stepsy > 0:
        stepsy = maxy - 1
            
    for (ox,oy) in obs:
        if dirx < 0 and ox < x and oy == y:
            new_steps = x - ox - 1
            newy = y
            newx = ox + 1
        elif dirx > 0 and ox > x and oy == y:
            new_steps = ox - x - 1
            newy = y
            newx = ox - 1
        elif diry < 0 and ox == x and oy < y:
            new_steps = y - oy - 1
            newx = x
            newy = oy + 1
        elif diry > 0 and ox == x and oy > y:
            new_steps = oy - y - 1
            newx = x
            newy = oy - 1
        else:
            continue
        
        if steps is None or new_steps <= steps:
            steps = new_steps
            stepsx = newx
            stepsy = newy
            
    return steps, stepsx, stepsy

def rotate(dirx, diry):
    if dirx < 0:
        dirx = 0
        diry = -1
    elif dirx > 0:
        dirx = 0
        diry = 1
    elif diry < 0:
        dirx = 1
        diry = 0
    elif diry > 0:
        dirx = -1
        diry = 0
    return dirx, diry


def print_progress(obs, x,y, dirx, diry, maxx, maxy, visited):
    if dirx < 0:
        g = '<'
    elif dirx > 0:
        g = '>'
    elif diry < 0:
        g = '^'
    elif diry > 0:
        g = 'v'
    
    map = []
    for j in range(maxy):
        line = []
        for i in range(maxx):
            line.append(".")
        map.append(line)
    
    for (ox,oy) in obs:
        map[oy][ox] = "#"
    
    for (vx,vy) in visited.keys():
        map[vy][vx] = "x"
    
    map[y][x] = g
    
    print("---------------------")
    
    for l in map:
        str = ""
        for s in l:
            str += s
        print(str)
    
    #ignore = input("press enter")
    
(x,y,dir) = guard
(dirx,diry) = dir
visited = {}
visited[(x,y)] = True 

print_progress(obstacles, x, y, dirx, diry, maxx, maxy, visited)

while x >= 0 and y >= 0 and x < maxx and y < maxy:
    
    steps, newx, newy = find_min_o(obstacles, x, y, dirx, diry, maxx, maxy)
    print("guard(%d,%d) dir(%d,%d) new_guard(%d,%d)" % (x,y,dirx,diry,newx,newy))
    while x != newx or y != newy:
        x += dirx
        y += diry
        visited[(x,y)] = True

    print_progress(obstacles, x, y, dirx, diry, maxx, maxy, visited)
    
    if steps is None:
        break
    
    dirx, diry = rotate(dirx, diry)
        
print(len(visited))
