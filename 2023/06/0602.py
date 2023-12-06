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
            x = ""
            for l in line:
                if l != " ":
                    x += l
            times = int(x)
            continue


        if line.startswith("Distance: "):
            ignore, line = line.split(":")
            x = ""
            for l in line:
                if l != " ":
                    x += l
            dists = int(x)
            continue

        
print("times", times)
print("dists", dists)

result = 1
pos = 0

t = times
d = dists

min_speed = d // t + 1
max_speed = min(d, t - 1)
counter = 0

start = 0
for s in range(min_speed, max_speed + 1):
    if (t - s) * s > d:
        start = s
        break

        
stop = 0
for s in range(max_speed + 1, min_speed, -1):
    if (t - s) * s > d:
        stop = s
        break

counter = stop - start + 1


print("%d * %d == %d" % (result, counter, result * counter))
result *= counter 


print("result", result)
        
