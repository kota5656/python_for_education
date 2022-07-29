print("aの数: ")
a = input()
print("bの数: ")
b = input()

x = int(a)
y = int(b)

while(True):
    if (x != y):
        if (x > y):
            x -= y
        else:
            y -= x
    else:
        break

print(a, "と", b, "の最大公約数は、", x, "です。")