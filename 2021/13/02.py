#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

dots = []
folds = []

max_x = 0
max_y = 0
for line in f_input:
    line = line.strip()

    if not line:
        continue

    if line.startswith("fold along y="):
        test, fold = line.split("=")
        fold = int(fold)
        folds.append(("y", fold))
    elif line.startswith("fold along x="):
        test, fold = line.split("=")
        fold = int(fold)
        folds.append(("x", fold))
    else:
        x,y = line.split(",")
        x = int(x)
        y = int(y)
        dots.append((x, y))

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

max_x += 1
max_y += 1
print(dots)
print("max x=%d y=%d" % (max_x, max_y))
print("folds %s" % (folds))
canvas = []
for y in range(max_y):
    canvas.append([" "] * (max_x+1))
    
for x,y in dots:
    print("dot x=%d, y=%d" % (x,y))
    canvas[y][x] = "#"
    

def print_canvas(c):
    pos = 0
    line = ""
    for x in range(len(c[0])):
        line += "%d" % (pos % 10)
        pos += 1
    print("--- %s" % line)

    pos = 0
    print()
    for y in range(len(c)):
        line = ""
        for x in range(len(c[y])):
            line += c[y][x]
        print("%02d: %s" % (pos, line))
        pos += 1
    

#print_canvas(canvas)

# do fold y
for axis, f in folds:
    print("Folding along %s=%d" % (axis, f))
    new_dots = []

    for x,y in dots:
        if axis == "y":
            if y >= f:  
                y = f - (y - f)
                canvas[y][x] = "#"
        else:
            if x >= f:  
                x = f - (x - f)
                canvas[y][x] = "#"
        if (x,y) not in new_dots:
            new_dots.append((x,y))

    dots = new_dots

    if axis == "y":
        canvas = canvas[0:f]
    else:
        for y in range(len(canvas)):
            canvas[y] = canvas[y][0:f]
    #break

print("===========")
print_canvas(canvas)

counter = 0
for y in range(len(canvas)):
    for x in range(len(canvas[y])):
        if canvas[y][x] == "#":
            counter += 1

print("total dots: %d (check %d)" % (counter, len(dots)))