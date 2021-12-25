#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

scores = []

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

    encode = {}
    encode[(round, close)] = ")"
    encode[(square, close)] = "]"
    encode[(curly, close)] = "}"
    encode[(triangle, close)] = ">"

    counters = {}
    counters[round] = []
    counters[square] = []
    counters[curly] = []
    counters[triangle] = []

    costs = {}
    costs[round] = 1
    costs[square] = 2
    costs[curly] = 3
    costs[triangle] = 4

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
        continue

    score = 0
    complete = ""

    #print(counters)

    max_pos = -1
    max_type = 0
    for t,p in counters.items():
        if p and p[-1] > max_pos:
            max_pos = p[-1]
            max_type = t

    while max_type:
        #print("%s %d" % (encode[(max_type, close)], max_pos))
        counters[max_type].pop()
        score *= 5
        score += costs[max_type]
        complete += encode[(type, close)]

        max_pos = -1
        max_type = 0
        for t,p in counters.items():
            if p and p[-1] > max_pos:
                max_pos = p[-1]
                max_type = t

    print("score %d complete $$%s$$ ##%s##" % (score, complete, line))
    scores.append(score)


scores.sort()

print("score: %d" % scores[len(scores)/2])
