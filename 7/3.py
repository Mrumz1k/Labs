def extract_and_sort_positive_two_digit(arr):
    filtered = [x for x in arr if 10 <= x <= 99]
    filtered.sort()
    return filtered

sequence = [5, 12, 99, 100, 8, 34, 87, 7, 21, -15, 55]
result = extract_and_sort_positive_two_digit(sequence)
print("Положительные двузначные числа, отсортированные:", result)