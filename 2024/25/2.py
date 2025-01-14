#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]

level = 0
max_level = 6
pins = 0

keys = []
locks = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue

        pin = 0
        for index in range(len(line)):
            if line[index] == "#":
                pin |= (1 << index * 4)
        
        pins += pin
        
        if level == max_level:
            pins -= 0x11111
            if line == "#####":
                keys.append(pins)
            else:
                locks.append(pins)

            pins = 0
            level = 0
        else:
            level += 1


print("keys=", [hex(i) for i in keys])
print("locks=", [hex(i) for i in locks])

def hexise(p):
    return [hex(i) for i in p]

fit_pairs = {}

for k in keys:
    for l in locks:
        s = k + l
        
        #print("%s + %s == %s" % (hex(k), hex(l), hex(s)))
              
        fits = True
        while s:
            if (s & 0xf) >= 6:
                fits = False
                break
            s >>= 4
        
        if fits:
            print("%s + %s fit" % (hex(k), hex(l)))
            fit_pairs[(k,l)] = 1
        else:
            print("%s + %s DO NOT fit" % (hex(k), hex(l)))
        
print("fitting pairs: %d" % len(fit_pairs))