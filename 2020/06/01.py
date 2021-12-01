#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:
    result = 0

    form = [0]*26

    for line in f:
        line = line.strip()

        if not line:
            
            for answer in form:
                result += answer

            form = [0]*26
            continue

        for letter in line:
            form[ord(letter) - ord('a')] = 1


    for answer in form:
        result += answer

    print("result: %d" % result)


