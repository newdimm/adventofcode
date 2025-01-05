#!/bin/python3
import sys, time, heapq, random

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
gates = {}

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        if ":" in line:
            i,v = line.split(": ")
            inputs[i] = int(v)
            
        if "->" in line:
            c,o = line.split(" -> ")
            i1,op,i2 = c.split(" ")
            gates[o] = (ops[op], i1, i2)
            

def runit(x, y, gates, maxbits):
    inputs = {}
    
    for bitno in range(maxbits+1):
        value = 1 << bitno
        if x & value:
            inputs["x%02d" % bitno] = 1
        else:
            inputs["x%02d" % bitno] = 0
        if y & value:
            inputs["y%02d" % bitno] = 1
        else:
            inputs["y%02d" % bitno] = 0
    
    iteration = 0
    
    program = []
    for g in gates.keys():
        op,i1,i2 = gates[g]
        program.append((g,op,i1,i2))
    
    while program:
        
        new_program = []
        for o,op,i1,i2 in program:
            if i1 not in inputs or i2 not in inputs:
                new_program.append((o,op,i1,i2))
                continue
            
            v1 = inputs[i1]
            v2 = inputs[i2]
            
            vo = op(v1,v2)
            
            inputs[o] = vo
        if program == new_program:
            break
        program = new_program
        
        iteration += 1
    #print("ran in %d iterations" % iteration)
    
    z = 0 
    for bitno in range(maxbits+1):
        bitname = "z%02d" % bitno
        if bitname not in inputs:
            return None
        
        z |= inputs[bitname] << bitno
        
    return z


def get_var_value(name, inputs):
    value = 0
    for i in inputs.keys():
        if i.startswith(name):
            inumber = i[len(name):]
            try:
                bitno = int(inumber)
            except:
                continue
            value |= inputs[i] << bitno
    return value

def get_max_bitno(name, gates):
    max_bitno = 0
    
    for i in gates.keys():
        if i.startswith(name):
            inumber = i[len(name):]
            try:
                bitno = int(inumber)
            except:
                continue
            max_bitno = max(max_bitno, bitno)
    return max_bitno

maxbits = get_max_bitno("z", gates)

x = get_var_value("x", inputs)
y = get_var_value("y", inputs)

z = runit(x, y, gates, maxbits)

print("x=0x%x + y=0x%x = z=0x%x" % (x,y,z))

def count_errors(gates, maxbits):
    errors = 0
    corrects = 0

    result = { 0: "BAD!", 1: "good"}
    
    for bitno in range(maxbits):
        for (nx,ny) in [(0,0),(0,1),(1,0),(1,1)]:
            #x = get_var_value("x", inputs)
            #y = get_var_value("y", inputs)
            #x &= ~(1 << bitno)
            #y &= ~(1 << bitno)
            
            x = y = 0
            
            x |= nx << bitno
            y |= ny << bitno
            
            z = runit(x, y, gates, maxbits)
            
            if z is None:
                return 1000
            
            expected_z = x + y
            
            #print("[%02d] %s 0x%x + 0x%x = 0x%x ? 0x%x" % (bitno, result[z == expected_z], x,y,z,expected_z))
            
            if z != expected_z:
                errors += 1
                
    x=0x11681da8e239
    y=0x1af78a4c5eaf
    z = runit(x, y, gates, maxbits)
    expected_z = x+y
    if z != expected_z:
        errors += 1
        
    x = int(random.random() * (1 << (maxbits+1)))
    y = int(random.random() * (1 << (maxbits+1)))
    z = runit(x, y, gates, maxbits)
    
    if z != x+y:
        errors += 1
    
    return errors

def get_error_gates(gates, maxbits):
    error_gates = []
    
    for bitno in range(maxbits):
        for (nx,ny) in [(0,0),(0,1),(1,0),(1,1)]:
            x = y = 0
            
            x |= nx << bitno
            y |= ny << bitno
            
            z = runit(x, y, gates, maxbits)
            
            expected_z = x + y
            
            if z != expected_z:
                stack = ["x%02d" % bitno, "y%02d" % bitno]
                
                while stack:
                    g = stack.pop()
                        
                    for o in gates.keys():
                        op,i1,i2 = gates[o]
                        if g == i1 or g == i2 and o not in stack and o not in error_gates:
                            error_gates.append(o)
                            stack.append(o)

    for bitno in range(maxbits):
        all_good = True
        for (nx,ny) in [(0,0),(0,1),(1,0),(1,1)]:
            x = y = 0
            
            x |= nx << bitno
            y |= ny << bitno
            
            z = runit(x, y, gates, maxbits)
            
            expected_z = x + y
            
            if z != expected_z:
                all_good = False
            
        if all_good:
            stack = ["x%02d" % bitno, "y%02d" % bitno]
                
            while stack:
                g = stack.pop()
                    
                for o in gates.keys():
                    op,i1,i2 = gates[o]
                    if g == i1 or g == i2 and o not in stack:
                        if o in error_gates:
                            error_gates.remove(o)
                        stack.append(o)
    return error_gates
            
def do_test(x,y,gates):
    for dx,dy in [(0,1),(1,0),(1,1)]:
        nx = dx*x
        ny = dy*y
        
        z = runit(nx, ny, gates, maxbits)
        
        if z != nx+ny:
            return False
    return True

def swap_gates(o1,o2,gates):
    g1 = gates[o1]
    g2 = gates[o2]
    
    gates[o2] = g1
    print("%s -> %s" % (g1,o2))
    gates[o1] = g2
    print("%s -> %s" % (g2,o1))
    
