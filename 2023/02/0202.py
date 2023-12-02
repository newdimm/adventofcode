#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

games_sum = 0

limits = {
        'red' : 12,
        'blue' : 14,
        'green' : 13
}

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        line = line[5:]
        game_no, line = line.split(":", 2)
        game_no = int(game_no)
        line = line.strip()
        
        print(game_no)

        games = line.split(";")

        maxes = {
                'red': 0,
                'green' : 0,
                'blue' : 0
        }

        for g in games:
            cubes = g.split(",")
            for c in cubes:
                c = c.strip()
                count, colour = c.split(" ")
                count = int(count)
                limit = limits[colour]

                print(count, colour, limit)

                maxes[colour] = max(maxes[colour], count)

        power = maxes['red'] * maxes['blue'] * maxes['green']

        games_sum += power


print("answer:", games_sum)


        

