f = open("input.txt")

class monkey:
    def __init__(self, index, items, v1, op, v2, test, true, false):
        self._index = index
        self._items = items
        self._v1 = v1
        self._op = op
        self._v2 = v2
        self._test = test
        self._true = true
        self._false = false
        
        self._score = 0
        
    @property
    def empty(self):
        return len(self._items) == 0
        
    def pop(self):
        if not self._items:
            return None
        
        level = self._items[0]
        del self._items[0]
        
        v1 = level
        if self._v1 != "old":
            v1 = int(self._v1)
            
        v2 = level
        if self._v2 != "old":
            v2 = int(self._v2)
            
        if self._op == "+":
            level = v1 + v2
        elif self._op == "-":
            level = v1 - v2
        elif self._op == "*":
            level = v1 * v2
        elif self._op == "/":
            level = v1 / v2
            
        level = level // 3
        
        if (level % self._test) == 0:
            new_monkey = self._true
        else:
            new_monkey = self._false
            
        self._score += 1
            
        return (level, new_monkey)
        
    
    def push(self, level):
        self._items.append(level)
        
    @property
    def score(self):
        return self._score
        
    def __repr__(self):
        return "[%d]: score %d items %s" % (self._index, self._score, str(self._items))
                
monkeys = []

m = None
index = None
items = None
v1 = None
op = None
v2 = None
test = None
true = None
false = None

for line in f:
    line = line.strip()
    print(line)
    
    if not line:
        print("m[%d] items=%s new = %s %s %s,  (div by %d) ?  %d : %d" % (index, items, v1, op, v2, test, true, false))
        m = monkey(index, items, v1, op, v2, test, true, false)
        monkeys.append(m)
        index = None
        continue
    
    if line.startswith("Monkey "):
        ignore, index = line.split()
        index = index[:-1]
        index = int(index)
        
        continue
    
    if line.startswith("Starting items: "):
        items = [int(x) for x in line[16:].split(", ")]
        continue
    
    if line.startswith("Operation: new = "):
        v1, op, v2 =  line[17:].split()
        continue
    
    
    if line.startswith("Test: divisible by "):
        test = int(line[19:])
        continue
    
    if line.startswith("If true: throw to monkey "):
        true = int(line[25:])
        continue
    
    if line.startswith("If false: throw to monkey "):
        false = int(line[26:])
        continue

if index is not None:
        print("m[%d] items=%s new = %s %s %s,  (div by %d) ?  %d : %d" % (index, items, v1, op, v2, test, true, false))
        m = monkey(index, items, v1, op, v2, test, true, false)
        monkeys.append(m)

for r in range(20):
    for i in range(len(monkeys)):
        m = monkeys[i]
        
        while not m.empty:
            level, new_monkey = m.pop()
            
            monkeys[new_monkey].push(level)
    
    print("Round: %d" % r)
    scores = []
    for i in range(len(monkeys)):
        print(monkeys[i])
        scores.append(monkeys[i].score)
        
    scores = sorted(scores)
    print("Result %d" % (scores[-1] * scores[-2]))
         