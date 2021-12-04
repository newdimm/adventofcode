#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

bitmask = []

numbers = list(map(int, f.readline().split(",")))
max_len = len(numbers) + 1

boards = []
board = []

for line in f:
    line = line.split()
    if len(line) < 2:
        if board:
            boards.append(board)
            board = []
        continue
    
    row = []
    for l in line:
        r = int(l)
        try:
            index = numbers.index(r)
        except ValueError:
            index = max_len
        
        row.append((r, index))
    board.append(row)

if board:
    boards.append(board)

num_cols = len(boards[0][0])
num_rows = len(board[0])

max_board_score = 0
max_value = 0

for board in boards:
    col_maxes = [0] * num_cols
    row_maxes = [0] * num_rows

    ridx = 0
    for row in board:
        cidx = 0    
        for num,index in row:
            if index > col_maxes[cidx]:
                col_maxes[cidx] = index
            if index > row_maxes[ridx]:
                row_maxes[ridx] = index
            cidx += 1
        ridx += 1
    
    board_min = min(row_maxes + col_maxes)
    if board_min > max_value:
        max_value = board_min

        score = 0
        for row in board:
            for num,index in row:
                if index > board_min:
                    score += num

        max_board_score = score * numbers[board_min]

print("max_value num[%d]=%d score %d" % (max_value, numbers[max_value], max_board_score))




