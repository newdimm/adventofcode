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
            
        map.append(line)

mx = len(map[0])
my = len(map)
            
def get_neighs(map, x,y):
	mx = len(map[0])
	my = len(map)

	plant = map[y][x]
	result = []
	
	for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
		nx = x + dx
		ny = y + dy
		
		if nx >= 0 and ny >= 0 and nx < mx and ny < my:
			if map[ny][nx] == plant:
				result.append((nx,ny))
	
	return result 

def find_start(map, seen):
	mx = len(map[0])
	my = len(map)
	
	for y in range(my):
		for x in range(mx):
			if (x,y) not in seen:
				return (x,y)
	return (-1,-1)
	
full_cost = 0
seen = {}

def print_sides(sides, mx ,my):
    map = []
    for y in range(my+1):
        l = []
        for x in range(mx+1):
            l.append(".")
        map.append(l)
        
    for (x,y) in sides.keys():
        nx,ny = sides[(x,y)]
        if y == ny:
            if x < nx:
                map[y][x] = "-"
            else:
                map[y][x] = "-"
        else:
            if y < ny:
                map[y][x] = "|"
            else:
                map[y][x] = "|"
                
    for line in map:
        s = ""
        for l in line:
            s += l
        print(s)

def optimise(sides, x,y, seen):
    
    count = len(sides)
    
    #print("%s: sides=%s start=(%d,%d)" % (plant, sides, x,y))
    #print_sides(sides,mx,my)
    
    for i in range(count):
        nx,ny = sides[(x,y)]
        seen[(x,y)] = True
        nnx,nny = sides[(nx,ny)]
        seen[(nx,ny)] = True
        while x == nx and nx == nnx or y == ny and ny == nny:
            del sides[(nx,ny)]
            sides[(x,y)] = (nnx,nny)
            nx,ny = nnx,nny
            nnx,nny = sides[(nx,ny)]
        x,y = nx,ny
        
    #print_sides(sides,mx,my)
    

while True:
    x,y = find_start(map, seen)
    plant = map[y][x]
    
    if x < 0:
        break
    
    stack = [(x,y)]
    seen[(x,y)] = True
    area = 0
    sides = {}
    start = (x,y)
    
    while stack:
        x,y = stack.pop(0)
        area += 1
        
        neighs = get_neighs(map, x, y)
        
        if (x,y-1) not in neighs:
            sides[(x,y)] = (x+1,y)
        if (x+1,y) not in neighs:
            sides[(x+1,y)] = (x+1,y+1)
        if (x,y+1) not in neighs:
            sides[(x+1,y+1)]= (x,y+1)
        if (x-1,y) not in neighs:
            sides[(x,y+1)] = (x,y)
        
        for (nx,ny) in neighs:
            if (nx,ny) not in seen:
                seen[(nx,ny)] = True
                stack.append((nx,ny))
                
    s = {}
    p = 1
    while True:
        for (x,y) in sides:
            if (x,y) not in s:
                break
        if (x,y) in s:
            #print("stop")
            break
        
        #print("[%d]: from (%d, %d)" % (p,x,y))
        optimise(sides, x,y, s)
        #print_sides(sides, mx, my)
        p += 1
    
    perimeter = len(sides)

    cost = area * perimeter
    #print("NEW  %s: sides=%s start=(%d,%d)" % (plant, sides, x,y))
    print("%s: area=%d perimeter=%d cost=%d" % (plant, area, perimeter, cost))
    
    full_cost += cost 

print("full_cost: %d" % full_cost)

## 852750 - too high
## 838694 - too lo