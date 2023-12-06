#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        print(line)

        if line.startswith("Time: "):
            ignore, line = line.split(":")
            times = [int(x) for x in line.split(" ") if x]
            continue


        if line.startswith("Distance: "):
            ignore, line = line.split(":")
            dists = [int(x) for x in line.split(" ") if x]
            continue

        
print("times", times)
print("dists", dists)

result = 1
pos = 0
while pos < len(times):
    t = times[pos]
    d = dists[pos]

    min_speed = d // t + 1
    max_speed = min(d, t - 1)
    counter = 0
    for s in range(min_speed, max_speed + 1):
        if (t - s) * s > d:
            counter += 1

    print("%d * %d == %d" % (result, counter, result * counter))
    result *= counter 
    pos += 1

print("result", result)
        
