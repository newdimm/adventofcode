#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
    
map = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        stones = line.split(" ")

def do_blink(stones):
    i = 0
    while i < len(stones):
        s = stones[i]
        if s == '0':
            stones[i] = '1'
        elif (len(s) & 1) == 0:
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2:]
            
            pos=0
            while pos < len(s1) and s1[pos] == "0":
                pos += 1
                
            if pos != 0:
                pos = min(pos, len(s1)-1)
                
                s1 = s1[pos:]

            pos=0
            while pos < len(s2) and s2[pos] == "0":
                pos += 1
                
            if pos != 0:
                pos = min(pos, len(s2)-1)
                
                s2 = s2[pos:]
            
            stones[i] = s2
            stones.insert(i,s1)
            i += 1
        else:
            number = int(s)
            stones[i] = "%d" % (2024 * int(s))
        i += 1
        
    
        
print(stones)

blink = 1

seen = {}

while blink <= 25:
    do_blink(stones)
    
    #print(stones)
    
    new = 0
    for s in stones:
        try:
            last = seen[s]
        except KeyError:
            last = 0
            new += 1
        last += 1
        seen[s] = last
            
    print("[%d]: stones:%d new:%d seen:%d" % (blink, len(stones), new, len(seen)))
    #ignore = input("press enter")
    blink += 1
    
    
print("result: %d" % len(stones))
    
        

