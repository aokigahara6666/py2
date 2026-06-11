count = int(input("Введите количество элементов в списке: "))
elements = []

for _ in range(count):
    item = input("Введите элемент списка: ")
    elements.append(item)

power = int(input("Введите степень: "))
result = []

for item in elements:
    if item.lstrip('-').isdigit():
        num = int(item)
        result.append(str(num ** power))
    else:
        result.append(item * power)

print("Вывод:", " ".join(result))