#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
    
map = []

button_a = "Button A: "
button_b = "Button B: "
prize = "Prize: "

costa = 3
costb = 1

games = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith(button_a):
            line = line[len(button_a):].strip()
            x,y = [x.strip() for x in line.split(",")]
            xx,dx = x.split("+")
            yy,dy = y.split("+")
            a = (int(dx),int(dy),costa)
        elif line.startswith(button_b):
            line = line[len(button_b):].strip()
            x,y = [x.strip() for x in line.split(",")]
            xx,dx = x.split("+")
            yy,dy = y.split("+")
            b = (int(dx),int(dy),costb)
        elif line.startswith(prize):
            line = line[len(prize):].strip()
            x,y = [x.strip() for x in line.split(",")]
            xx,px = x.split("=")
            yy,py = y.split("=")
            p = (int(px) + 10000000000000, int(py) + 10000000000000) 
            games.append((a,b,p))

print(games)

def factors_find(ax, bx, px, ay, by, py):
    
    ai = 0
    while ai <= 10000000:
        
        pxt = px - ai * ax
        
        if pxt < 0:
            break
            
        bi = pxt // bx
        
        if  pxt == bi * bx and ay*ai + by*bi == py:
            return ((ai,bi))
        
        ai += 1
    
    return None
    
total_cost = 0

for (a,b,p) in games:
    print("a=%s b=%s prize=%s" % (a,b,p))
    ax, ay, ac = a
    bx, by, bc = b
    px,py = p
    
    bi = (ay * px - ax * py) // (ay * bx - ax * by)
    ai = (px - bi * bx) // ax
    
    if px != ai*ax+bi*bx or py != ai*ay+bi*by:
        print("impossible")
    else:
        cost = ai * ac + bi * bc
        print("%d * %d + %d * %d = %d cost %d" % (ai,ax,bi,bx,ai*ax+bi*bx,cost))
        total_cost += cost


print("result: %d" % total_cost)
            
            

    
     
             
        
