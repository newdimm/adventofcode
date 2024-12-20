#!/bin/python3
import sys, time, heapq

fname = "1.txt"
target = 50

snakelen = 20

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        target = 100

walls={}
track={}
start=()
finish=()

buckets = {}

y = 0
mx = 0
my = 0

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
        x = 0
      
        mx = len(line)  
        for l in line:
            if l == "#":
                walls[(x,y)] = True
            else:
                track[(x,y)] = None
                if l == "S":
                    track[(x,y)] = 0
                    start = (x,y)
                elif l == "E":
                    finish = (x,y)
                bx = x // snakelen
                by = y // snakelen
                try:
                    b = buckets[(bx,by)]
                except:
                    b = []
                b.append((x,y))
                buckets[(bx,by)] = b
            x+= 1
            

        y += 1
my = y
mbx = mx // snakelen
mby = my // snakelen

def show(walls, track, start, finish, current):
    for y in range(my):
        str = ""
        for x in range(mx):
            if current and (x,y) == current:
                str += "@"
            elif (x,y) == start:
                str += "S"
            elif (x,y) == finish:
                str += "E"
            elif (x,y) in walls:
                str += "#"
            elif (x,y) in track:
                str += "."
            else:
                str += "?"
        print(str)
        
show(walls, track, start, finish, None)

pico = 1
(x,y) = start
while (x,y) != finish:
    found = False
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= mx or ny >= my:
            continue
        if (nx,ny) in walls:
            continue
        if (nx,ny) in track and track[(nx,ny)] is None:
            track[(nx,ny)] = pico
            found = True
            break
            
    if not found:
        raise("trouble, not found")
    (x,y) = (nx,ny)
    pico += 1
    
    #show(walls, track, start, finish, (x,y))
    #ignore = input("(%d,%d): press enter" % (x,y))
    
print("Normal time is %dps" % track[finish])

(x,y) = start
cheats={}
while (x,y) != finish:
    pico = track[(x,y)]    
    
    bx = x // snakelen
    by = y // snakelen
    
    print("[%d] bucket(%d,%d)" % (pico, bx,by))

    for dbx, dby in [(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
        nbx = bx + dbx
        nby = by + dby
        if (nbx,nby) in buckets:
            #print("  ? buckets(%d,%d)" % (nbx,nby))
            for nx,ny in buckets[(nbx,nby)]:
                
                dist = abs(x - nx) + abs(y-ny)
                #print("  ?? (%d,%d) dist %d" % (nx,ny,dist)) 
                if dist > snakelen:
                    continue
                #print("  ???? cheat %d - %d - %d == %d >= %d" % (track[(nx,ny)], pico, dist,track[(nx,ny)] - pico - dist, target))
                if track[(nx,ny)] >= pico + target + dist:
                    
                    cheat = track[(nx,ny)] - pico - dist
                    try:
                        cheat_count = cheats[cheat]
                    except KeyError:
                        cheat_count = 0
                    cheat_count += 1
                    cheats[cheat] = cheat_count
    
    
    #print("= (%d,%d)" % (x,y))
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        tx = x + dx
        ty = y + dy
        if tx < 0 or ty < 0 or tx >= mx or ty >= my:
            continue
        if (tx,ty) in walls:
            continue
        if (tx,ty) in track and track[(tx,ty)] > track[(x,y)]:
            nx,ny = tx,ty
    
    #ignore = input("(%d,%d): press enter" % (x,y))        
    (x,y) = (nx,ny)
    


cheat_list = []
for cheat in cheats.keys():
    cheat_list.append((cheat, cheats[cheat]))
    
sorted(cheat_list)

print(cheats)

target_count = 0
for cheat,count in cheat_list:
    print("%dps - %s times" % (cheat, count))
    target_count += count
    
print("Best: %d" % max(cheats))
print("Above 100ps: %d" % target_count)


# 403,404 - too low


