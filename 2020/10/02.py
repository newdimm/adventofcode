#!/usr/bin/python

test = 3

if test == 0:
    input_file = "simple_input.txt"
elif test == 1:
    input_file = "simple_input2.txt"
elif test == 2:
    input_file = "simple_input3.txt"
else:
    input_file = "input.txt"

data = []

with open(input_file, "r") as f:

    for line in f:
        line = line.strip()

        if not line:
            continue

        num = int(line)

        data.append(num)
        

data = [0] + sorted(data)

print(data)

def get_sets(r1, r2):
    
    if r1[0] > r2[0]:
        r = r2
        r2 = r1
        r1 = r
    # r1 < r2
    if r1[0] == r2[0]:
        return []

    common = []
    for r in r1:
        if r in r2:
            common.append(r)
    if not common:
        return []
    
    if len(r1)+len(r2) - 2 * len(common) <= 2:
        return []
    
    if len(r1) == 3:
        a = r1[1]
        if len(r2) == 3:
            # x a x
            #     x b x
            b = r2[1]
            return [ (a, b) ]
        
        ## len(r2) == 4
        c = r2[1]
        d = r2[2]
        
        if r1[2] == r2[0]:
            # x a x
            #     x c d x
            return [ (a, c), (a , d), (a, c, d) ] 
        # x a x
        #   x c d x
        return  [ (a, d) ] 
    
    ## len == 4
    a = r1[1]
    b = r1[2]
    
    if len(r2) == 3:
        c = r2[1]
        if r1[3] == r2[0]:
            # x a b x
            #       x c x
            return [ (a, c), (b, c), (a, b, c) ]
        else:
            # x a b x
            #     x c x
            return [ (a, c) ]
    
    ## both len == 4
    c = r2[1]
    d = r2[2]
    if r1[3] == r2[0]:
        # x a b x
        #       x c d x
        return [
            (a, c), (a, d), (b, c), (b, d),
            (a, b, c), (a, b, d), (a, c, d), (b, c, d),
            (a, b, c, d)
        ]
    # x a b x
    # x   x c d x
    return [
        (a, c), (a, d), (b, d),
        (a, b, d), (a, c, d)
    ]
    


def test():
    del r1[0]
    del r1[-1]
    del r2[0]
    del r2[-1]

    counter = 0

    common = []
    for r in r1:
        if r in r2:
            common.append(r)
                
    for r in common:
        del r1[r1.index(r)]
        del r2[r2.index(r)]
        
    result = []
    r = r1 + r2
    for i in r1:
        for j in r2:
            result.append( (i,j) )
    
    if len(r1) + len(r2) >= 3:
        if len(r1) > 1:
            result.append( (r1[0],r1[1],r2[0]) )
            if len(r2) > 1:
                result.append( (r1[0], r1[1], r2[1]) )
        if len(r2) > 1:
            result.append( (r1[0], r2[0], r2[1]) )
            if len(r1) > 1:
                result.append( (r1[1], r2[0], r2[1]) )
    if len(r1) + len(r2) == 4:
        result.append( (r1[0], r1[1], r2[0], r2[1]) )                   
            
    return result
        

def parse_group(group, left, right):    
    counter = 1
    
    if len(group) <= 2:
        return counter
    
    if left:
        group = [group[0] - 2] + group
    if right:
        group.append(group[-1] + 2)
    
    print("Group: %s" % (group))
    
    runs = []
    pos = 0
    # 0 1 2 3 4
    while pos < len(group) - 2:
        r = group[pos:pos+3]
        if r[-1] - r[0] <= 3:
            runs.append(r)
        r = group[pos:pos+4]
        if pos + 3 < len(group) and r[-1] - r[0] <= 3:
            runs.append(r)
        pos += 1
        
    print("found %d runs: %s" % (len(runs), str(runs)))
    
    i = 0
    sets = []
    while i < len(runs):
        j = i+1
        r1 = runs[i]
        while j < len(runs):
            r2  = runs[j]
            new_sets = get_sets(r1[:],r2[:])
            print("r[%d]=%s <> r[%d]=%s ==> %s" % (i, r1, j, r2, new_sets))
            for s in new_sets:
                if s not in sets:
                    print(">> %s and %s == %s" % (r1, r2, s))
                    sets.append(s)
            j += 1
        i += 1

    result = 1 + len(runs) + len(sets)
    print("group %s == %d" % (group, result))
    return result

j_prev = 0
pos = 1
group = False

result = 1


while pos < len(data):
    j = data[pos]
    diff = j - j_prev
    
    if diff == 1:
        if not group:
            group = True
            start = pos - 1
    elif group:
        left = False
        right = False
        if start != 0 and data[start] - data[start - 1] == 2:
            left = True
        if pos + 1 != len(data) and data[pos + 1] - data[pos] == 2:
            right = True
            
        result *= parse_group(data[start:pos], left, right)
        
        group = False
    pos += 1
    j_prev = j
    
if group:
    left = False
    right = False
    if start != 0 and data[start] - data[start - 1] == 2:
        left = True
            
    result *= parse_group(data[start:], left, right)
    
  
print("reulst: %d" % result)
