#!/bin/python3
import sys

fname = "input"

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == "test":
            fname = "input_test"

FIVE_OF_KIND = 7
FOUR_OF_KIND = 6
FULL_HOUSE = 5
THREE_OF_KIND = 4
TWO_PAIRS = 3
ONE_PAIR = 2
HIGH = 1

def get_type(cards):
    counts = {
    }
    for c in cards:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    count_list = []
    for card,count in counts.items():
        count_list.append(count)

    count_list.sort()
    if count_list[-1] == 5:
        return FIVE_OF_KIND
    elif count_list[-1] == 4:
        return FOUR_OF_KIND
    elif count_list[-1] == 3:
        if count_list[-2] == 2:
            return FULL_HOUSE
        else:
            return THREE_OF_KIND
    elif count_list[-1] == 2:
        if count_list[-2] == 2:
            return TWO_PAIRS
        else:
            return ONE_PAIR
    else:
        return HIGH

values = {
        "A" : 13,
        "K" : 12,
        "Q" : 11,
        "J" : 10,
        "T" : 9,
        "9" : 8,
        "8" : 7,
        "7" : 6,
        "6" : 5,
        "5" : 4,
        "4" : 3,
        "3" : 2 ,
        "2" : 1 
}

def hand_score(hand):
    score = 0

    mult = 16 ^ len(hand)
    score += mult * get_type(hand)

    for card in hand:
        mult /= 16
        score += mult * values[card]

    return score

bids = {
}
hands = []

with open(fname) as f:

    for line in f:
        line = line.strip()
        if not line:
            continue

        hand, bid = line.split(" ")
        bid = int(bid)
        bids[hand] = bid
        hands.append(hand)

        print("hand %s type %d bid %d score %d" % (hand, get_type(hand), bid, hand_score(hand)))

hands.sort(key=hand_score)
print(hands)

rank = 1
result = 0
for h in hands:
    score = rank * bids[h]
    print("[%d] %s score %d" % (rank, h, score))
    result += score
    rank += 1


print("result", result)


