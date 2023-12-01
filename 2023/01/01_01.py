#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

cal_sum = 0

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        cal = 0

        pos = 0
        while pos < len(line):
            if line[pos].isdigit():
                cal += int(line[pos]) * 10
                break
            pos += 1

        pos = -1
        while pos >= -len(line):
            if line[pos].isdigit():
                cal += int(line[pos])
                break
            pos -= 1

        print(line, cal)

        cal_sum += cal

print("answer:", cal_sum)


        

