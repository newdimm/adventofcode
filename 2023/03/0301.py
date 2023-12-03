#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

class window():
    def __init__(self):
        self._size = 0
        self._result = 0

    def setsize(self,size):
        if size != self._size:
            self.line1 = ['.'] * size
            self.line2 = ['.'] * size
            self._symbols = []
            self._size = size

    def addline(self, line):
        self.setsize(len(line))

        for s in self._symbols:
            self._check(line, s)

        self.line1 = self.line2
        self.line2 = line
        self._symbols = []
        self._process()

    def _check(self, line, pos):
        self._check_once(line, pos - 1)
        self._check_once(line, pos)
        self._check_once(line, pos + 1)

    def _check_once(self, line, pos):
        if not line[pos].isdigit():
            return

        while pos > 0 and line[pos-1].isdigit():
            pos -= 1

        num = 0

        while pos >= 0 and pos < len(line) and line[pos].isdigit():
            num = num * 10 + int(line[pos])
            line[pos] = '.'
            pos += 1

        if num:
            self._score(num)

    def _score(self, num):
        print("scored: ", num)
        self._result += num

    def _process(self):
        pos = 0
        while pos < len(self.line2):
            d = self.line2[pos]

            if d.isdigit():
                pass
            elif d == '.':
                pass
            else:
                print("symbol", pos)
                self._symbols.append(pos)
                self._check(self.line1, pos)
                self._check(self.line2, pos)

            pos += 1

    def result(self):
        return self._result
    

with open(fname) as f:

    w = window()

    for line in f:
        line = line.strip()
        if not line:
            continue

        print(line)

        line = [x for x in line]

        w.addline(line)

    print(w.result())


                    







        

