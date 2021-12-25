#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
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
for line in f_input:
    line = line.strip()
    raw = []
    for c in line:
        raw.append(int(c))
    
    octo.append(raw)


def octo_print(o):
    CSELECTED = '\33[7m'
    CEND = '\033[0m'

    for line in o:
        print_line = ""
        for c in line:
            if c == 0:
                print_line += CSELECTED + ("%d" % c) + CEND
            else:
                print_line += "%d" % c

        print("%s" % print_line)
    print("")

import time

octo_raws = len(octo)
octo_cols = len(octo[0])

fcounter = 0

all_flashed = False
iteration = 0

while not all_flashed:
    octo_print(octo)

    flashes = []

    # 1. energy level of each octopus increases by 1.
    for r in range(octo_raws):
        for c in range(octo_cols):
            energy = octo[r][c] + 1
            octo[r][c] = energy            
            if energy == 10:
                flashes.append((r,c))
                fcounter += 1

    # 2. octopus with an energy level greater than 9 flashes
    while flashes:
        r,c = flashes.pop()
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= octo_raws or nc >= octo_cols:
                    continue
                energy = octo[nr][nc] + 1
                octo[nr][nc] = energy
                if energy == 10:
                    flashes.append((nr,nc))
                    fcounter += 1
    
    n_flashed = 0
    for r in range(octo_raws):
        for c in range(octo_cols):
            if octo[r][c] > 9:
                octo[r][c] = 0
                n_flashed += 1
    
    if n_flashed == 100:
        all_flashed = True

    iteration += 1
            
    #time.sleep(0.5)
octo_print(octo)

print("Num flashed: %d, all flashed at %d" % (fcounter, iteration))