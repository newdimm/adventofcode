#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
stones = {}

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        start = line.split(" ")
        for s in start:
            try:
                count = stones[s]
            except:
                count = 0
            count += 1
            stones[s] = count
            
            

def do_blink(stones):
    new_stones = {}
    
    for s in stones.keys():
        count = stones[s]
                
        if s == '0':
            new_s = ['1']
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
            
            new_s = [s1, s2]
        else:
            number = int(s)
            new_s = ["%d" % (2024 * int(s))]
    
            
        for ns in new_s:
            try:
                old_count = new_stones[ns]
            except:
                old_count = 0
            new_stones[ns] = count + old_count
    
    
    return new_stones
        
    
        
print(stones)

blink = 1

    
while blink <= 75:
    stones = do_blink(stones)
    
    #print(stones)
    
    
    score = 0
    for s in stones.keys():
        score += stones[s]
    
    print("[%d]: stones:%d score:%d" % (blink, len(stones), score))
    #ignore = input("press enter")
    blink += 1
    
    
print("result: %d" % len(stones))
    
        

