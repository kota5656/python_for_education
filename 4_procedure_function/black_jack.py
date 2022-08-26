import trump

trump.trump_printer()

player_card = []
cpu_card = []

number_point = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'joker': 10,
}

def point_calc(card_list):
    a_included = 0
    sum = 0
    for card in card_list:
        if card['number'] == 'A': a_included += 1
        sum += number_point[card['number']]
    if sum > 21 and a_included > 0:
        sum = 0
        number_pattern = []
        for card in card_list:
            if card['number'] != 'A': sum += number_point[card['number']]
        tmp_sum = sum
        for i in range(a_included):
            for j in range(i):
                for k in range(a_included):
                    if j <= k: tmp_sum += 11
                    else: tmp_sum += 1
            number_pattern.append(tmp_sum)
            tmp_sum = sum
        print(number_pattern)
        sum = number_pattern.pop()
    return sum

print("your turn")
for i in range(2):
    if len(trump.trump_card) > 0:
        player_card.append(trump.trump_drow())
    else: break
for i in range(2):
    if len(trump.trump_card) > 0:
        cpu_card.append(trump.trump_drow())
    else: break

    
print("your card list")
trump.trump_printer2(player_card)

print("cpu card list")
trump.trump_printer2(cpu_card)
print("cpu2 card list")

print("public card list")
trump.trump_printer()

print(len(player_card))
print(len(cpu_card))

point = point_calc([
    {
        'suit': 'heart',
        'number': 'A'
    },
    {
        'suit': 'diamond',
        'number': 'A'
    },
    {
        'suit': 'crover',
        'number': 'A'
    },
    {
        'suit': 'speed',
        'number': 'A'
    },
])

print(point)