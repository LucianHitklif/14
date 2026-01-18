import random

nes_list = [
    [random.randint(-20, 20) for i in range(random.randint(1, 10))]
    for i in range(random.randint(1, 10))
    ]

print("Исходный список:")
for row in nes_list:
    print(row)

fil_list = []
for row in nes_list:
    fil_row = [num for num in row if num > 0]
    if fil_row:
        fil_list.append(fil_row)

print("Отфильтрованный список:")
for row in fil_list:
    print(row)
