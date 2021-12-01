#!/usr/bin/python

test = 3

if test == 0:
    input_file = "simple_input.txt"
elif test == 1:
    input_file = "simple_input2.txt"
else:
    input_file = "input.txt"

data = []

with open(input_file, "r") as f:

    for line in f:
        line = line.strip()

        if not line:
            continue

        num = int(line)

        data.append(num)
        

data = sorted(data)


joltage = 0
s = {0:0, 1:0, 2:0, 3:0}

data.append(data[-1] + 3)

for j in data:
    diff = j - joltage
    print("%d (joltage %d) diff %d" % (j, joltage, diff))
    
    if diff > 3:
        print("Error")
        break
        
    s[diff] += 1
    joltage = j
 
print("%s: s[1]=%d * s[3]=%d == %d" %(
    str(s), s[1], s[3], s[1] * s[3]))
    
