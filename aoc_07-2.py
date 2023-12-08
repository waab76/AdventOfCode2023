from functools import cmp_to_key

input = open('aoc_07.txt', 'r')
lines = input.readlines()

card_values = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7,
               '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}

def compute_key(cards):
    card_sets = {}
    for card in cards:
        if not card in card_sets:
            card_sets[card] = 1
        else:
            card_sets[card] += 1
    joker_count = card_sets['J'] if 'J' in card_sets else 0
    if 5 == len(card_sets):
        # No pairs, but if we have a joker, it makes a pair
        hand_rank = 0 + joker_count
    elif 4 == len(card_sets):
        # One pair
        hand_rank = 1
        # If we have a joker, the pair becomes trips (even if it's a pair of jokers)
        if joker_count > 0:
            hand_rank = 3
    elif 3 == len(card_sets):
        # Trips or 2 pair
        hand_rank = 2
        for card in card_sets:
            if 3 == card_sets[card]:
                hand_rank = 3
        if 2 == hand_rank and 2 == joker_count:
            hand_rank = 5
        elif 2 == hand_rank and 1 == joker_count:
            hand_rank = 4
        elif 3 == hand_rank and joker_count > 0:
            hand_rank = 5
    elif 2 == len(card_sets):
        # quads or full boat
        hand_rank = 4
        for card in card_sets:
            if 4 == card_sets[card]:
                hand_rank = 5
        if joker_count > 0:
            # Any jokers makes it 5 of a kind
            hand_rank = 6
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

# First answer 249519293 was too low
print(winnings)