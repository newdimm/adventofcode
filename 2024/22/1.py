#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
nums = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        nums.append(int(line))
        

def secret(num):
    num ^= num * 64
    num %= 16777216
    
    num ^= num // 32
    num %= 16777216
    
    num ^= num * 2048
    num %= 16777216
    
    return num
    

total = 0
for num in nums:
    print("%d" % num)
    
    n = num
    for i in range(2000):
        n = secret(n)
        
    print("[2000]: %d" % n)
    total += n
    
print("result: %d" % total)
        

