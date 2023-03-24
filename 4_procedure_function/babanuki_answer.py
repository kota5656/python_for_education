import random
import trump

def throw_pair_cards(member_hand):
    number_count_dict = {
        'A': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
        '10': [],
        'J': [],
        'Q': [],
        'K': [],
        'joker': [],
    }
    card_registered = []
    card_index = 0
    for card in member_hand:
        number_count_dict[card["number"]].append(card_index)
        card_index += 1
    print(number_count_dict)
    for card_index_list in number_count_dict.values:
        if len(card_index_list) >= 2:
            if len(card_index_list) == 4:
                trump.trump_card.append(member_hand[card_index_list[0]])
                trump.trump_card.append(member_hand[card_index_list[1]])
                trump.trump_card.append(member_hand[card_index_list[2]])
                trump.trump_card.append(member_hand[card_index_list[3]])
            else:
                trump.trump_card.append(member_hand[card_index_list[0]])
                trump.trump_card.append(member_hand[card_index_list[1]])
                
    print()



random.shuffle(trump.trump_card)

print("参加者を入力してください: ", end="")
member_count = int(input())

members = []
ranking = 0
for i in range(member_count):
    print(i+1, "人目")
    print("名前: ", end="")
    name = input()
    members.append({
        "name": name,
        "hand": [],
        "ranking": 0
    })

while trump.trump_card != []:
    for member in members:
        if trump.trump_card != []:
            member["hand"].append(trump.trump_drow(trump.trump_card))

for member in members:
    member["hand"] = trump.trump_sort(member["hand"])
    trump.trump_printer(member["hand"])
    throw_pair_cards(member["hand"])

turn = 0
while ranking <= member_count-1:
    print(
        members[turn % member_count]["name"], 
        "さん、\n", 
        members[(turn+1) % member_count]["name"],
        "さんのカードを一枚引いてください。\n", 
        "0 ~", len(members[(turn+1) % member_count]["hand"]) -1, ": ", end=""
    )
    card_index = int(input())
    members[turn % member_count]["hand"].append(members[turn % member_count]["hand"].pop(card_index))
    
    turn += 1
    if members[turn % member_count]["hand"] == [] and members[turn % member_count]["ranking"] == 0:
        ranking += 1
        members[turn % member_count]["ranking"] = ranking
    if members[(turn+1) % member_count]["hand"] == [] and members[(turn+1) % member_count]["ranking"] == 0:
        ranking += 1
        members[(turn+1) % member_count]["ranking"] = ranking

print("結果発表")
for member in members:
    print(member["name"], "さん、", member["ranking"], "位！！")

print("終了", "enterを押してください", input())