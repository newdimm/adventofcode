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

token = 0
for day in range(256):
    #print("[%d] %s = %d" % (token, fishes, sum(fishes)))
    fishes[(token + 7) % 9] += fishes[token]
    token = (token + 1) % 9

#print("fishes: %d" % sum(fishes))

    