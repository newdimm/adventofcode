f = open("input.txt")

forest = []
visible = []

for line in f:
    line = line.strip()
    row = []
    for c in line:
        row.append(int(c))
    #print(row)
    forest.append(row)
    visible.append([0] * len(row))
    
y_max = [-1] * len(forest[0])
for y in range(len(forest)):
    x_max = -1
    for x in range(len(forest[0])):
        current = forest[y][x]
        if current > x_max:
            visible[y][x] = 1
            x_max = current
        if current > y_max[x]:
            visible[y][x] = 1
            y_max[x] = current
        
print("")

y_max = [-1] * len(forest[0])
for y in range(len(forest)-1, -1, -1):
    x_max = -1
    for x in range(len(forest[0])-1, -1, -1):
        current = forest[y][x]
        if current > x_max:
            visible[y][x] = 1
            x_max = current
        if current > y_max[x]:
            visible[y][x] = 1
            y_max[x] = current

count = 0
for row in visible:
    #print(row)
    count += sum(row)
    
print(count)

