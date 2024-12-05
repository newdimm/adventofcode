#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 
            
after = {}
before = {}
orders = []
    
with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if line and "|" in line:
            a,b = [int(x) for x in line.split("|")]
            try:
                l = after[a]
            except KeyError:
                l = []
            l.append(b)
            after[a] = l
            
            try:
                l = before[b]
            except KeyError:
                l = []
            l.append(a)
            before[b] = l
        elif "," in line:
            o = [int(x) for x in line.split(",")]
            orders.append(o)
    
middles = 0
        
for o in orders:
    wrong = {}
    is_good = True
    m = 0
    
    for i in range(len(o)):
        x = o[i]

        if x in wrong:
            is_good = False
            break
        try:
            for w in before[x]:
                wrong[w] = True
        except KeyError:
            pass
        if i == len(o) // 2:
            m = x
        
    if is_good:
        print("YES %s middle %d" % (o, m))
        middles += m
    else:
        print("NO  %s" % (o))
        
print("Result: %d" % middles)        
    