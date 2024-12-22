#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
cmds = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        cmds.append(line)

class BaseDial:
    map = {}
    buttons = []
    
    moves = {
        ( 1, 0) : ">",
        (-1, 0) : "<",
        ( 0, 1) : "v",
        ( 0,-1) : "^"
    }
    
    def __init__(self, upstream, state = "A", name = "BaseDial"):
        self._upstream = upstream
        self._state = state
        self._paths = self._build_paths()
        self.name = name
        self._cache = {}
            
    def _find_sp(self, nf, nt):
        #print("%s::_build_paths(%s,%s))" % (self.name, nf, nt))
        if nf == nt:
            return [""]
            
        for x,y in self.map.keys():
            if self.map[(x,y)] == nf:
                break
        fx,fy = (x,y)
        #print("from (%d,%d)" % (fx,fy))
        
        all_paths = []
        path = ""
        stack = [(x,y, path)]
        seen = {(x,y):path}
        while stack:
            x,y,path = stack.pop(0)
            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy
                if (nx,ny) in self.map:
                    npath = path + self.moves[(dx,dy)]
                    if (nx,ny) not in seen or len(seen[(nx,ny)]) == len(npath):
                        seen[(nx,ny)] = npath
                        if self.map[(nx,ny)] == nt:
                            #print("to (%d,%d)" % (nx,ny))
                            all_paths.append(npath)
                            continue
                        stack.append((nx,ny,npath))
        return all_paths
        
    def _build_paths(self):
        #print("%s::_build_paths)" % (self.name))
        paths = {}
        for nf in self.buttons:
            for nt in self.buttons:
                paths[(nf,nt)] = self._find_sp(nf,nt)
        return paths
    
    def set_state(self, new_state):
        #print("%s: %s -> %s" % (self.name, self._state, new_state))
        self._state = new_state
    
    def get_paths(self, new_state):
        #print("%s::paths(%s,%s)=%s" % (self.name, self._state, new_state, self._paths[(self._state, new_state)]))
        return self._paths[(self._state, new_state)]
        
        
    def press(self, new_state):
        
        if (self._state, new_state) in self._cache:
            min_len = self._cache[(self._state, new_state)]
        else:
            paths = self.get_paths(new_state)
            
            if not self._upstream:
                min_len = len(paths[0] + "A")
            else:
                min_len = None
                for path in paths:
                    #print("%s::press(%s) TRY path: %s" % (self.name, new_state, path))
                    path_len = 0
                    
                    for p in path:
                        path_len += self._upstream.press(p)
                    path_len += self._upstream.press("A")
                    if not min_len or min_len > path_len:
                        min_len = path_len
                    
                #print("got len(%d): %s" % (len(sequence), sequence)
            self._cache[(self._state, new_state)] = min_len
            
        self.set_state(new_state)
        
        return min_len

        
class NumDial(BaseDial):
    map = {
    (0,0):"7", (1,0):"8", (2,0):"9",
    (0,1):"4", (1,1):"5", (2,1):"6",
    (0,2):"1", (1,2):"2", (2,2):"3",
               (1,3):"0", (2,3):"A"
    }
    mx = 3
    my = 4
    buttons = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]
    
    name = "numdial"

    def __init__(self, upstream, state = "A", name = "NumDial"):
        super().__init__(upstream, state, name)


class ArrowDial(BaseDial):
    map = {
                   (1,0):"^", (2,0):"A",
        (0,1):"<", (1,1):"v", (2,1):">"
    }
    mx = 3
    my = 2
    buttons = [">", "v", "<", "^", "A"]
    
    name = "arrowdial"

    def __init__(self, upstream, state = "A", name = "ArrowDial"):
        super().__init__(upstream, state, name)
        
    

dial_prev = None
for i in range(25):
    dial_prev = ArrowDial(dial_prev, "A", "arrowdial%d"%i)
dial4 = NumDial(dial_prev, "A", "numdial1")

score = 0

for cmd in cmds:
    seq = 0
    for c in cmd:
        seq += dial4.press(c)
        
    print("%s: len %d" % (cmd, seq))
    
    score += seq * int(cmd[:3])

print("score: %d" % score)

