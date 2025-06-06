class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration  # в минутах

    def __repr__(self):
        return (f"FitnessCenter(ClientCode={self.client_code}, Year={self.year}, "
                f"Month={self.month}, Duration={self.duration})")

sessions = [
    FitnessCenter("C001", 2023, 6, 45),
    FitnessCenter("C002", 2023, 5, 30),
    FitnessCenter("C003", 2024, 6, 60),
    FitnessCenter("C004", 2024, 4, 20),
    FitnessCenter("C005", 2023, 6, 50),
    FitnessCenter("C006", 2025, 7, 40),
    FitnessCenter("C007", 2025, 8, 55),
    FitnessCenter("C008", 2024, 9, 15),
    FitnessCenter("C009", 2025, 10, 35),
    FitnessCenter("C010", 2023, 11, 25),
]

duration_per_year = {}
for session in sessions:
    duration_per_year[session.year] = duration_per_year.get(session.year, 0) + session.duration

max_duration = max(duration_per_year.values())

years_with_max = [year for year, total in duration_per_year.items() if total == max_duration]
min_year_with_max = min(years_with_max)

print(f"Год с наибольшей суммарной продолжительностью занятий: {min_year_with_max}")
print(f"Наибольшая суммарная продолжительность: {max_duration} минут")