#!/usr/bin/python

test = 1

if test:
    input_file = "simple_input.txt"
    pre = 5
else:
    input_file = "input.txt"
    pre = 25


def valid(data, num):

    d = {}

    for value in data:
        d[value] = 1


    for value in d.keys():
        if value <= num and (num - value) in d and d[num-value] != value:
            return True

    return False


with open(input_file, "r") as f:

    data = []

    for line in f:
        line = line.strip()

        if not line:
            continue

        num = int(line)

        if len(data) < pre:
            data.append(num)
            continue


        if not valid(data, num):
            print("Not valid: %d" % num);
            break

        del data[0]
        data.append(num)
        
