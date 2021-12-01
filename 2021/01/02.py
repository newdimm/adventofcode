#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")


counter = 0
troika = []

for line in f:
    num = int(line)
    troika.append(num)
    if len(troika) <= 3:
        prev_sum = sum(troika)
        continue

    troika.pop(0)
    new_sum = sum(troika)
    if new_sum > prev_sum:
        counter += 1
    prev_sum = new_sum

print("%d" % counter)




