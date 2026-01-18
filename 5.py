quan = int(input('Сколько предметов можете взять: '))
values = list(map(int, input("Ценности этих предметов: ").split()))

values.sort(reverse=True)

max_value = sum(values[:quan])
print(max_value)
