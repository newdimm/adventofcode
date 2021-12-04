#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

depth = 0
pos = 0
aim = 0

def forward(depth, pos, aim, value):
    return depth + value * aim, pos + value, aim

def up(depth, pos, aim, value):
    if value > aim:
        return depth, pos, 0
    else:
        return depth, pos, aim - value

def down(depth, pos, aim, value):
    return depth, pos, aim + value

commands = {"forward" : forward,
            "down" : down,
            "up" : up}
for line in f:
    cmd, value = line.split(" ")

    if cmd in commands:
        func = commands[cmd]
        depth, pos, aim = func(depth, pos, aim, int(value))
    else:
        print("unknown command <%s> value <%s> line <%s>" % (cmd, value, line))
        break

print("depth=%d * pos=%d = %d (aim %d)" % (depth, pos, depth*pos, aim))

    
    



