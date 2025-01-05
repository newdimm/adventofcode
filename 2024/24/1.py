#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]

def op_or(i1,i2):
    return i1 or i2

def op_and(i1,i2):
    return i1 and i2

def op_xor(i1,i2):
    return op_or(op_and(i1, not i2),op_and(not i1, i2))

ops = {
    "OR" : op_or,
    "AND" : op_and,
    "XOR" : op_xor 
}

inputs = {}
outputs = {}

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        if ":" in line:
            i,v = line.split(": ")
            inputs[i] = (int(v),[])
            
        if "->" in line:
            c,o = line.split(" -> ")
            i1,op,i2 = c.split(" ")
            outputs[o] = (ops[op], i1, i2)
            
            for i in (i1,i2):
                if i in inputs:
                    v,olist = inputs[i]
                else:
                    v,olist = (None, [])
                olist.append(o)
                inputs[i] = (v, olist)

num_changed = 1
iteration = 0
while num_changed > 0:
    
    num_changed = 0
    
    print("[%d]: scanning" % iteration)

    active = []
    
    for o in outputs.keys():
        op,i1,i2 = outputs[o]
        v1,l1 = inputs[i1]
        v2,l2 = inputs[i2]
        if (v1 is not None) and (v2 is not None):
            active.append(o)
            
    print("  %d outputs active" % len(active))
            
    for o in active:
        op,i1,i2 = outputs[o]
        v1,l1 = inputs[i1]
        v2,l2 = inputs[i2]
        vo = op(v1,v2)
        if o not in inputs:
            print("missing in inputs: %s" % (o))
            oldv = None
            olist = []
        else:
            oldv, olist = inputs[o]
        if oldv is None:
            num_changed += 1
        inputs[o] = (vo, olist)
    
    print("  %d inputs changed" % num_changed)
    iteration += 1


result = 0
for i in inputs.keys():
    if i[0] == "z":
        vi,ilist = inputs[i]
        print("%s=%d" % (i, vi))
        try:
            bitno = int(i[1:])
        except:
            bitno = None
        if bitno is None:
            print("skip %s" % i)
            continue
        if vi:    
            result |= (1 << bitno)
            
print("Result: %d" % result)