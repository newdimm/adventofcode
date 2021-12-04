#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

depth = 0
pos = 0

def forward(depth, pos, value):
    return depth, pos + value

def up(depth, pos, value):
    if value > depth:
        return 0, pos
    else:
        return depth - value, pos

def down(depth, pos, value):
    return depth + value, pos

commands = {"forward" : forward,
            "down" : down,
            "up" : up}
for line in f:
    cmd, value = line.split(" ")

    if cmd in commands:
        func = commands[cmd]
        depth, pos = func(depth, pos, int(value))
    else:
        print("unknown command <%s> value <%s> line <%s>" % (cmd, value, line))
        break

print("depth=%d * pos=%d = %d" % (depth, pos, depth*pos))

    
    



