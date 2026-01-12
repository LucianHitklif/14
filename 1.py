import random

rows = random.randint(1, 20)
cols = random.randint(1, 20)
lists = [[random.randint(1, 100) for i in range(cols)] for j in range(rows)]

print('Список: ')
for row in lists:
    print(row)

max_val = lists[0][0]
max_row, max_col = 0, 0

for i in range(rows):
    for j in range(cols):
        if lists[i][j] > max_val:
            max_val = lists[i][j]
            max_row, max_col = i, j

print(f'Максимальное число: {max_val}')
print(f'Позиция: {max_row, max_col}')
