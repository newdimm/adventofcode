#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

class window():
    def __init__(self):
        self._result = 0
        self._lines = []

    def addline(self, line):
        if not self._lines:
            self._lines = [[]] * 3
            for x in range(3):
                self._lines[x] = ['.'] * len(line)

        del self._lines[0]
        self._lines.append(line)


        pos = 0
        while pos < len(self._lines[1]):
            d = self._lines[1][pos]
            if d == '*':
                self._check(pos)

            pos += 1

    def _check(self, pos):
        parts = []

        for l in [0, 1, 2]:
            for p in [pos-1, pos, pos + 1]:
                result = self._get_num(self._lines[l], p)
                if result is not None: 
                    start, num = result
                    part = (num, l, start)

                    if part not in parts:
                        parts.append(part)

        if len(parts) == 2:
            part0 = parts[0][0]
            part1 = parts[1][0]
            self._score(part0, part1)

    def _get_num(self, line, pos):
        if not line[pos].isdigit():
            return None

        while pos > 0 and line[pos-1].isdigit():
            pos -= 1

        start = pos

        num = 0
        while pos < len(line) and line[pos].isdigit():
            num = num * 10 + int(line[pos])
            pos += 1

        return (start, num)

    def _score(self, part0, part1):
        print("%u * %u == %u" % (part0, part1, part0 * part1))
        self._result += part0 * part1

    def result(self):
        return self._result
    

with open(fname) as f:

    w = window()

    size = 0

    for line in f:
        line = line.strip()
        if not line:
            continue

        print(line)

        line = [x for x in line]

        size = len(line)
        w.addline(line)

    w.addline(['.'] * size)

    print(w.result())


                    







        

