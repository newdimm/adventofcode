#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        mx=71
        my=71
        symulate=1024
        fx=70
        fy=70
    else:
        mx=7
        my=7
        symulate=12
        fx=6
        fy=6


bytes = []


nmx = 0
nmy = 0
with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        x,y = [int(x) for x in line.split(",")]
        bytes.append((x,y))
        
        nmx=max(x,nmx)
        nmy=max(y,nmy)
        



def show(corrupt):
    for y in range(my):
        str = ""
        for x in range(mx):
            if (x,y) in corrupt:
                str += "#"
            else:
                str += "."
        print(str)

def get_steps(x,y, corrupt, seen):
    result = []
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx = x + dx
        ny = y + dy
        
        if nx < 0 or ny < 0 or nx >= mx or ny >= my:
            continue
            
        if (nx,ny) in corrupt or (nx,ny) in seen:
            continue
            
        result.append((nx,ny))
    return result


corrupt = {}

index = 0
for x,y in bytes:
    corrupt[(x,y)] = True
    
    if index >= symulate:
        
        if index == symulate:
            show(corrupt)
            
        print("byte[%d]=(%d,%d)" % (index,x,y))
    
        stack = [(0,0,0)]
        finish = (fx,fy)
        seen = {}
        found = False
        
        while stack:
            x,y,step = stack.pop(0)
            
            if (x,y) == finish:
                print("step: %d" % step)
                found = True
                break
            
            if (x,y) in seen:
                continue
            seen[(x,y)] = True
            
            paths = get_steps(x,y,corrupt, seen)
            for nx,ny in paths:
                stack.append((nx,ny,step+1))
        
        if not found:
            print("byte[%d]=(%d,%d) has closed the path" % (index, bytes[index][0], bytes[index][1]))
            break

    index += 1




