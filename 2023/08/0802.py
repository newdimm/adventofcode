#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test2"

m = []
n = {}

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        if "=" in line:
            node, turns = line.split("=")
            node = node.strip()
            turns = turns.strip()
            turns = turns[1:-1]
            left, right = turns.split(",")
            left = left.strip()
            right = right.strip()
            n[node] = (left, right)
        else:
            m = line

nodes = []
for node in n.keys():
    if node[-1] == "A":
        nodes.append(node)
finish = False

def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return out

import math

def factors(num):
    l = {
    }
    for d in primes(math.floor(num)):
        while num % d == 0:
            if d not in l:
                l[d] = 1
            else:
                l[d] += 1
            num //= d 

    return l

periods = []

for node in nodes:
    cycles = {}
    step = 0

    print("start", node)

    phase_count = 0
    period_count = 0
   
    finish = False
    while not finish:
        mstep = 0
        for s in m:
            #print("[%d:%d] node %s" % (step, mstep, node))
            if node[-1] == 'Z':
                item = node + "-%d" % mstep
                if item in cycles:
                    phase, period = cycles[item]
                    if not period:
                        period = step - phase
                        cycles[item] = (phase, period)
                        period_count += 1
                        print("%s: %d:%d" % (item, phase, period))
                        periods.append(period)
                else:
                    phase = step
                    period = 0
                    cycles[item] = (phase, period)
                    phase_count += 1
                    print("%s: new %d" % (item, phase))

                if phase_count == period_count:
                    finish = True
                    break

            if s == "L":
                node = n[node][0]
            else:
                node = n[node][1]

            mstep += 1
            step += 1
    print("period %d cycles %s" % (step, cycles))


all_mults = {}

for p in periods:
    mults = factors(p)
    print("%d: %s" % (p, mults))
    for m,count in mults.items():
        if not m in all_mults:
            all_mults[m] = count
        else:
            all_mults[m] = max(count, all_mults[m])

print("all_mults", all_mults)
result = 1
for m,count in all_mults.items():
    result *= pow(m, count)
    
print("result", result)


