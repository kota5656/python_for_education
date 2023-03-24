import random
import trump

# 手札の中から被った2枚を山札へ還す処理
def throw_pair_cards(member_hand: list):
    throw_index_list = []
    for number in trump.number:
        card_index_list = []
        for card_index in range(len(member_hand)):
            if member_hand[card_index]["number"] == number:
                card_index_list.append(card_index)
        if len(card_index_list) // 2 == 1:
            throw_index_list.append(card_index_list[0])
            throw_index_list.append(card_index_list[1])
        if len(card_index_list) == 4:
            for card_index in card_index_list:
                throw_index_list.append(card_index)
    
    new_card_list = []
    for card_index in range(len(member_hand)):
        hit = False
        for throw_index in throw_index_list:
            if card_index == throw_index: hit = True
        if hit: trump.trump_card.append(member_hand[card_index])
        else: new_card_list.append(member_hand[card_index])
    
    return new_card_list




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
        if trump.trump_card != []: # メンバーが一巡する途中でカードを切らすのを防ぐため
            member["hand"].append(trump.trump_drow(trump.trump_card))

for member in members:
    member["hand"] = trump.trump_sort_by_number(member["hand"])
    member["hand"] = throw_pair_cards(member["hand"])
    trump.trump_printer(member["hand"])

trump.trump_printer(trump.trump_card)

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