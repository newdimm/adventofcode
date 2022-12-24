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
    
def score(x,y):
    c = forest[y][x]
    xp = 0
    for cx in range(x+1, len(forest[0])):
        xp += 1
        if forest[y][cx] >= c:
            break

    xm = 0
    for cx in range(x-1, -1, -1):
        xm += 1
        if forest[y][cx] >= c:
            break

    yp = 0
    for cy in range(y+1, len(forest)):
        yp += 1
        if forest[cy][x] >= c:
            break

    ym = 0
    for cy in range(y-1, -1, -1):
        ym += 1
        if forest[cy][x] >= c:
            break
    return xp*xm*yp*ym

max_score = 0
for y in range(len(forest)):
    for x in range(len(forest[0])):
        max_score = max(max_score, score(x,y))
        
        

    
print(max_score)

