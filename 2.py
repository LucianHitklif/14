import random

lists = [[random.randint(1,100) for i in range(4)] for i in range(5)]

row_sum = [sum(row) for row in lists]
total_sum = sum(row_sum)
max_row_sum = row_sum.index(max(row_sum))

print(f'Список: {lists}')
print(f'Сумма строк: {row_sum}')
print(f'Общая сумма эл-ов: {total_sum}')
print(f'Строка с максимальной суммой: {max_row_sum}')
