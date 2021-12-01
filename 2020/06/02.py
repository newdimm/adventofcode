#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:
    result = 0

    form = [0]*26
    count = 0

    for line in f:
        line = line.strip()

        if not line:
            
            for answer in form:
                if count == answer:
                    result += 1

            form = [0]*26
            count = 0
            continue

        count += 1
        for letter in line:
            form[ord(letter) - ord('a')] += 1


    for answer in form:
        if count == answer:
            result += 1

    print("result: %d" % result)


