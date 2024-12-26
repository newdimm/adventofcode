#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
edges = {}

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        f,t = line.split("-")
        
        try:
            flist = edges[f]
        except KeyError:
            flist = []
        flist.append(t)
        edges[f] = flist
            
        try:
            tlist = edges[t]
        except KeyError:
            tlist = []
        tlist.append(f)
        edges[t] = tlist

tripple = []
tripples = []

for f in edges.keys():
    flist = edges[f]
    print("[%s]: %s" % (f, flist))
    
    tripple.append(f)    
    for t1 in flist:
        tripple.append(t1)
        
        for t2 in flist:
            if t2 in tripple:
                continue
            tripple.append(t2)
            print("? %s" % tripple)
            
            is_good = True
            for t in tripple:
                l = edges[t]
                    
                for tt in tripple:
                    if tt == t:
                        continue
                    if tt not in l:
                        is_good = False
            if is_good:
                print("good")
                is_t = False
                for t in tripple:
                    if t.startswith("t"):
                        is_t = True
                if is_t:
                    good_tripple = tripple[:]
                    good_tripple.sort()
                    if good_tripple not in tripples:
                        tripples.append(good_tripple)
                    
            tripple.pop()            
        tripple.pop()
    tripple.pop()

for tri in tripples:
    print(tri)
    
print(len(tripples))