#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]

walls={}
track={}
start=()
finish=()

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
            elif l == ".":
                track[(x,y)] = None
            elif l == "S":
                track[(x,y)] = 0
                start = (x,y)
            elif l == "E":
                track[(x,y)] = None
                finish = (x,y)
            else:
                raise("Unexpected symbol")
            x+= 1
            

        y += 1
my = y
        
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
    #print("= (%d,%d)" % (x,y))
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        tx = x + dx
        ty = y + dy
        if tx < 0 or ty < 0 or tx >= mx or ty >= my:
            continue
        if (tx,ty) in walls:
            #print("? (%d,%d)" % (tx,ty))
            for dtx,dty in [(0,1),(0,-1),(1,0),(-1,0)]:
                ttx = tx + dtx
                tty = ty + dty
                #print("  ?? (%d,%d)" % (ttx,tty))
                if ttx < 0 or tty < 0 or ttx >= mx or tty >= my:
                    continue
                if (ttx,tty) in track:
                    #print("  T %d -> %d" % (track[(ttx,tty)], track[(x,y)]))
                    if track[(ttx,tty)] > track[(x,y)]:
                        cheat = track[(ttx,tty)] - track[(x,y)] - 2
                        if cheat < 1:
                            continue
                        try:
                            cheat_count = cheats[(cheat)]
                        except KeyError:
                            cheat_count = 0
                        cheat_count += 1
                        cheats[(cheat)] = cheat_count
                        #print("found (%d,%d) %d -> %d gain %dps" % (tx, ty, track[(ttx,tty)], track[(x,y)], cheat))
                        #show(walls, track, start, finish, (tx, ty))
            continue
        if (tx,ty) in track and track[(tx,ty)] > track[(x,y)]:
            nx,ny = tx,ty
    
    #ignore = input("(%d,%d): press enter" % (x,y))        
    (x,y) = (nx,ny)
    


cheat_list = []
for cheat in cheats.keys():
    cheat_list.append((cheat, cheats[cheat]))
    
sorted(cheat_list)

above100 = 0
for cheat,count in cheat_list:
    print("%dps - %s times" % (cheat, count))
    if cheat >= 100:
        above100 += count
    
print("Best: %d" % max(cheats))
print("Above 100ps: %d" % above100)


# 403,404 - too low


