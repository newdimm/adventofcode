f = open("input.txt")
for line in f:
    length = len(line)
    # mjqjpqmgbljsphdztnvjfqwrcgsmlb
    d = [0] * 256
    counter = 0
    
    #print(line)
    
    pos = 0
    while pos <= 13:
        code = ord(line[pos])
        
        if d[code] == 1:
            counter += 1
        d[code] += 1

        pos += 1

    if counter == 0:
        print(pos+1)
        exit()

    while pos < length:
        code = ord(line[pos])
        
        if d[code] == 1:
            counter += 1
        d[code] += 1
        
        code = ord(line[pos-14])
        d[code] -= 1
        if d[code] == 1:
            counter -= 1
            
        if counter == 0:
            print(pos+1)
            exit()

        pos += 1
