# tall, weight, age
human_list = [
    [150, 43, 14],
    [143, 35, 14],
    [158, 55, 14],
    [164, 52, 14],
    [161, 57, 14]
]

human_list = [
    {"tall": 150, "weight": 43, "age": 14},
    {"tall": 143, "weight": 35, "age": 14},
    {"tall": 158, "weight": 55, "age": 14},
    {"tall": 164, "weight": 52, "age": 14},
    {"tall": 161, "weight": 57, "age": 14},
]

for i in human_list:
    print(i["tall"])
