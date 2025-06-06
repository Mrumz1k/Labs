def extract_positive_numbers(arr):
    return [x for x in arr if x > 0]

sequence = [-5, 3, 0, 7, -1, 4, -2]
positives = extract_positive_numbers(sequence)
print("Положительные числа:", positives)