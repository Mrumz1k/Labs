class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration  # продолжительность занятия в минутах

    def __repr__(self):
        return (f"FitnessCenter(ClientCode={self.client_code}, Year={self.year}, "
                f"Month={self.month}, Duration={self.duration} мин)")

sessions = [
    FitnessCenter("C001", 2025, 6, 45),
    FitnessCenter("C002", 2025, 5, 30),
    FitnessCenter("C003", 2025, 6, 60),
    FitnessCenter("C004", 2025, 4, 20),
    FitnessCenter("C005", 2025, 6, 50),
]

longest_session = max(sessions, key=lambda x: x.duration)
shortest_session = min(sessions, key=lambda x: x.duration)

print("Самое продолжительное занятие:")
print(longest_session)

print("\nСамое короткое занятие:")
print(shortest_session)