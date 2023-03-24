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
            'number': j,
            'is_opened': False
        })
if joker_on: trump_card.append({
    'suit': 'joker',
    'number': 'joker',
    'is_opened': False
})

def trump_length():
    return len(trump_card)

def trump_printer(trump_card):
    for i in trump_card:
        print(i)
    print()

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

def trump_sort_by_suit(card_list):
    new_card_list = []
    for i in suit:
        for j in number:
            for card in card_list:
                if card['suit'] == i and card['number'] == j:
                    new_card_list.append(card)
    for card in card_list:
        if card['suit'] == 'joker' or card['number'] == 'joker':
            new_card_list.append(card)
    return new_card_list

def trump_sort_by_number(card_list):
    new_card_list = []
    for i in number:
        for j in suit:
            for card in card_list:
                if card['number'] == i and card['suit'] == j:
                    new_card_list.append(card)
    for card in card_list:
        if card['suit'] == 'joker' or card['number'] == 'joker':
            new_card_list.append(card)
    return new_card_list

def trump_drow(trump_card):
    try:
        # random drow 
        """
        drown_card_id = random.randint(0, len(trump_card)-1)
        drown_card = trump_card[drown_card_id]
        trump_card.pop(drown_card_id)
        """
        drown_card = trump_card.pop(0)
    except Exception:
        print('Error')
        drown_card = {
            'suit': '0',
            'number': '0'
        }
    
    return drown_card


if __name__ == '__main__':
    trump_printer(trump_card)
    random.shuffle(trump_card)
    trump_printer(trump_card)
    '''
    trump_card = trump_sort_by_suit(trump_card)
    trump_printer(trump_card)
    '''
    trump_card = trump_sort_by_number(trump_card)
    trump_printer(trump_card)
    one_card = trump_drow(trump_card)
    print(one_card)
    print()
    trump_printer(trump_card)