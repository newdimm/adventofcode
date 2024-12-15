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
            sides[(x,y,"u")] = (x,y)
        if (x+1,y) not in neighs:
            sides[(x,y,"r")] = (x,y)
        if (x,y+1) not in neighs:
            sides[(x,y,"d")] = (x,y)
        if (x-1,y) not in neighs:
            sides[(x,y,"l")] = (x,y)
        
        for (nx,ny) in neighs:
            if (nx,ny) not in seen:
                seen[(nx,ny)] = True
                stack.append((nx,ny))
                
    s = {}
    while True:
        for x,y,dir in sides:
            if (x,y,dir) not in s:
                break
        if (x,y,dir) in s:
            break
        s[(x,y,dir)] = True
        
        ex,ey = sides[(x,y,dir)]
        if dir == "l":
            while (ex,ey-1,dir) in sides:
                nex,ney = sides[(ex,ey-1,dir)]
                del sides[(ex,ey-1,dir)]
                sides[(x,y,dir)] = (nex,ney)
                ex,ey = sides[(x,y,dir)]
        elif dir == "r":
            while (ex,ey+1,dir) in sides:
                nex,ney = sides[(ex,ey+1,dir)]
                del sides[(ex,ey+1,dir)]
                sides[(x,y,dir)] = (nex,ney)
                ex,ey = sides[(x,y,dir)]
        elif dir == "u":
            while (ex+1,ey,dir) in sides:
                nex,ney = sides[(ex+1,ey,dir)]
                del sides[(ex+1,ey,dir)]
                sides[(x,y,dir)] = (nex,ney)
                ex,ey = sides[(x,y,dir)]
        elif dir == "d":
            while (ex-1,ey,dir) in sides:
                nex,ney = sides[(ex-1,ey,dir)]
                del sides[(ex-1,ey,dir)]
                sides[(x,y,dir)] = (nex,ney)
                ex,ey = sides[(x,y,dir)]
                
    perimeter = len(sides)

    cost = area * perimeter
    #print("NEW  %s: sides=%s start=(%d,%d)" % (plant, sides, x,y))
    print("%s: area=%d perimeter=%d cost=%d" % (plant, area, perimeter, cost))
    
    full_cost += cost 

print("full_cost: %d" % full_cost)

## 852750 - too high
## 838694 - too lo