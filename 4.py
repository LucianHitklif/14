import random

lis = [[random.randint(1, 5) for _ in range(4)] for _ in range(3)]
mean = 3
pos = []

for i in range(len(lis)):
    for j in range(len(lis[i])):
        if lis[i][j] == mean:
            pos.append((i, j))

print("Список:", lis,)
print(f"{mean} на позициях:", pos)
