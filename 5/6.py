def invert_signs(arr):
    return [-x for x in arr]

arr = [1, -5, 0, 3, -4]
inverted = invert_signs(arr)
print(inverted)  