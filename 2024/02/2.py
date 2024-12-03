#!/bin/python3
import sys
from _operator import index

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

safe_reports = 0

def check(report):
    if report[1] > report[0]:
        growing = True
    else:
        growing = False
        
    prev = report[0]
    for r in report[1:]:
        delta = r - prev
        if abs(delta) not in [1,2,3]:
            return False
        
        if (delta > 0) != growing:
            return False
        prev = r
        
    return True

def check_report(report):
    if report[1] > report[0]:
        growing = True
    else:
        growing = False
        
    prev = report[0]
    for index in range(1,len(report)):
        r = report[index]
        delta = r - prev
        if abs(delta) not in [1,2,3]:
            return index
        
        if (delta > 0) != growing:
            return index
        prev = r
        
    return len(report)
    
        

with open(fname) as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        
        if not report:
            continue
        
        if len(report) == 1:
            safe_reports += 1
            continue
        
        if check(report):
            print("YES %s" % report)
            safe_reports += 1
        else:
            print("NO %s" % report)
            
            first = check_report(report)
            
            targets = [first, first - 1, first + 1, 0, len(report)-1]
                
            for t in targets:
                if t < 0 or t >= len(report):
                    continue
                new_report = report[:]
                del(new_report[t])
                if check(new_report):
                    print("YES2 %s (%d)" % (new_report, t))
                    safe_reports += 1
                    break
        
print(safe_reports)