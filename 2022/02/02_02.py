f = open("input.txt")

LOST_SCORE = 0
DRAW_SCORE = 3
WON_SCORE = 6

game = {
    # (score, wins, loses)
    'A' : (1, 'C', 'B'),  # rock
    'B' : (2, 'A', 'C'),  # paper
    'C' : (3, 'B', 'A'),  # scissors
}

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

total_score = 0

for line in f:
    line = line.strip()
    them, what = line.split(" ")
        
    ignore0, wins, loses = game[them]
    
    if what == LOSE:
        you = wins
    elif what == WIN:
        you = loses
    else:
        you = them
        
    score, wins, loses = game[you]
        
    if you == them:
        score += DRAW_SCORE
    elif wins == them:
        score += WON_SCORE
    
    total_score += score
    
print(total_score)