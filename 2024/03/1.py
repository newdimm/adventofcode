#!/bin/python3
import sys
from curses.ascii import isdigit

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

class Match:
    digits = ['0','1','2','3','4','5','6','7','8','9']
    
    def __init__(self, match_str):
        self.str = match_str
        self.total = 0
        
        self.reset()
        
    def get_total(self):
        return self.total
        
    def reset(self):
        self.pos = 0
        self.arg = ""
        self.args = []
        
    def arg_is_valid(self):
        return len(self.arg) in [1,2,3]
    
    def cur(self):
        return self.str[self.pos]
    
    def next(self):
        self.pos += 1
        
        if self.pos == len(self.str):
            mul = 1
            for x in self.args:
                mul *= x
            print("total += %s == %d" % (self.args, mul))
            self.total += mul
            self.reset()
    
    def do_match(self, sym):
        if self.cur() == "@":
            if sym in self.digits:
                self.arg += sym
            else: ### no match
                if self.pos == 0:
                    return
                
                if self.arg_is_valid():
                    print("@=%s" % self.arg)
                    self.args.append(int(self.arg))
                    self.arg = ""
                    self.next()
                else:
                    self.reset()
                    
                self.do_match(sym)
        else:
            if sym == self.cur():
                self.next()
            else: # no match
                if self.pos != 0:
                    self.reset()
                    self.do_match(sym)
                
            
m = Match("mul(@,@)")

with open(fname) as f:
    for line in f:
        for l in line:
            m.do_match(l)
            
print(m.get_total())
