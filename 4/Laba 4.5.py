try:
    a = 10
    b = 2
    result = a / b
    print("Результат:", result)
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except Exception as e:
    print("Произошла ошибка:", e)