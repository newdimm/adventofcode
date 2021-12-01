#!/usr/bin/python

with open("input.txt", "r") as f:
    d = {}

    for line in f:
        n1 = int(line)

        for n2 in d.keys():
            n3 = 2020 - n2 - n1
            if n3 != n2 and n3 in d:
                print("%d+%d+%d == %d, %d*%d*%d=%d" % (n1, n2, n3, n1+n2+n3, n1, n2, n3, n1*n2*n3))

        d[n1] = 1

