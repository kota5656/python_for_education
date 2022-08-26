number_last = 37 # ロト7の番号の数
fill_number = 7 # ロト7の番号を埋める数

'''
all patterns
'''
all_pattern = 1
for i in range(fill_number):
    print(number_last-i, i+1)
    all_pattern *= number_last-i
    all_pattern /= i+1

'''
each point(r)
'''
points = []
for r in range(fill_number):
    point = 1
    for i in range(r+1):
        print('2:',i)
        point *= number_last-i
        point /= i+1
    for i in range(number_last-fill_number):
        point *= number_last-fill_number-i
        point /= i+1
    points.append(point)

print("all pattern: ", all_pattern)
print(points)
for i in points:
    print(i / all_pattern)