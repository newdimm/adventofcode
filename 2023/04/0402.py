#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

total_sum = 0

stack = []

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line.startswith("Card "):
            continue

        print(line)

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

        num = 0
        for c in check:
            if c in win:
                num += 1

        ctr = 1 + len(stack)

        #print("card[%d] win %d total += %d stack len %d (%s)" % (card_no, num, ctr, len(stack), stack))

        total_sum += ctr


        new_stack = []
        for s in stack:
            if s == 1:
                #print("del 1")
                continue
            new_stack.append(s-1)
        stack = new_stack

        if num:
            for i in range(ctr):
                #print("add", num)
                stack.append(num)


print("result", total_sum)




                    







        

