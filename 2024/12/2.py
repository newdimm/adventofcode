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

seen = {}

def find_start(map, seen):
	mx = len(map[0])
	my = len(map)
	
	for y in range(my):
		for x in range(mx):
			if (x,y) not in seen:
				return (x,y)
	return (-1,-1)
	
full_cost = 0

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
				
	(x,y) = start
	count = len(sides)
	
	print("%s: sides=%s start=(%d,%d)" % (plant, sides, x,y))
	
	for i in range(count*2):
		nx,ny = sides[(x,y)]
		nnx,nny = sides[(nx,ny)]
		while x == nx and nx == nnx or y == ny and ny == nny:
			del sides[(nx,ny)]
			sides[(x,y)] = (nnx,nny)
			nx,ny = nnx,nny
			nnx,nny = sides[(nx,ny)]
		x,y, = nx,ny
	perimeter = len(sides)
			
			

	cost = area * perimeter				
	print("%s: area=%d perimeter=%d cost=%d" % (plant, area, perimeter, cost))
	
	full_cost += cost 
		
print("full_cost: %d" % full_cost)

## 852750 - too high