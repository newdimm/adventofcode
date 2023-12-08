#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

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


node = "AAA"
step = 0

while node != "ZZZ":
    for s in m:
        print("[%d] %s: %s" % (step, s, node))
        if node == "ZZZ":
            break
        left,right = n[node]
        if s == "L":
            node = left
        else:
            node = right
        step += 1

print("result", step)


