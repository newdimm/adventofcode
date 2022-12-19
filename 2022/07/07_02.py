f = open("input.txt")

class dentry:
    def __init__(self, parent, name, size = None):
        self._parent = parent
        self._name = name
        self._size = size
        self._children = []
        
    def __eq__(self, other):
        if isinstance(other, dentry):
            return self.parent == other.parent and \
                self.name == other.name
        return False

    @property
    def parent(self):
        return self._parent
    
    @property
    def name(self):
        return self._name
    
    @property
    def is_dir(self):
        return self._size is None
    
    @property
    def is_root(self):
        return self.parent is not None
    
    def add_child(self, child):
        if child in self._children:
            return False
        
        self._children.append(child)
        
        return True
        
    def get_next_child(self, prev = None):
        index = 0
        if prev is not None:
            for child in self._children:
                index += 1
                if child.name == prev.name:
                    break
            
        if index < len(self._children):
            return self._children[index]
        return None
    
    def __repr__(self):
        return self.get_path()
    
    def get_child(self, child_name):
        for child in self._children:
            if child.name == child_name:
                return child
        return None
    
    def get_path(self):
        path = ""
        p = self
        while p is not None:
            if p.is_dir and p.name != "/":
                path = p.name + "/" + path
            else:
                path = p.name + path
            p = p.parent
        return path
    
    def get_size(self):
        if self.is_dir:
            size = 0
            for child in self._children:
                size += child.get_size()
            return size
        else:
            return self._size
    

root = dentry(None, "/")

def change_dir(env, params, line = None):
    current_dir = env.get_current_dir()
    print("%s $ CD <%s>" % (current_dir.get_path(), params))
    if params == "..":
        if current_dir.parent is not None:
            current_dir = current_dir.parent
    elif params == "/":
        current_dir = root
    else:
        child = current_dir.get_child(params)
        if child is not None:
            current_dir = child
    
    env.set_current_dir(current_dir)
            

def list_dir(env, params, line = None):
    if line is None:
        return

    current_dir = env.get_current_dir()
    print("%s $ LS <%s>" % (current_dir.get_path(), line))
    
    size, name = line.split(" ")
    if size == "dir":
        size = None
    else:
        size = int(size)
        
    child = dentry(current_dir, name, size)
    current_dir.add_child(child)

cmd_list = {
    "cd" : change_dir,
    "ls" : list_dir
}

cmd = None
params = None
handler = None

class Environment:
    def __init__(self, current_dir = None):
        self._current_dir = current_dir
    
    def get_current_dir(self):
        return self._current_dir
    
    def set_current_dir(self, current_dir):
        self._current_dir = current_dir
        
env = Environment(root)

for line in f:
    line = line.strip()
    
    print(">>> %s" % line)
    
    if line.startswith("$ "):
        cmd = line[2:]
        params = None
        if " " in cmd:
            params = cmd[cmd.index(" ")+1:]
            cmd = cmd[:cmd.index(" ")] 
        handler = cmd_list[cmd]
        handler(env, params)
    else:
        handler(env, params, line)

def traverse(root, handler, state):
    entries = [root]
    
    while entries:
        e = entries.pop()
    
        handler(state, e)
        
        child = e.get_next_child()
        while child:
            entries.insert(0, child)
            child = e.get_next_child(child)

class State:
    def __init__(self, target):
        self._target = target
        self._size = None
        
    def add(self, size):
        if self.size is None or self.size > size:
            self._size = size
         
    @property
    def size(self):
        return self._size

    @property
    def target(self):
        return self._target

def size_more_than_target(state, entry):
    if entry.is_dir:
        size = entry.get_size()
        if size > state.target:
            state.add(size)

target = root.get_size() - (70000000 - 30000000)

print("Target: %s" % target)

state = State(target)
traverse(root, size_more_than_target, state)

print("answer: %d" % state.size)
