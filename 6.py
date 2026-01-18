prices = list(map(int, input().split()))

print("Сортировка по возрастанию:", sorted(prices))
print("Сортировка по убыванию:", sorted(prices, reverse=True))
print("Оригинальный порядок (от старых к новым):", prices)
print("Обратный порядок (от новых к старым):", list(reversed(prices)))
