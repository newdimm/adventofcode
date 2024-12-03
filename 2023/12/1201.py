#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg.startswith("test"):
            fname = "input_%s" % arg

space = []

def matches(pattern, pos, g, last):
    if len(pattern) < pos + g:
        return False

    for shift in range(g):
        if pattern[pos+shift] not in ["#", "?"]:
            return False
    
    return last or len(pattern) > pos + shift + 1 and pattern[pos+shift+1] in ["?", "."]

def no_further(pattern, pos):
    for i in range(pos, len(pattern)):
        if pattern[i] == "#":
            return False
    return True

def do_matches(pattern, pi, groups, gi):
    counter = 0

    g = groups[gi]
    is_last = len(groups) - 1 == gi

    print(" " * gi + "[%d]=%d pos %d last %d" % (gi, g, pi, is_last))

    for pos in range(pi, len(pattern)-g+1):
        #print(" " * gi + "? pos %d" % pos)
        if matches(pattern, pos, g, is_last):
            if is_last:
                if no_further(pattern, pos+g):
                    print(" " * gi + "matches %d" % pos)
                    counter += 1
            else:
                print(" " * gi + "matches %d" % pos)
                counter += do_matches(pattern, pos + g + 1, groups, gi+1)

        if pattern[pos] == "#":
            break

    return counter

total_counter = 0

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        pattern, groups = line.split(" ")

        groups = [ int(x) for x in groups.split(",")]

        print(pattern, groups)

        counter = 0

        '''
        0 1 2 3 4 5 6 7 8 9 1011  len 12
        ? # # # ? ? ? ? ? ? ? ?  3,2,1
        0       4     7
        '''

        counter = do_matches(pattern, 0, groups, 0)

        print(counter)

        total_counter += counter

print ("total: %d" % total_counter)












