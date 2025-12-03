#!/bin/python3
import sys
import math
 
fname = "test.txt"
debug = False
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if len(sys.argv) > 2 and sys.argv[2] == "debug":
            debug = True

def gen_and_add_len(start, stop, repeat):
    chunk = len(start) // repeat
    s = [start[i*chunk:(i+1)*chunk] for i in range(repeat)]
    s1 = int(s[0])
    if int(s[0]*repeat) < int("".join(s)):
        s1 += 1

    e = [stop[i*chunk:(i+1)*chunk] for i in range(repeat)]
    e1 = int(e[0])
    if int(e[0] * repeat) > int("".join(e)):
        e1 -= 1

    if debug:
        print("    %s-%s s=(%d,%s) e=(%d,%s)" % (start, stop, s1, s, e1, e))
    
    if e1 < s1:
        return None

    count = e1 - s1 + 1
    results = []
    for num in range(s1, e1+1):
        mult = pow(10, int(math.log10(num)) + 1)
        r = num
        for i in range(repeat-1):
              r *= mult
              r += num
        results.append(r)
    
    if debug:
        print("    %d numbers (%d: %s)" % (count, len(results), results[:100]))

    return results

def gen_and_add(start, stop, repeat):
    if debug:
        print("  %s-%s [%d]" % (start, stop, repeat))

    if len(start) % repeat:
        zeros = (len(start) // repeat + 1) * repeat - 1
        start = "1" + "0"*zeros

    if len(stop) % repeat:
        nines = len(stop) // repeat * repeat
        stop = "9"*nines

    if int(stop) < int(start):
        return None

    results = []

    for length in range(len(start), len(stop)+1):
        if (length % repeat) == 0:
            if length != len(start):
                sub_start = "1" + "0"*(length-1)
            else:
                sub_start = start

            if length != len(stop):
                sub_stop = "9"*length
            else:
                sub_stop = stop

            sub_res = gen_and_add_len(sub_start, sub_stop, repeat)

            if sub_res is not None:
                for s in sub_res:
                    if not s in results:
                        results.append(s)

    return results

total = 0

with open(fname, "rt") as f:
    for line in f:
        line = line.strip()
        ranges = line.split(",")
        for r in ranges:
            [start, stop] = [x.strip() for x in r.split("-")]

            results = []
            for repeat in range(2, len(stop)+1):
                result = gen_and_add(start, stop, repeat)
                if result is not None:
                    for one_res in result:
                        if one_res not in results:
                            results.append(one_res)

            if debug:
                print("%s-%s: total %d" % (start, stop, sum(results)))
                print("")

            total += sum(results)

print(total)
