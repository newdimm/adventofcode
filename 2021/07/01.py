#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

crabs = list(map(int, f.readline().split(",")))
min_crab = min(crabs)
max_crab = max(crabs)
crabs_count = len(crabs)

positions = [0] * (max_crab - min_crab + 1)
weight_min_crab = 0

for crab in crabs:
    positions[crab] += 1
    weight_min_crab += crab - min_crab

print("positions: %s " % positions)
print("weight[0]: %d" % weight_min_crab)

min_weight = weight_min_crab
min_weight_crab = min_crab

total_count = positions[0]
weight = weight_min_crab
for index in range(1, max_crab - min_crab + 1):
    weight += total_count
    weight -= (crabs_count - total_count)
    print("weight[%d]: %d" % (index, weight))
    if weight < min_weight:
        min_weight = weight
        min_weight_crab = index + min_crab

    total_count += positions[index]

print("min weight %d crab %d" % (min_weight, min_weight_crab))

    