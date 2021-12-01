#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"



def run_program(mem):
    acc_value = 0
    pos = 0

    while pos < len(mem) and mem[pos]:
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

    return (pos, acc_value)

with open(input_file, "r") as f:

    code = []

    for line in f:
        line = line.strip()


        (command, data) = line.split(" ")
        data = int(data)

        code.append((command, data))


    start = 0
    pos = 0
    while start < len(code) and pos != len(code):
        mem = code[:]
        while start < len(mem):
            (command, value) = mem[start]
            if command == "jmp":
                mem[start] = ("nop", value)
                break
            elif command == "nop":
                mem[start] = ("jmp", value)
                break
            start += 1

        start += 1

        (pos, acc_value) = run_program(mem)

print("Acc: %d found %d" % (acc_value, pos == len(code)))


