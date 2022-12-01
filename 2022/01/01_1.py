f = open("input.txt")

msum = 0
csum = 0

for line in f:
    line = line.strip()
    if not line:
        if csum > msum:
            msum = csum
        csum = 0
        continue
        
    csum += int(line)


print(msum)