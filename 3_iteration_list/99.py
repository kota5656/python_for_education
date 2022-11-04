kuku = []

for i in range(1, 10):
    column = []
    for j in range(1, 10):
        column.append(i*j)
    kuku.append(column)
    
print(kuku)
print(kuku[2])
print(kuku[3][4])