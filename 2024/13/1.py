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
            p = (int(px),int(py))
            games.append((a,b,p))

print(games)

def factors_find(a, b, p):
    factors = []
    
    ai = 0
    while ai <= 100:
        bi = 0
        
        pt = p - ai * a
        
        if pt < 0:
            break
            
        bi = pt // b
        
        if bi <= 100 and pt == bi * b:
            factors.append((ai,bi))
        
        ai += 1
    
    return factors
    
total_cost = 0

for (a,b,p) in games:
    print("a=%s b=%s prize=%s" % (a,b,p))
    ax, ay, ac = a
    bx, by, bc = b
    px,py = p
    
    fx = factors_find(ax, bx, px)
    fy = factors_find(ay, by, py)
    
    fs = []
    for f in fx:
        if f in fy:
            fs.append(f)
    
    cost_min = None
    cost_index = -1
    
    for (ai,bi) in fs:
        cost = ai * ac + bi * bc   
        if cost_min is None or cost_min > cost:
            cost_min = cost
            
    if cost_min is not None:
        print("cost: %d" % cost)
        total_cost += cost_min
    else:
        print("not possible")
        
print("result: %d" % total_cost)
            
            

    
     
             
        
