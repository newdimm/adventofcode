#!/usr/bin/python

test = False
if test:
    f_input = open("input.test3")
else:
    f_input = open("input")

class RaiseType(Exception):
    def __init__(self, type, pos):
        self.type = type
        self.pos = pos
    def get_type(self):
        return self.type
    def get_pos(self):
        return self.pos

octo = []

edges = {}

for line in f_input:
    line = line.strip()

    e1,e2 = line.split("-")

    for e,c in [(e1, e2), (e2, e1)]:
        try:
            adj_list = edges[e]
        except:
            adj_list = []
        adj_list.append(c)
        edges[e] = adj_list

print(edges)

counter = 0

tree = []
tree.append(["start"])
path = []

while tree:
    print("path<%s> heads<%s> tree<%s>" % ("->".join(path), tree[-1], tree))

    heads = tree[-1]

    if not heads:
        print("backtrack")
        tree.pop()
        if path:
            path.pop()
        continue

    head = heads.pop()
    path.append(head)
    next = edges[head]

    print("head<%s> path<%s> next<%s>" % (head, "->".join(path), next))

    selected = []

    for e in next:
        if e.islower() and e in path:
            continue
        elif e == "end":
            counter += 1
            print("%d path<%s>" % (counter, path))
        else:
            selected.append(e)

    tree.append(selected)

        

        

#     start
#     /   \
# c--A-----b--d
#     \   /
#      end

print("counter: %d" % counter)