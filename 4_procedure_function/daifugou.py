import trump

trump.trump_printer()

player_card = []
cpu_card = []
cpu_card2 = []
cpu_card3 = []

print("your turn")
for i in range(len(trump.trump_card)):
    if len(trump.trump_card) > 0:
        player_card.append(trump.trump_drow())
    if len(trump.trump_card) > 0:
        cpu_card.append(trump.trump_drow())
    if len(trump.trump_card) > 0:
        cpu_card2.append(trump.trump_drow())
    if len(trump.trump_card) > 0:
        cpu_card3.append(trump.trump_drow())
    else: break
    
print("your card list")
trump.trump_printer2(player_card)

print("cpu card list")
trump.trump_printer2(cpu_card)
print("cpu2 card list")
trump.trump_printer2(cpu_card2)
print("cpu3 card list")
trump.trump_printer2(cpu_card3)

print("public card list")
trump.trump_printer()

print(len(player_card))
print(len(cpu_card))
print(len(cpu_card2))
print(len(cpu_card3))