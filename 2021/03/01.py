#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

bitmask = []

for line in f:
    pos = 0
    for bit in line:
        line = line.strip()

        if not bitmask:
            bitmask = [0] * len(line)

        if bit == '0':
            bitmask[pos] -= 1
        elif bit == '1':
            bitmask[pos] += 1
        pos += 1

pos = len(bitmask) - 1
gamma = 0
epsilon = 0
for bit in bitmask:
    if bit > 0:
        gamma += 1 << pos
    elif bit < 0:
        epsilon += 1 << pos
    pos -= 1

print("bitmask <%s> gamma %d * epsilon %d = %d" % (bitmask, gamma, epsilon, gamma * epsilon))



    
    



