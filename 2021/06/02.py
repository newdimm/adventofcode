#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

fishes = [0] * 9

start = f.readline().split(",")
for fish in start:
    fishes[int(fish)] += 1

for day in range(256):
    #print("%s = %d" % (fishes, sum(fishes)))
    newborns = fishes[0]
    for age in range(8):
        fishes[age] = fishes[age+1]
    fishes[8] = newborns
    fishes[6] += newborns

#print("fishes: %d" % sum(fishes))

    