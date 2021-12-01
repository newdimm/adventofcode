#!/usr/bin/python

test = False

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:
    num_valid = 0

    for line in f:
        letter_min = int(line[0 : line.find("-")])
        line = line[line.find("-") + 1:]
        letter_max = int(line[0 : line.find(" ")])
        line = line[line.find(" ") + 1:]
        letter = line[0]
        line = line[line.find(":") + 1:].lstrip()

        counter = 0

        for l in line:
            if l == letter:
                counter += 1

        if counter >= letter_min and counter <= letter_max:
            num_valid += 1


    print("Valid passwords: %d" % num_valid)


