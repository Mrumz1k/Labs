def find_first_positive_and_last_negative(arr):
    first_positive = None
    last_negative = None

    for num in arr:
        if first_positive is None and num > 0:
            first_positive = num
        if num < 0:
            last_negative = num

    return first_positive, last_negative

arr = [-3, -1, 0, 2, 5, -7, 4, -2]
first_pos, last_neg = find_first_positive_and_last_negative(arr)
print("Первый положительный элемент:", first_pos)
print("Последний отрицательный элемент:", last_neg)