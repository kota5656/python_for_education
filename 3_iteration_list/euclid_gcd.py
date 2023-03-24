print("aの数: ", end="")
a = input()
print("bの数: ", end="")
b = input()

x = int(a)
y = int(b)

'''
while True:
    if x != y:
        if x > y: x -= y
        else: y -= x
    else: break
'''

while x != y:
    if x > y: x -= y
    else: y -= x

print(a, "と", b, "の最大公約数は、", x, "です。")