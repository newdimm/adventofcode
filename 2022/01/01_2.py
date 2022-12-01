f = open("input.txt")

msum = [0, 0, 0]
csum = 0

for line in f:
    line = line.strip()
    if not line:
        if csum > msum[0]:
            del msum[0]
            msum.append(csum)
            msum = sorted(msum)
        csum = 0
        continue
        
    csum += int(line)


print(sum(msum))