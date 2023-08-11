import numpy as np

kuku_column = []

for i in range(1, 10):
    kuku_row = []
    for j in range(1, 10):
        kuku_row.append(i*j)
    kuku_column.append(kuku_row)

print(np.array(kuku_column))
print()

kuku_cheat = [
    [1,2,3,4,5,6,7,8,9],
    [2,4,6,8,10,12,14,16,18],
    [3,6,9,12,15,18,21,24,27],
]

print(np.array(kuku_cheat))

# -------------------------------------

character = {
    "name": "Ayato",
    "level": 1,
    "hp": 12,
    "atk": 5,
    "def": 3,
    "speed": 4 
}

print("name:", character["name"])
print("level:", character["level"])
print("hp:", character["hp"])
print("atk:", character["atk"])
print("def:", character["def"])
print("speed:", character["speed"])
