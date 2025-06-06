import datetime
import locale


try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')
    except locale.Error:
        print("⚠️ Русская локаль не поддерживается на этой системе.")


def format_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%d.%m.%Y")

        formatted_date = date_obj.strftime("%A, %-d %B, %Y год")

        return formatted_date.capitalize()
    except ValueError:
        return "Неверный формат даты. Используйте ДД.ММ.ГГГГ"


user_input = input("Введите дату (в формате ДД.ММ.ГГГГ): ")
print(format_date(user_input))