array = []

print("Введите 14 чисел:")
for i in range(14):
    num = int(input(f"Введите число {i+1}: "))
    array.append(num)

array.append(sum(array))

print("Элементы массива:")
for element in array:
    print(element)