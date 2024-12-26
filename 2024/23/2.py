#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
edges = {}

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        f,t = line.split("-")
        
        try:
            flist = edges[f]
        except KeyError:
            flist = []
        flist.append(t)
        edges[f] = flist
            
        try:
            tlist = edges[t]
        except KeyError:
            tlist = []
        tlist.append(f)
        edges[t] = tlist

def test(edges, group):
    #print("   ? %s" % group)
    
    for t in group:
        flist = edges[t]
        for tt in group:
            if t == tt:
                continue
            if tt not in flist:
                return False

    return True

def find_groups(cache, edges, group, flist, results, depth):
    #print("   [%d]%s - %s" % (depth, group, flist))
    flist_minus = flist[:]
    for f in flist:
        group.append(f)
        flist_minus.remove(f)

        group.sort()
        key = ""
        for g in group:
            key += g
            
        if depth == 0:
            #print("   [%d]%s - %s" % (depth, group, flist))
            if key not in cache:
                cache[key] = test(edges, group)
                if cache[key]:
                    if key not in result:
                        #print("      +%s" % res)
                        result[key] = True
        else:
            if key not in cache:
                cache[key] = test(edges, group)
            
            if cache[key]:
                find_groups(cache, edges, group, flist_minus, results, depth-1)

        group.remove(f)
        flist_minus.append(f)
    
def find_len_groups(edges, group, result, group_len):
    if group_len == len(group):
        if test(edges, group):
            gsorted = sorted(group)
            key = ",".join(gsorted) 
            if key not in result:
                result[key] = True
    else:
        group_copy = group[:]
        for g in group[1:]:
            group_copy.remove(g)
            find_len_groups(edges, group_copy, result, group_len)
            group_copy.append(g)

maxdepth = 13

depth = 15
while True:
    print("Depth[%d]" % depth)
    
    result = {}
        
    for f in edges.keys():
        flist = edges[f]
        if len(flist) + 1 < depth:
            continue
            
        print("  %s: %s (len %d)" % (f, flist, len(flist)))

        group = [f]
        for ff in flist:
            group.append(ff)
        
        find_len_groups(edges, group, result, depth)
                
    
    if result:
        break

    depth -= 1


print("final: %s" % result)
print("final: %s" % (",".join(result.keys())))

# ao,fx,gk,im,kh,nh,oi,or,qt,rm,th,ww - not that