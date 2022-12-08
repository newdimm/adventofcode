f = open("input.txt")

# read the configuration
raw_crates = []

for line in f:
    while line and not line.isprintable():
        line = line[:-1]
         
    if not line:
        break
    
    raw_crates.append(line)

header = raw_crates[-1]
raw_crates = raw_crates[:-1]

stacks = []

pos = 0
skip_digits = False

while pos < len(header):
    if header[pos].isdigit():
        if not skip_digits:
            # new stack
            stack = []
            for crate in raw_crates:
                if crate[pos].isalpha():
                    crate = crate[pos : ]
                    ends = crate.find("]")
                    crate = crate[:ends]
                    item = crate
                    stack.insert(0, item)
            stacks.append(stack)
            
            skip_digits = True
        else:
            # skip this digit
            pass
    else:
        # not a digit
        skip_digits = False
    pos += 1

    
def print_stacks(stacks):
    index = 0
    for s in stacks:
        print("(%02d): %s" % (index, s))
        index += 1
    print("")
        
print_stacks(stacks)

for move in f:
    move = move.strip()
    
    if not move:
        continue
    
    # move COUNT from STACK to STACK
    
    # discard "move"
    move = move[5:]
    count, stacks_from_to = move.split(" from ")
    
    count = int(count)
    stack_from, stack_to = stacks_from_to.split(" to ")
    stack_from = int(stack_from) - 1
    stack_to = int(stack_to) - 1
        
    print("%d: %d -> %d" % (count, stack_from, stack_to))
    
    if len(stacks[stack_from]) < count:
        print("No %d items in stack %d (%s)" % (count, stack_from, str(stacks[stack_from])))
        exit()
    items = stacks[stack_from][-count:]
    del stacks[stack_from][-count:]
    items.reverse()
    stacks[stack_to].extend(items)
    
    print_stacks(stacks)
    
result = ""
for s in stacks:
    if s:
        result += s[-1]
        
print(result) 
    
    
