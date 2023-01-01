f = open("input.txt")

class Item:
    def __init__(self, level):
        self._level = level
        self._rems = {}
        
    def set_dividers(self, divs):
        for div in divs:
            self._rems[div] = self._level % div
        
    def divides(self, div):
        return self._rems[div] == 0
    
    def square(self):
        for div in self._rems.keys():
            self._rems[div] = (self._rems[div] * self._rems[div]) % div
        #self._level = self._level * self._level
    
    def mult(self, value):
        for div in self._rems.keys():
            self._rems[div] = (self._rems[div] * value) % div
        #self._level *= value
    
    def add(self, value):
        for div in self._rems.keys():
            self._rems[div] = (self._rems[div] + value) % div
        #self._level += value
        
    def __repr__(self):
        return str(self._rems)

class BaseMonkey:
    def __init__(self, index, items, value, div, true, false):
        self._index = index
        
        self._items = [Item(i) for i in items]
        self._value = value
        self._div = div
        self._true = true
        self._false = false
        
        self._score = 0
        
    def set_dividers(self, divs):
        for item in self._items:
            item.set_dividers(divs)
            
    @property
    def empty(self):
        return len(self._items) == 0
        
    def pop(self):
        if self.empty:
            return None
        
        item = self._items.pop(0)
        
        self.do_op(item)
            
        if self.do_test(item):
            new_monkey = self._true
        else:
            new_monkey = self._false
            
        self._score += 1
            
        return (item, new_monkey)
        
    def do_test(self, item):
        return item.divides(self._div)
        
    def push(self, item):
        self._items.append(item)
        
    @property
    def score(self):
        return self._score
        
    def __repr__(self):
        return "[%d]: ?? score %d items %s" % (self._index, self._score, self._items)
    
class SquareMonkey(BaseMonkey):
    def __init__(self, index, items, value, div, true, false):
        super(SquareMonkey, self).__init__(index, items, value, div, true, false)
        
    def do_op(self, item):
        item.square()

    def __repr__(self):
        return "[%d] ^^ score %d items %s" % (self._index, self._score, self._items)

class MultMonkey(BaseMonkey):
    def __init__(self, index, items, value, div, true, false):
        super(MultMonkey, self).__init__(index, items, value, div, true, false)
        
    def do_op(self, item):
        item.mult(self._value)
        
    def __repr__(self):
        return "[%d] ** score %d items %s" % (self._index, self._score, self._items)


class AddMonkey(BaseMonkey):
    def __init__(self, index, items, value, div, true, false):
        super(AddMonkey, self).__init__(index, items, value, div, true, false)
        
    def do_op(self, item):
        item.add(self._value)

    def __repr__(self):
        return "[%d] ++ score %d items %s" % (self._index, self._score, self._items)
                
                
monkeys = []

m = None
index = None
items = None
op = None
value = None
div = None
true = None
false = None

dividers = []

for line in f:
    line = line.strip()
    print(line)
    
    if not line:
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
        if op == "*" and v1 == "old" and v2 == "old":
            op = "^"
            value = 0
        else:
            value = int(v2)
        continue
    
    if line.startswith("Test: divisible by "):
        div = int(line[19:])
        if div not in dividers:
            dividers.append(div)
        continue
    
    if line.startswith("If true: throw to monkey "):
        true = int(line[25:])
        continue
    
    if line.startswith("If false: throw to monkey "):
        false = int(line[26:])
    else:
        raise("Unexpected line %s" % line)
    
    if op == "^":
        m = SquareMonkey(index, items, 0, div, true, false)
    elif op == "*":
        m = MultMonkey(index, items, value, div, true, false)
    elif op == "+":
        m = AddMonkey(index, items, value, div, true, false)
    print(m)
    monkeys.append(m)

for i in range(len(monkeys)):
    m = monkeys[i]
    
    m.set_dividers(dividers)

for r in range(10000):
    for i in range(len(monkeys)):
        m = monkeys[i]
        
        while not m.empty:
            level, new_monkey = m.pop()
            
            monkeys[new_monkey].push(level)
    
    print("Round: %d" % r)
    scores = []
    for i in range(len(monkeys)):
        #print(monkeys[i])
        scores.append(monkeys[i].score)
        
    scores = sorted(scores)
    print("Result %d" % (scores[-1] * scores[-2]))
