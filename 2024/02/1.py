#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

safe_reports = 0

with open(fname) as f:
    for line in f:
        report = [int(x) for x in line.strip().split(" ")]
        
        if not report:
            continue
        
        if len(report) == 1:
            safe_reports += 1
            continue
        
        report_is_safe = True
        
        prev = report[0]
        delta = report[1] - report[0]
        if delta != 0:
            sign = delta // abs(delta)
        else:
            sign = 1
            
        for r in report[1:]:
            delta = r - prev
            if delta * sign not in [1,2,3] or delta // abs(delta) != sign:
                report_is_safe = False
                break
            
            prev = r
            
        if report_is_safe:
            safe_reports += 1

        
        
print(safe_reports)