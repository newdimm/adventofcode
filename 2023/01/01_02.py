#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test2"

cal_sum = 0

digits = {
        'zero'  : 0,
        'one'   : 1,
        'two'   : 2,
        'three' : 3,
        'four'  : 4,
        'five'  : 5,
        'six'   : 6,
        'seven' : 7,
        'eight' : 8,
        'nine'  : 9
}

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        print(line)

        cal = 0

        pos = 0
        stop = False
        while pos < len(line) and not stop:
            if line[pos].isdigit():
                cal += int(line[pos]) * 10
                break
            for d,i in digits.items():
                if line[pos:].startswith(d):
                    print("left", d, i)
                    cal += i * 10
                    stop = True
                    break


            pos += 1

        pos = -1
        stop = False
        while pos >= -len(line) and not stop:
            if line[pos].isdigit():
                cal += int(line[pos])
                break
            for d,i in digits.items():
                if line[pos:].startswith(d):
                    print("right", d, i)
                    cal += i
                    stop  = True
                    break
            pos -= 1

        print(line, cal)

        cal_sum += cal

print("answer:", cal_sum)


        

