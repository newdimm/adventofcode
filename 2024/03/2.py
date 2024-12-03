#!/bin/python3
import sys
from curses.ascii import isdigit

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1] 

class Match:
    digits = ['0','1','2','3','4','5','6','7','8','9']
    
    def __init__(self, match_str, score_func):
        self.str = match_str
        self.score_func = score_func
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
            self.score_func(self.args)
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
                
total = 0
enabled = True

def score_total(args):
    global total
    global enabled
    
    if enabled:
        mul = 1
        for x in args:
            mul *= x
        print("total += %s == %d" % (args, mul))
        total += mul
    else:
        print("total not changed")

def score_do(args):
    global enabled
    enabled = True
    print("ENABLE")

def score_dont(args):
    global enabled
    enabled = False
    print("DISABLE")
    
m = Match("mul(@,@)", score_total)
do = Match("do()", score_do)
dont = Match("don't()", score_dont)


with open(fname) as f:
    for line in f:
        for l in line:
            m.do_match(l)
            do.do_match(l)
            dont.do_match(l)
            
print(total)
