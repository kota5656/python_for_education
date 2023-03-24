import random
import trump



if __name__ == '__main__':
    # trump.trump_printer(trump.trump_card)
    random.shuffle(trump.trump_card)
    # trump.trump_printer(trump.trump_card)
    
    n = 4
    trump_tefuda1 = []
    trump_tefuda2 = []
    trump_tefuda3 = []
    trump_tefuda4 = []
    
    print(trump.trump_drow(trump.trump_card))
    
    print(len(trump.trump_card))
    
    while len(trump.trump_card) != 0:
        trump_tefuda1.append(trump.trump_drow(trump.trump_card))
        trump_tefuda2.append(trump.trump_drow(trump.trump_card))
        trump_tefuda3.append(trump.trump_drow(trump.trump_card))
        trump_tefuda4.append(trump.trump_drow(trump.trump_card))
    
    trump.trump_printer(trump_tefuda1)
    trump.trump_printer(trump_tefuda2)
    trump.trump_printer(trump_tefuda3)
    trump.trump_printer(trump_tefuda4)
    
    print(len(trump_tefuda1))