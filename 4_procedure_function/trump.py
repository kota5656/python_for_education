import random

trump_card = []
suit = ['heart', 'diamond', 'crover', 'speed']
number = ['A', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'J', 'Q', 'K']
joker_on = True

for i in suit:
    for j in number:        
        trump_card.append({
            'suit': i,
            'number': j
        })
if joker_on: trump_card.append({
    'suit': 'joker',
    'number': 'joker'
})

def trump_length():
    return len(trump_card)

def trump_printer():
    for i in trump_card:
        print(i)

def trump_printer2(card_list):
    for i in suit:
        for j in number:
            for card in card_list:
                if card['suit'] == i and card['number'] == j:
                    print(card)
    for card in card_list:
        if joker_on:
            if card['suit'] == 'joker' and card['number'] == 'joker':
                print(card)

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

def trump_drow():
    try: 
        drown_card_id = random.randint(0, len(trump_card)-1)
        drown_card = trump_card[drown_card_id]
        trump_card.pop(drown_card_id)
    except Exception:
        print('Error')
        drown_card = {
            'suit': '0',
            'number': '0'
        }
    
    return drown_card