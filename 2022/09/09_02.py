f = open("input.txt")


class Pos:
    def __init__(self, x = 0, y = 0, caption = "X"):
        self._x = x;
        self._y = y
        self._visited = {}
        self.stamp()
        self._caption = caption

    def __repr__(self):
        max_x = max_y = min_x = min_y = 0
        for (x,y) in self._visited.keys():
            min_x = min(x, min_x)
            min_y = min(y, min_y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            
        output = "==== %s [%d,%d] visited %d====\n" % (self._caption, self.x, self.y, self.visited_count)
        for y in range(max_y, min_y -1, -1):
            row = ""
            for x in range(min_x, max_x + 1):
                if x == self._x and y == self._y:
                    row += self._caption
                elif x == 0 and y == 0:
                    row += "S"
                elif (x,y) in self._visited:
                    row += "#"
                else:
                    row += "~"
            output += row + "\n"
        return output


    def stamp(self):
        self._visited[(self._x, self._y)] = 1
        
    def up(self):
        self._y += 1
        self.stamp()
        
    def down(self):
        self._y -= 1
        self.stamp()
        
    def left(self):
        self._x -= 1
        self.stamp()
        
    def right(self):
        self._x += 1
        self.stamp()
            
    @property
    def visited_count(self):
        count = 0
        for (x,y) in self._visited.keys():
            count += 1
        return count
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
        
        
class H(Pos):
    def __init__(self, caption = "H"):
        super(H, self).__init__(caption = caption)

class T(Pos):
    def __init__(self, caption = "T", head = None):
        super(T, self).__init__(caption = caption)
        self._head = head
        
    def touching(self, h = None):
        if h is None:
            h = self._head
        return abs(self.y - h.y) <= 1 and abs(self.x - h.x) <= 1
    
    def follow(self, h = None):
        if h is None:
            h = self._head
        while not self.touching(h):
            delta_x = h.x - self.x
            delta_y = h.y - self.y
            if delta_x:
                delta_x  //= abs(delta_x)
            if delta_y:
                delta_y //= abs(delta_y)
            
            self._x += delta_x
            self._y += delta_y
            
            self.stamp()
        

h = H()
tails = []
prev = h
for index in range(1,10):
    t = T("%d" % index, prev)
    prev = t
    tails.append(t)

for line in f:
    line = line.strip()
    where, count = line.split()
    count = int(count)
    while count:
        if where == "L":
            h.left()
        elif where == "R":
            h.right()
        elif where == "U":
            h.up()
        elif where == "D":
            h.down()
        else:
            raise "Unknown direction <%s>" % where

        #print(h)
        for t in tails:
            t.follow()
        
        #print(t)

        count -= 1
    

print(h)
print(tails[8])
print(tails[8].visited_count)