# rock
A="A"
X="X"

# paper
B="B"
Y="Y"

# scissors
C="C"
Z="Z"

# X means lose
# Y means draw
# Z means win


def calc_new(round):
    score = 0
    opp_throw = round[0]
    your_move = round[1]

    if your_move == X:
        score += 0
        if opp_throw == A:
            score += 3
        elif opp_throw == B:
            score += 1
        elif opp_throw == C:
            score += 2
    elif your_move == Y:
        score += 3
        if opp_throw == A:
            score += 1
        elif opp_throw == B:
            score += 2
        elif opp_throw == C:
            score += 3
    elif your_move == Z:
        score += 6
        if opp_throw == A:
            score += 2
        elif opp_throw == B:
            score += 3
        elif opp_throw == C:
            score += 1

    return score

def calculate_rps(hand1, hand2):
    if hand1 == A:
        hand1 = "rock"
    elif hand1 == B:
        hand1 = "paper"
    elif hand1 == C:
        hand1 = "scissors"
    if hand2 == X:
        hand2 = "rock"
    elif hand2 == Y:
        hand2 = "paper"
    elif hand2 == Z:
        hand2 = "scissors"

    if hand1 == "rock":
        if hand2 == "rock":
            return 1+3
        elif hand2 == "paper":
            return 2+6
        elif hand2 == "scissors":
            return 3+0
    elif hand1 == "paper":
        if hand2 == "rock":
            return 1+0
        elif hand2 == "paper":
            return 2+3
        elif hand2 == "scissors":
            return 3+6
    elif hand1 == "scissors":
        if hand2 == "rock":
            return 1+6
        elif hand2 == "paper":
            return 2+0
        elif hand2 == "scissors":
            return 3+3

score = 0
with open("2.input", 'r') as guide:
    a = guide.readlines()
for line in a:

    round = line.strip().split(" ")

    #score += calculate_rps(round[0], round[1])
    score += calc_new(round)
    print(score)