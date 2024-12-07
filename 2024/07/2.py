#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
        
def try_solve(result, numbers):
    
    ns = numbers[1:]
    ns.reverse()
    
    
    rs = [result]

    for n in ns :
        nrs = []
        
        for r in rs:
            if (r % n) == 0:
                nrs.append(r // n)
            nrs.append(r - n)
            
            if r > 0:
                strn = str(n)
                strr = str(r)
                if len(strr) > len(strn) and strr[-len(strn):] == strn:
                    print("n=%s r=%s" % (strn, strr))
                    nrs.append(int(strr[:-len(strn)]))
        
        rs = nrs
            
    print("need %d have: %s" % (numbers[0], rs))
    
    for r in rs:
        if r == numbers[0]:
            return True
    
    return False

counter = 0
                
with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        result, numbers = line.split(":")
        result = int(result)
        
        numbers = [int(n) for n in numbers.strip().split(" ")]
        
        solved = try_solve(result, numbers)
        
        print("%d: %s == %d" % (solved, numbers, result))
        
        if solved:
            counter += result
            
print("result: ", counter)
