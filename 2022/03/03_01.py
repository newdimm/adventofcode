f = open("input.txt")

a_code = ord('a')
A_code = ord('A')

total = 0

for line in f:
    line = line.strip()
    
    pivot = len(line) // 2
    
    seen = [False] * 26 * 2
    pos = 0
    for c in line:
        if c >= 'a' and c <= 'z':
            index = ord(c) - a_code
        else:
            index = ord(c) - A_code + 26
            
        if pos < pivot:
            seen[index] = True
        else:
            if seen[index]:
                break
        pos += 1
        
    print("%s: %s priority %d" % (line, c, index + 1))
    total += 1 + index
     

print(total)
