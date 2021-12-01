#!/usr/bin/python

test = 0

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
            break

        del data[0]
        data.append(num)


print("Not valid: %d" % num);
target = num

with open(input_file, "r") as f:

    data = []
    data_sum = 0

    for line in f:
        line = line.strip()

        if not line:
            continue

        num = int(line)
        
        data.append(num)
        data_sum += num
        
        #print("sum(%s) == %d (need %d)" % (str(data), data_sum, target))
        
        if len(data) < 2:    
            continue
            
        if data_sum == target:
            break
        
        if data_sum < target:
            continue
        # data_sum > target
        while data_sum > target:
            data_sum -= data[0]
            del(data[0])
            
        if data_sum == target:
            break
            
if data_sum == target:
    print("Found: sum(%s)=%d,\nmin=%d + max=%d == %d" % (
        str(data), num, min(data), max(data), min(data) + max(data)))
else:
    print("Not found")
            
        
