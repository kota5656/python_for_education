import random

mahjong_tiles = []
suits = ['characters', 'dots', 'bamboo']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
honours = ['east', 'south', 'west', 'north', 
           'white', 'green', 'red']
flower_on = True

member_tiles = []
member_thrown_tiles = []

for i in suits:
    for j in number:
        for k in range(4):
            mahjong_tiles.append({
                'type': i,
                'number': j
            })
for i in honours:
    for j in range(4):
        mahjong_tiles.append({
            'type': 'honours',
            'honours': i
        })
if flower_on: 
    for i in range(4):
        mahjong_tiles.append({
            'type': 'flower',
            'flower': 'flower'
        })

def tile_length():
    print(len(mahjong_tiles))

def tile_printer():
    for i in mahjong_tiles:
        print(i)

def member_tiles_printer(player=None):
    print()
    if player == None:        
        for i in member_tiles:
            print()
            for j in i:
                print(j)
    else:
        for i in member_tiles[player]:
            print(i)
    print()

def deal_tiles(members=4):
    random.shuffle(mahjong_tiles)
    # make member's tiles
    for i in range(members):
        member_tiles.append([])
        member_thrown_tiles.append([])
    # distribute tiles to member
    for i in range(13):
        for j in range(members):
            tile = mahjong_tiles.pop(0)
            member_tiles[j].append(tile)

def sort_member_tiles(player=0):
    weight_list = []
    weight_dict = {}
    new_members_tiles = []
    for i in member_tiles[player]:
        weight = 0
        if i['type'] == 'honours':
            weight = 30 + honours.index(i['honours'])
        elif i['type'] == 'flower':
            weight = 40
        else:
            weight = 10 * suits.index(i['type']) + i['number']
        weight_list.append(weight)
        weight_dict[weight] =  i
    # print(weight_list)
    weight_list.sort()
    # print(weight_list)
    for i in weight_list:
        new_members_tiles.append(weight_dict[i])
    '''
    for i in new_members_tiles:
        print(i)
    '''
    member_tiles[player] = new_members_tiles

def draw_tile(player=0):
    tile = mahjong_tiles.pop(0)
    member_tiles[player].append(tile)
    # sort_member_tiles(player=player)

def throw_tile(player=0, tile_index=0):
    tile = mahjong_tiles.pop(tile_index)
    member_thrown_tiles[player].append(tile)

if __name__ == "__main__":
    print('Welcome to Mahjong')
    print('choose members: (3 or 4): ',end="")
    members = input()
    members = int(members)
    # tile_length()
    deal_tiles(members=members)
    # tile_length()
    # tile_printer()
    # member_tiles_printer()
    # print()
    for i in range(members):
        sort_member_tiles(player=i)
    member_tiles_printer()
    
    print("メンバーは", members, "人です") 
    
    count = 0
    count += 1
    print(count, "順目")
    while True:        
        for i in range(members):
            print(i+1, "人目の番です")
            # member_tiles_printer(player=i)
            draw_tile(player=i)
            member_tiles_printer(player=i)
            print("捨てる牌を選択してください(index):", end="")
            tile_index = input()
            tile_index = int(tile_index)
            throw_tile(player=i, tile_index=tile_index)
            sort_member_tiles(player=i)
            member_tiles_printer(player=i)
            
            if len(mahjong_tiles) == 0:
                print("流局")
                exit()