#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

seeds = []

def import_seeds(s):
    global seeds

    seeds = [int(x) for x in s.split(" ")]

seed_maps = {
}

current_from = ""
current_to = ""

def import_map(m):
    global current_from
    global current_to
    global seed_maps

    f, ignore, t = m.split("-")

    current_from = f
    current_to = t

    seed_maps[current_from] = (current_to, [])

    print("new map: %s -> %s" % (current_from, current_to))

def import_range(r):
    global seed_maps

    r_to, r_from, r_num = [int(x) for x in r.split(" ")]

    if r_num > 0:
        map_from = r_from
        map_to = r_from + r_num - 1
        delta = r_to - r_from
        print("range %d:%d delta %d" % (map_from, map_to, delta))

        t, ranges = seed_maps[current_from]
        ranges.append((map_from, map_to, delta))


with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        print(line)

        if line.startswith("seeds: "):
            import_seeds(line[7:])
            print("seeds", seeds)
            continue

        if line.endswith(" map:"):
            import_map(line[0:-5])
            continue

        import_range(line)


print("Lets walk")

min_result = seeds[0]

for s in seeds:
    print("seed:", s)
    pos = "seed"
    result = s

    while pos:
        print("->", pos, "[%d]" % result)

        try:
            next_pos, ranges = seed_maps[pos]
        except KeyError:
            print("done")
            break

        for (f,t,delta) in ranges:
            if result >= f and result <= t:
                print(result, ":->:", result + delta)
                result += delta
                break

        pos = next_pos

    min_result = min(result, min_result)

print("Min result:", min_result)
