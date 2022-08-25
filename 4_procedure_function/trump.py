trump_card = []
suit = ['heart', 'diamond', 'crover', 'speed']
number = ['A', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'J', 'Q', 'K']
joker = ['joker', 'joker']

def trump_printer(trump_card):
    for i in trump_card:
        print(i)

def hit_suit(input_suit):
    count = 0
    for i in suit:
        if input_suit == i: return count
        count += 1
    print("not found suit")
    exit()

def hit_number(input_number):
    count = 0
    for i in number:
        if input_number == i: return count
        count += 1
    print("not found number")
    exit()

def trump_drow(trump_card, suit, number):
    trump_card[hit_suit(suit)][hit_number(number)] = 0
    your_card = suit, number
    return trump_card, your_card

for i in suit:
    row = []
    for j in number:
        row.append(1)
    trump_card.append(row)