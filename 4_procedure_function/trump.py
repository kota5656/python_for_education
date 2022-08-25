trump_card = []
suit = ['heart', 'diamond', 'crover', 'speed']
number = ['A', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'J', 'Q', 'K']
joker = ['joker', 'joker']

def trump_printer(trump_card):
    for i in trump_card:
        print(i)

for i in suit:
    row = []
    for j in number:
        row.append(1)
    trump_card.append(row)