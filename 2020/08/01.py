#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

acc_value = 0

with open(input_file, "r") as f:

    mem = []

    for line in f:
        line = line.strip()


        (command, data) = line.split(" ")
        data = int(data)

        mem.append((command, data))


    pos = 0
    while mem[pos]:
        command, data = mem[pos]
        print("%s :: %d" % (command, data))
        mem[pos] = 0
        if command == "acc":
            acc_value += data
            pos += 1
        elif command == "jmp":
            pos += data
        elif command == "nop":
            pos += 1 
        else:
            print("Unknown command %s data %d" %(command, data))

print("Acc: %d" % acc_value)


