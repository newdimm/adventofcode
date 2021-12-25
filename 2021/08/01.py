#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

a,b,c,d,e,f,g = 0,1,2,3,4,5,6

disp = {
    0 : [a,b,c,e,f,g],
    1 : [c,f],  # 2
    2 : [a,c,d,e,g],
    3 : [a,c,d,f,g],
    4 : [b,d,c,f], # 4
    5 : [a,b,d,f,g],
    6 : [a,b,d,f,g],
    7 : [a,c,f], # 3
    8 : [a,b,c,d,e,f,g], #7
    9 : [a,b,c,d,f,g]
}

counter = 0

for line in f_input:
    input, output = line.strip().split(" | ")
    print("output: %s" % output)
    digits = output.split(" ")
    for d in digits:
        if len(d) in [len(disp[1]),
                      len(disp[4]),
                      len(disp[7]),
                      len(disp[8])]:
            print("%s" % d)
            counter += 1

print("counter: %d" % counter)
           
