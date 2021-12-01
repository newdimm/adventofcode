#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

prev = None
counter = 0
for line in f:
    num = int(line)
    if not prev is None:
        if prev < num:
            counter += 1
    prev = num

print("%d" % counter)




