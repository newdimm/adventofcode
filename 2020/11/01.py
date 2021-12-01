#!/usr/bin/python

test = 1

if test == 0:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"


def print_room(room):
    for row in room:
        str_row = ""
        for c in row:
            str_row += c
        print(str_row)

def count_occupied(room, r, c):
    num_occupied = 0

    if r == 0:
        rows = [r, r + 1]
    elif r == len(room) - 1:
        rows = [r-1, r]
    else:
        rows = [r-1, r, r+1]

    if c == 0:
        cols = [c, c+1]
    elif c == len(room[r]) - 1:
        cols = [c-1, c]
    else:
        cols = [c-1, c, c+1]

    for rr in rows:
        for cc in cols:
            if room[rr][cc] == "#":
                num_occupied += 1

    return num_occupied

def to_be_empty(room, r, c):
    # If a seat is occupied (#) and 
    # four or more seats adjacent to it are also occupied,
    # the seat becomes empty.

    if room[r][c] != "#":
        return False

    num_occupied = count_occupied(room, r, c)

    # subtract seat itself
    num_occupied -= 1

    return num_occupied >= 4

def to_be_occupied(room, r, c):
    # If a seat is empty (L) and
    # there are no occupied seats adjacent to it, 
    # the seat becomes occupied.
    
    if room[r][c] != "L":
        return False

    num_occupied = count_occupied(room, r, c)


    return num_occupied == 0

room = []

with open(input_file, "r") as f:

    for line in f:
        line = line.strip()

        if not line:
            continue

        row = []
        for c in line:
            row.append(c)

        room.append(row)

    new_room = room 
    room = []
    iteration = 0
    while new_room != room:
        room = new_room
        iteration += 1
        print("Iteration: %d" % iteration)
        #print_room(room)

        new_room = []
        r = 0
        while r < len(room):
            row = room[r]
            new_row = row[:]

            c = 0
            while c < len(row):
                if to_be_empty(room, r, c):
                    new_row[c] = "L"
                elif to_be_occupied(room, r, c):
                    new_row[c] = "#"
                c += 1
            r += 1

            new_room.append(new_row)

        print("\n")

print("Stopped")
#print_room(new_room)

num_occupied = 0
for row in room:
    for c in row:
        if c == "#":
            num_occupied += 1

print("Num occupied: %d" % num_occupied)



        
