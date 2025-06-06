def sum_lengths(strings):
    return sum(len(s) for s in strings)

sequence = ["hello", "world", "Python", "GPT"]
total_length = sum_lengths(sequence)
print("Сумма длин всех строк:", total_length)