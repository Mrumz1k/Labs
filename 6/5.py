def count_elements_start_end_with_c(arr, c):
    count = 0
    for s in arr:
        if len(s) > 1 and s.startswith(c) and s.endswith(c):
            count += 1
    return count

A = ["civic", "cat", "cbc", "cc", "c", "abc", "cac"]
C = "c"

result = count_elements_start_end_with_c(A, C)
print("Количество элементов:", result)