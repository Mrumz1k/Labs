from datetime import datetime

class Task:
    def __init__(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description

    def __repr__(self):
        return (f"Task(Start: {self.date_start}, Finish: {self.date_finish}, "
                f"Description: '{self.description}')")

tasks = [
    Task(datetime(2025, 6, 1, 9, 0), datetime(2025, 6, 1, 10, 0), "Математика"),
    Task(datetime(2025, 6, 1, 10, 30), datetime(2025, 6, 1, 12, 0), "Физика"),
    Task(datetime(2025, 6, 1, 13, 0), datetime(2025, 6, 1, 14, 0), "Химия"),
    Task(datetime(2025, 6, 1, 15, 0), datetime(2025, 6, 1, 16, 30), "Биология"),
    Task(datetime(2025, 6, 1, 17, 0), datetime(2025, 6, 1, 16, 30), "История"),
]

latest_finish = max(task.date_finish for task in tasks)

for task in tasks:
    if task.date_finish == latest_finish:
        print("Занятие, заканчивающееся позже всех:")
        print(task)
        break