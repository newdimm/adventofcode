f = open("input.txt")

a_code = ord('a')
A_code = ord('A')

total = 0

pos = 0
for line in f:
    line = line.strip()
    
    if pos == 0:
        seen = [[],[],[]]
        seen[0] = [0] * 26 * 2
        seen[1] = [0] * 26 * 2
        seen[2] = [0] * 26 * 2
        
    print(line)
    
    for c in line:
        if c >= 'a' and c <= 'z':
            index = ord(c) - a_code
        else:
            index = ord(c) - A_code + 26
            
        seen[pos][index] += 1
        
    if pos == 2:
        for index in range(26*2):
            if seen[0][index] and seen[1][index] and seen[2][index]:
                prio = seen[0][index] + seen[1][index] + seen[2][index]
                if index < 26:
                    c = chr(ord('a') + index)
                else:
                    c = chr(ord('A') + index - 26)
                    
                print("%d : %s : %d" % (index, c, prio))
                total += index + 1
        pos = 0
    else:
        pos += 1
        
     

print(total)