def list_output_gates(o, gates):
    result = [o]
    stack = []
    stack.append(o)
    while stack:
        g = stack.pop()
        op,i1,i2 = gates[g]
        for i in [i1, i2]:
            if i in gates: 
                result.append(i)
                stack.append(i)
        
    return result


def find_gate(i1, i2, op):
    global gates
    for g in gates:
        if gates[g] == (op, i1, i2) or gates[g] == (op, i2, i1):
            return g
    return None

def find_part(i1, op):
    global gates
    for g in gates:
        nop, ni1, ni2 = gates[g]
        if op == nop and i1 in (ni1, ni2):
            return g
    return None

cin = None
result = []

def rappend(g):
    global result
    if g not in result:
        print("++%s", g)
        result.append(g)

bitno = 0        
while bitno < maxbits:
    x = "x%02d" % bitno
    y = "y%02d" % bitno
    z = "z%02d" % bitno
    next_z = "z%02d" % (bitno+1)
    
    xor1 = find_gate(x,y,op_xor)
    if not xor1:
        print("[%02d] can't find XOR1 for %s and %s" % (bitno, x, y))
        print("terminate")
        break

    and1 = find_gate(x,y,op_and)
    if not and1:
        print("[%02d] can't find AND1 for %s and %s" % (bitno, x, y))
        print("terminate")
        break
    
    print("[%02d] CIN=%s XOR1=%s AND1=%s" % (bitno, cin, xor1, and1))

    if cin:
        xor2 = find_gate(xor1, cin, op_xor)
        if xor2:
            if xor2 != z:
                print("[%02d] XOR2 for XOR1=%s, CIN=%s not connected to Z" % (bitno, xor1, cin))
                swap_gates(xor2, z, gates)
                rappend(xor2)
                rappend(z)
                continue
        else: ## no XOR2
            print("[%02d] no XOR2 for XOR1=%s, CIN=%s" % (bitno, xor1, cin))
            part_xor2_cin = find_part(cin, op_xor)
            if part_xor2_cin == z:
                op,i1,i2 = gates[z]
                rappend(xor1)
                if cin == i1:
                    
                    swap_gates(i2, xor1, gates)
                    rappend(i2)
                    xor1 = i2
                else:
                    swap_gates(i1, xor1, gates)
                    rappend(i1)
                    xor1 = i1
                continue
            else:
                part_xor2_xor1 = find_part(xor1, op_xor)
                if part_xor2_xor1 == z:
                    op,i1,i2 = gates[z]
                    rappend(cin)
                    if xor1 == i1:
                        swap_gates(cin, i2, gates)
                        rappend(i2)
                        cin = i2
                    else:
                        swap_gates(cin, i1, gates)
                        rappend(i1)
                        cin = i1
                    continue
                else:
                    print("[%02d] stuck XOR1=%s CIN=%s Z=%s" % (bitno, xor1, cin, gates[z]))
                    print("terminate")
                    break
        
        and2 = find_gate(xor1, cin, op_and)
        print("[%02d] AND2(%s,%s)=%s" % (bitno, xor1, cin, and2))
        if not and2:
            print("[%02d] can't find AND2 XOR1=%s CIN=%s" % (bitno, xor1, cin))
            print("terminate")
            break
                
        or1 = find_gate(and2, and1, op_or)
        print("[%02d] OR1(%s,%s)=%s" % (bitno, and2, and1, or1))

        if not or1:
            print("[%02d] no OR1 for AND1=%s, AND2%s" % (bitno, and1, and2))
            part_o1_and2 = find_part(and2, op_or)
            if part_o1_and2 and find_part(part_o1_and2, op_xor) == next_z:
                op,i1,i2 = gates[part_o1_and2]
                rappend(and1)
                if and2 == i1:
                    swap_gates(and1, i2, gates)
                    rappend(i2)
                    and1 = i2
                else:
                    swap_gates(and1, i1, gates)
                    rappend(i1)
                    and1 = i1
                continue
            else:
                part_o1_and1 = find_part(and1, op_or)
                if part_o1_and1 and find_part(part_o1_and1, op_xor) == next_z:
                    op,i1,i2 = gates[part_o1_and1]
                    rappend(and2)
                    if and1 == i1:
                        swap_gates(and2, i2, gates)
                        rappend(i2)
                        and2 = i2
                    else:
                        swap_gates(and2, i1, gates)
                        rappend(i1)
                        and2 = i1
                    continue
                else:
                    print("[%02d] stuck XOR1=%s XOR2=%s" % (bitno, xor1, xor2))
                    print("terminate")
                    break
            or1 = find_gate(xor1, xor2, op_or)
            if not or1:
                print("[%02d] can't finally find XOR1=%s XOR2=%s" % (bitno, xor1, xor2))
                print("terminate")
                break
        cin = or1
            
    else: # not CIN
        if xor1 != z:
            result.append(xor1)
            print("[%02d] first XOR1 not connected to Z for for %s and %s" % (bitno, x, y))
        cin = and1
    
    bitno += 1

result.sort()
print("Result: %s" % ",". join(result))

for i in range(20):
    x = int(random.random() * (1 << (maxbits)))
    print("x", x)
    y = int(random.random() * (1 << (maxbits)))
    print("y", y)
    z = runit(x, y, gates, maxbits)
    print("z", z)
        
    if z:
        print("x=0x%x + y=0x%x = z=0x%x (%d)" % (x,y,z, z == x+y))
    else:
        print("x=0x%x + y=0x%x = z=%s" % (x,y,z))
        

# cdk,cmd,ddn,hnj,kqh,pfk,rmn,vbr,z09,z21,z34 - not the right
# ddn,gqh,kqh,nnf,rmn,wrc,z09,z34 - not tje right
# ddn,kqh,nhs,nnf,rmn,wrc,z09,z34 - not
