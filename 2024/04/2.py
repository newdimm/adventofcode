#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 
                
total = 0

m = []

result = {}

with open(fname) as f:
    for line in f:
        line = line.strip()
        m.append(line)
        
mx = len(m[0])
my = len(m)
print("NAX-X %d MAX-Y %d" % (mx,my))

token = "MAS"
token_pos = 0
foundx = 0
foundy = 0
crossx = 0
crossy = 0

def do_match(m,x,y):
    global token
    global token_pos
    global result
    global foundx
    global foundy
    global crossx
    global crossy
    
    if m[y][x] == token[token_pos]:
        if token_pos == 0:
            (foundx, foundy) = (x,y)
            token_pos += 1
        elif token_pos == 1:
            crossx = x
            crossy = y
            token_pos += 1
        elif token_pos + 1 == len(token):
            result[(foundx, dx, foundy, dy)] = (crossx, crossy)
            token_pos = 0
        else:
            token_pos += 1
    else:
        if token_pos != 0:
            token_pos = 0
            # do it again from position 0
            do_match(m,x,y)

        
for (dx,dy) in [(1,1), (1,-1), (-1,1), (-1,-1)]:
    
    for startx in range(mx):
        for starty in range(my):
            if starty != 0 and startx !=0 and startx+1 != mx and starty+1 != my:
                continue
            
            (x,y) = (startx, starty)
        
            token_pos = 0
            while x >=0 and x < mx and y >= 0 and y < my:
                do_match(m,x,y)
                  
                x += dx
                y += dy

crosses = {}
        
v = []
for vy in range(my):
    line = []
    for vx in range(mx):
        line.append(" ")
    v.append(line)
    
crosses = {}

for (x,dx,y,dy) in result.keys():
    (crossx, crossy) = result[(x,dx,y,dy)]
    try:
        c = crosses[(crossx, crossy)]
    except KeyError:
        c = []
        
    c.append((x,dx,y,dy))
    crosses[(crossx, crossy)] = c
        
    s = ""
    for i in range(len(token)):
        s += m[y + dy * i][x+dx*i]
        v[y + dy * i][x+dx*i] = m[y + dy * i][x+dx*i] 
    print("(%d,%d) [%d,%d] -> %s" % (x,y, dx,dx, s))
    
for vy in v:
    str = ""
    for vx in vy:
        str += vx
    print(str)

v = []
for vy in range(my):
    line = []
    for vx in range(mx):
        line.append(" ")
    v.append(line)
    
print("--------------------")
counts = 0
    
for (crossx, crossy) in crosses.keys():
    entries = crosses[(crossx, crossy)]
    
    if len(entries) >= 2:
        counts += 1
        for entry in entries:
            (x,dx,y,dy) = entry
            
            for i in range(len(token)):
                v[y + dy * i][x+dx*i] = m[y + dy * i][x+dx*i]

for vy in v:
    str = ""
    for vx in vy:
        str += vx
    print(str)

                 
print(counts)
