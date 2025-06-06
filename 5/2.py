def analyze_numbers(arr):
    sum_positive = sum(x for x in arr if x > 0)

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    product = 1
    for num in arr[start:end]:
        product *= num

    return sum_positive, product


numbers = [3, -1, 4, 1, 5, 9, -2, 6]
sum_pos, prod_between = analyze_numbers(numbers)
print("Сумма положительных элементов:", sum_pos)
print("Произведение чисел между мин и макс элементами:", prod_between)