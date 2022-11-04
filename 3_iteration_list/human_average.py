tall_list = [150, 143, 158, 164, 161]

tall_sum = 0
for i in tall_list:
    print(i)
    tall_sum += i

tall_average = tall_sum / len(tall_list)

print(tall_sum, tall_average)