import random
from re import S

lst = []

for i in range(5):
    elm = random.randint(0,1) 
    lst.append(elm)

print(lst) # debug

tmp = 0
zerocount = 0
onecount = 1
for elm in lst:
    if tmp == elm:
        if elm == 1: onecount += 1
        else: zerocount += 1
    else:
        if elm == 1: onecount = 0
        else: zerocount = 0
    tmp = elm
        
print(zerocount, onecount) # debug

if zerocount >= 3:
    print("黒の勝利です")
elif onecount >= 3:
    print("白の勝利です")
else:
    print("引き分けです。")