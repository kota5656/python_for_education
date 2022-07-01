print("input number: ", end="")
num = input()
# ちなみにここで整数を打たないと、ValueErrorが出力される。

if int(num) % 3 == 0:
    print("fizz", end="")
if int(num) % 5 == 0:
    print("buzz")

print()