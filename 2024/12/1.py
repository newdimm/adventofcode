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
	perimeter = 0
	
	while stack:
		x,y = stack.pop(0)
		area += 1
		
		neighs = get_neighs(map, x, y)
		
		perimeter += 4 - len(neighs)
		
		for (nx,ny) in neighs:
			if (nx,ny) not in seen:
				seen[(nx,ny)] = True
				stack.append((nx,ny))

	cost = area * perimeter				
	print("%s: area=%d perimeter=%d cost=%d" % (plant, area, perimeter, cost))
	
	full_cost += cost 
		
print("full_cost: %d" % full_cost)