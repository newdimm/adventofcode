#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
    
map = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        map.append([int(x) for x in line])
        
def print_map(m):
    for l in m:
        s = ""
        for x in l:
            s += "%d" % x
        print(s)
    print("---------")
    
def get_neighbours(m, x, y, h):
    mx = len(m[0])
    my = len(m)
    
    result = []
    
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx = x+dx
        ny = y+dy
        
        if nx >= 0 and ny >= 0 and nx < mx and ny < my:
            if m[ny][nx] == h:
                result.append((nx,ny))
    
    return result
            
    
print_map(map)

scores = 0


for y in range(len(map)):
    l = map[y]
    for x in range(len(l)):
        h = l[x]
        if h == 0:
            queue = [(x,y,h)]
            
            nines = {}
            
            while queue:
                nx, ny, nh = queue.pop()

                nh += 1
                
                ns = get_neighbours(map, nx, ny, nh)
                
                if nh == 9:
                    for ninex, niney in ns:
                        nines[(ninex, niney)] = True
                elif ns:
                    for nx,ny in ns:
                        queue.append((nx,ny,nh))
            
            print("score(%d,%d) = %d" % (x,y,len(nines)))
            
            scores += len(nines)
                     
print("result: %d" % scores)            
