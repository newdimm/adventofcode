f = open("input.txt")

LOST = 0
DRAW = 3
WON = 6

game = {
    # (score, wins)
    'A' : (1, 'C'),  # rock
    'B' : (2, 'A'),  # paper
    'C' : (3, 'B'),  # scissors
}

encoding = {
    'X' : 'A',
    'Y' : 'B',
    'Z' : 'C'
}

total_score = 0

for line in f:
    line = line.strip()
    them, you = line.split(" ")
    
    you = encoding[you]
    
    score, wins = game[you]
    
    if you == them:
        score += DRAW
    elif wins == them:
        score += WON
    
    total_score += score
    
print(total_score)