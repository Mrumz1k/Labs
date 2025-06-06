N = int(input("Введите число N: "))

total = 0
for i in range(1, N + 1):
    total += i

print("Сумма чисел от 1 до", N, "равна", total)