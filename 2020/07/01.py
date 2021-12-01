#!/usr/bin/python

test = 0

if test:
    input_file = "simple_input.txt"
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

            try:
                bags_list = g[color]
            except KeyError:
                bags_list = []

            bags_list.append((container, weight))
            print("%s -- %d --> %s" % (color, weight, container))
            g[color] = bags_list

    target = "shiny gold"

    print("\n Searching for: %s\n" %target)

    q = []
    seen = {}

    q.append(target)
    seen[target] = True
    counter = -1

    while q:
        next_bag = q.pop()

        counter += 1

        print("--> %s" % next_bag)
        try:
            for (bag, weight) in g[next_bag]:

                if bag in seen:
                    print("XXX %s" % bag)
                    continue
                seen[bag] = True
                print("<-- %s" % bag)
                q.append(bag)
        except KeyError:
            pass


    print("Counter: %d" % counter)


