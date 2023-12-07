from functools import cmp_to_key

input = open('aoc_07.txt', 'r')
lines = input.readlines()

card_values = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6,
               '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

def compute_key(cards):
    card_sets = {}
    for card in cards:
        if not card in card_sets:
            card_sets[card] = 1
        else:
            card_sets[card] += 1
    if 5 == len(card_sets):
        hand_rank = 0
    elif 4 == len(card_sets):
        hand_rank = 1
    elif 3 == len(card_sets):
        # Trips or 2 pair
        hand_rank = 2
        for card in card_sets:
            if 3 == card_sets[card]:
                hand_rank = 3
    elif 2 == len(card_sets):
        # quads or full boat
        hand_rank = 4
        for card in card_sets:
            if 4 == card_sets[card]:
                hand_rank = 5
    else:
        # 5 of a kind
        hand_rank = 6
    return card_values[cards[4]] + 13 * (card_values[cards[3]] + 13 * (card_values[cards[2]] + 13 * (card_values[cards[1]] + 13 * (card_values[cards[0]] + 13 * hand_rank))))

def hand_key(hand):
    return hand['key']

hands = []

for line in lines:
    hand = {}
    hand['cards'] = line.strip().split()[0]
    hand['bid'] = int(line.strip().split()[1])
    hand['key'] = compute_key(hand['cards'])
    
    hands.append(hand)
    
hands.sort(key=hand_key)
winnings = 0

for hand_num in range(len(hands)):
    winnings += hands[hand_num]['bid'] * (hand_num + 1)
    
print(winnings)
