with open('AOC_2022_day2.txt', 'r') as f:
    rounds = f.read().split('\n')

def AOC_2022_day2_pt1(rounds):
    outcomes = {'A X': 3 + 1, 'A Y': 6 + 2, 'A Z': 0 + 3,
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3,
                'C X': 6 + 1, 'C Y': 0 + 2, 'C Z': 3 + 3}
    score = sum(outcomes[i] for i in rounds)
    return score

def AOC_2022_day2_pt2(rounds):
    outcomes = {'A X': 0 + 3, 'A Y': 3 + 1, 'A Z': 6 + 2,
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3,
                'C X': 0 + 2, 'C Y': 3 + 3, 'C Z': 6 + 1}
    score = sum(outcomes[i] for i in rounds)
    return score

print(AOC_2022_day2_pt1(rounds))
print(AOC_2022_day2_pt2(rounds))
