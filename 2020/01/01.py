#!/usr/bin/python

with open("input.txt", "r") as f:
    d = {}

    for line in f:
        number = int(line)
        pair = 2020 - number

        if pair in d:
            print("%d+%d == %d, %d*%d=%d" % (number, pair, number+pair, number, pair, number*pair))
            break

        d[number] = 1

