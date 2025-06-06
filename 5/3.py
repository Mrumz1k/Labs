import random


def generate_sorted_even_array(size, start=0, end=100):
    even_numbers = []

    while len(even_numbers) < size:
        num = random.randint(start, end)
        if num % 2 == 0:
            even_numbers.append(num)

    even_numbers.sort()
    return even_numbers

arr = generate_sorted_even_array(10, 0, 100)
print(arr)