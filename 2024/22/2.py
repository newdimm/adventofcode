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
seqs = []

print("build sequences") 
for num in nums:
        
    seq = []
    
    n = num
    prev = n % 10
    for i in range(2000):
        n = secret(n)
        new = n % 10
        diff = new - prev
        seq.append((diff, new))
        prev = new
    
    seqs.append(seq)
    
    print("%d : %d" % (num, n))
    total += n


print("find fours")

fours = {}

encode = {
    0 : 0,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    -1 : 0x11,
    -2 : 0x12,
    -3 : 0x13,
    -4 : 0x14,
    -5 : 0x15,
    -6 : 0x16,
    -7 : 0x17,
    -8 : 0x18,
    -9 : 0x19,
}

def encode4(four):
    return (encode[four[0]] << 24) | \
      (encode[four[1]] << 16) | \
      (encode[four[2]] <<  8) | \
      (encode[four[3]] <<  0)

decode = {}
for key in encode:
    value = encode[key]
    decode[value] = key


def decode4(key):
    four = []
    four.append(decode[(key >> 24)])
    four.append(decode[(key >> 16) & 0xff])
    four.append(decode[(key >>  8) & 0xff])
    four.append(decode[(key >>  0) & 0xff])
    
    return four

candidates = {}


pernum = {}
index = 0
for seq in seqs:
    
    perseq = {}
        
    four = []
    seen = {}
    for (s,price) in seq:
        four.append(s)
        if len(four) >= 4:
            key = encode4(four)
            if not key in seen:
                if key in fours:
                    candidates[key] = True
                    prev = fours[key]
                else:
                    prev = 0
                fours[key] = prev + price
                seen[key] = True
                perseq[key] = price
            four.pop(0)
    
    #print(",".join([str(x) for x,price in seq]))
    
    pernum[nums[index]] = perseq
    index += 1


for check in ([-2,1,-1,3],[1,-3,5,1]):
    key = encode4(check)
    print("%s key=0x%x" % (check, key))
    for index in range(len(nums)):
        num = nums[index]
        perseq = pernum[num]
        if key in perseq:
            print("  [%d]: %d" % (num, perseq[key]))
        else:
            print("  [%d]: none" % num)
    print("total: %d" % fours[key])
            
        
    

max_key = None
max_value = 0 
for c in candidates.keys():
    if fours[c] > max_value:
        max_value = fours[c]
        max_key = c
        
print("key: %d" % max_key)
four = decode4(max_key)
    
print("At most %d bananas with sequence %s" % (max_value, four))
        

