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

token = "XMAS"
token_pos = 0
foundx = 0
foundy = 0

def do_match(m,x,y):
    global token
    global token_pos
    global result
    global foundx
    global foundy
    
    if m[y][x] == token[token_pos]:
        if token_pos == 0:
            (foundx, foundy) = (x,y)
            token_pos += 1
        elif token_pos + 1 == len(token):
            result[(foundx, dx, foundy, dy)] = True
            token_pos = 0
        else:
            token_pos += 1
    else:
        if token_pos != 0:
            token_pos = 0
            # do it again from position 0
            do_match(m,x,y)

        
for (dx,dy) in [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]:
    
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
        
v = []
for vy in range(my):
    line = []
    for vx in range(mx):
        line.append(" ")
    v.append(line)
    
for (x,dx,y,dy) in result.keys():
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
        
            
print(len(result))
