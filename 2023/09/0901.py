#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

result = 0

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        print(line)
        values = [int(x) for x in line.split(" ")]

        levels = []
        l = 0
        levels.append(values)
        finished = False
        while not finished:
            l += 1
            levels.append([0] * (len(levels[l-1]) - 1))

            for p in range(len(levels[l])):
                levels[l][p] = levels[l-1][p+1] - levels[l-1][p] 

            finished = True
            if len(levels[l]) > 1:
                for value in levels[l]:
                    if value != 0:
                        finished = False

        l = len(levels) - 1
        levels[l].append(0)
        while l >= 0:
            l -= 1
            levels[l].append(levels[l+1][-1] + levels[l][-1])
        result += levels[0][-1]

print("result", result)


