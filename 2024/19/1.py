#!/bin/python3
import sys, time, heapq

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]

read_patterns = True

pts = []
twls = []

with open(fname) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
            
        if read_patterns:
            pts = [x.strip() for x in line.split(",")]
            
            read_patterns = False
            continue
            
        twls.append(line)
        
        
print(pts)
print(twls)


class TrieNode:
    def __init__(self, text=""):
        self.text = text
        self.is_word = False
        self.children = {}
        
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        #print("    TRIE: insert <%s>" % word)
        for i,c in enumerate(word):
            if c not in current.children:
                prefix = word[0:i+1]
                current.children[c] = TrieNode(prefix)
                #print("        TRIE: NODE<%s> pfx=<%s>" % (c, prefix))
            current = current.children[c]
        current.is_word = True
        #print("      TRIE: <%s>.is_word" % current.text)
        
    def find(self, word):
        current = self.root
        #print("    TRIE: find <%s>" % word)
        for i,c in enumerate(word):
            if c not in current.children:
                #print("      TRIE: <%s> NOT IN" % c)
                return None
            #print("        TRIE: <%s>" % c)
            current = current.children[c]
        if current.is_word:
            #print("      TRIE: <%s> IS WORD" % current.text)
            return current
        #print("      TRIE: <%s> NOT IS WORD" % current.text)
        return None
    def starts_with(self, word):
        #print("    TRIE: starts <%s>" % word)
        current = self.root
        for i,c in enumerate(word):
            if c not in current.children:
                #print("    TRIE: <%s> NOT IN" % c)
                return []
            current = current.children[c]
            #print("    TRIE: +<%s> pfx %s is_word %d" % (c, current.text, current.is_word))
        
        result = []
        stack = [current]
        while stack:
            current = stack.pop()
            #print("    TRIE: pop <%s>" % current.text)
            if current.is_word:
                #print("    TRIE: IS WORD")
                result.append(current.text)
            #print("    TRIE: NOT IS WORD")
            for c in current.children.keys():
                #print("    TRIE: +stack<%s>" % current.children[c].text)
                stack.append(current.children[c])
        #print("return: %s" % result)
        return result

t = PrefixTree()

for p in pts:
    t.insert(p)

count = 0
    
for tw in twls:
    stack = [tw]
    possible = False
    while stack:
        prefix = stack.pop()
        #print("prefix=<%s>" % prefix)

        if prefix == "":
            possible = True
            break
        
        pos = 0
        while pos < len(prefix):
            test_prefix = prefix[:pos+1]
            if t.find(test_prefix):
                new_prefix = prefix[pos+1:]
                #print("+<%s> add <%s>" % (test_prefix, new_prefix))
                stack.append(new_prefix)
            else:
                variants = t.starts_with(test_prefix)
                for v in variants:
                    if prefix.startswith(v):
                        new_prefix = prefix[len(v):]
                        #print("+<%s> add <%s>" % (test_prefix, new_prefix))
                        stack.append(new_prefix)
                #print("-<%s>" % (prefix[:pos+1]))
                break
            pos += 1
    print("<%s> %d" % (tw, possible))
    if possible:
        count += 1
        
print("count possible: %d" % count)
        