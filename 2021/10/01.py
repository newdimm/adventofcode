#!/usr/bin/python

test = True
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

score = 0

class RaiseType(Exception):
    def __init__(self, type, pos):
        self.type = type
        self.pos = pos
    def get_type(self):
        return self.type
    def get_pos(self):
        return self.pos

for line in f_input:
    line = line.strip()

    stacks = {}

    round = 1
    square = 2
    curly = 3
    triangle = 4

    open = 0
    close = 1

    decoder = {}
    decoder["("] = (round, open)
    decoder[")"] = (round, close)
    decoder["["] = (square, open)
    decoder["]"] = (square, close)
    decoder["{"] = (curly, open)
    decoder["}"] = (curly, close)
    decoder["<"] = (triangle, open)
    decoder[">"] = (triangle, close)

    counters = {}
    counters[round] = []
    counters[square] = []
    counters[curly] = []
    counters[triangle] = []

    costs = {}
    costs[round] = 3
    costs[square] = 57
    costs[curly] = 1197
    costs[triangle] = 25137

    try:
        pos = 0
        for c in line:
            type, action = decoder[c]
            if action == open:
                counters[type].append(pos)
            else: # close
                for counter_pos in counters.values():
                    if not counters[type] or \
                            counter_pos and counters[type][-1] < counter_pos[-1]:
                        raise RaiseType(type, pos)
                counters[type].pop()
            pos += 1

    except RaiseType as t:
        print("tripped on %s (%d) at pos %d line #%s#" % (line[t.get_pos()], t.get_type(), t.get_pos(), line))
        score += costs[t.get_type()]


print("score: %d" % score)
