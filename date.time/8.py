from datetime import datetime

dob_str = input("Введіть дату народження (рррр-мм-дд): ")

date_format = "%Y-%m-%d"
dob = datetime.strptime(dob_str, date_format)

current_date = datetime.now()

age = current_date.year - dob.year

if current_date.month < dob.month or (current_date.month == dob.month and current_date.day < dob.day):
    age -= 1


print(f"Ваш вік в поточному році: {age} років")
