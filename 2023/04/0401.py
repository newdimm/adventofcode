#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

total_sum = 0

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line.startswith("Card "):
            continue

        line = line[5:]
        card_no, numbs = line.split(":")
        card_no = int(card_no.strip())
        numbs = numbs.strip()
        win, check = numbs.split("|")
        win = win.strip()
        check = check.strip()

        new_win = ""
        for x in win:
            if x == ' ' and new_win and new_win[-1] == ' ':
                continue
            new_win += x
        win = new_win

        new_check = ""
        for x in check:
            if x == ' ' and new_check and new_check[-1] == ' ':
                continue
            new_check += x
        check = new_check

        win = [int(x) for x in win.split(" ")]
        check = [int(x) for x in check.split(" ")]

        score = 0
        for c in check:
            if c in win:
                if score:
                    score = score << 1
                else:
                    score = 1

        total_sum += score

print("result", total_sum)




                    







        

