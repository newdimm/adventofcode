f = open("input.txt")

counter = 0

for line in f:
    pair = line.strip().split(",")
    range1 = [int(x) for x in pair[0].split("-")]
    range2 = [int(x) for x in pair[1].split("-")]
    
    #print("%s :: %s" % (range1, range2))
    if range1[0] <= range2[0] and range1[1] >= range2[0] \
        or range2[0] <= range1[0] and range2[1] >= range1[0]:
        counter += 1
        
print(counter)