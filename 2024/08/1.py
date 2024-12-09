#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
map = []
ants = {}
lants = {}

mx,my = 0,0
x,y = 0,0

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        ll = []
        x = 0
        for l in line:
            if l != ".":
                try:
                    a = ants[l]
                except KeyError:
                    a = []
                a.append((x,y))
                ants[l] = a
                lants[(x,y)] = l
            ll.append(l)
            x += 1
            
        map.append(ll)
        y += 1

mx = len(map[0])
my = len(map)

anodes = {}

def new_anode(x,y):
    global anodes
    global mx
    global my
    
    if x >= 0 and x < mx and y >= 0 and y < my:
        anodes[(x,y)] = True
        return True
    
    return False
 
'''
7.4
4,6

x=4-3 = 1
y=4-2 = 2

a1=4,2 a2=3,3
00123456789
1..........
2....1......
3...2.......
4..........
5..........
6..........
7..........
8..........
9..........
'''
        
def print_step(sym, ants, nodes):
    global mx
    global my
    
    for y in range(my):        
        l = ""
        for x in range(mx):
            is_ant = (x,y) in ants
            is_anode = (x,y) in nodes
            if is_ant and is_anode:
                l += "@"
            elif is_ant:
                l += sym
            elif is_anode:
                l += "#"
            else:
                l += "."
        print(l)

for letter in ants.keys():
    ant = ants[letter]
    
    if len(ant) < 2:
        continue
    
    print("%s: %s" % (letter, ant))
    
    for i in range(len(ant)):
        for j in range(i+1, len(ant)):
            a1x, a1y = ant[i]
            a2x, a2y = ant[j]

            dx = a1x - a2x 
            dy = a1y - a2y

            n1x,n1y = a2x,a2y
            while new_anode(n1x, n1y):
                n1x -= dx
                n1y -= dy
            
            n2x,n2y = a1x,a1y
            while new_anode(n2x,n2y):
                n2x += dx
                n2y += dy
                
            #print("(%d,%d) vs (%d,%d) produce (%d,%d) and (%d,%d)" % (a1x,a1y,a2x,a2y,n1x,n1y,n2x,n2y))
            
            #print_step(letter, [(a1x,a1y), (a2x,a2y)], [(n1x,n1y),(n2x,n2y)])
    

for y in range(my):        
    
    l = ""
    for x in range(mx):
        is_ant = (x,y) in lants.keys()
        is_anode = (x,y) in anodes
        if is_ant and is_anode:
            l += "@"
        elif is_ant:
            l += lants[(x,y)]
        elif is_anode:
            l += "#"
        else:
            l += "."
    print(l)

#print("Antennaes: %d : %s" % (len(lants), lants))
print("Anodes: %d : %s" % (len(anodes), anodes))
              
# 376 is not right   
