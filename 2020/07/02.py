#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input2.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:

    g = {}

    for line in f:
        line = line.strip()

        # dark purple bags contain 3 dotted teal bags, 1 wavy tomato bag.
        if line[-1] == ".":
            line = line[:-1]

        edges = line.split(" bags contain ");
        container = edges[0]
        content = edges[1].split(", ")

        
        try:
            bags_list = g[container]
        except KeyError:
            bags_list = []

        for bag in content:
            first_space = bag.find(" ")
            weight = bag[:first_space]
            if weight == "no":
                print("%s is a leaf" % container)
                continue
            weight = int(weight)

            color = bag[first_space + 1:]

            if color.endswith("bags"):
                color = color[:-5]
            elif color.endswith("bag"):
                color = color[:-4]

            bags_list.append((color, weight))
            print("%s -- %d --> %s" % (container, weight, color))

        g[container] = bags_list

    target = "shiny gold"

    print("\n Searching for: %s\n" % target)

    q = []
    seen = {}

    q.append((target, 1))
    counter = 0

    while q:
        (next_bag, mult) = q.pop()

        print("--> %s" % next_bag)

        try:
            for (bag, weight) in g[next_bag]:
                counter += weight * mult
                q.append((bag, weight * mult))
        except KeyError:
            pass


    print("Counter: %d" % counter)


