from datetime import datetime

date1_str = input("Введіть першу дату (рррр-мм-дд): ")
date2_str = input("Введіть другу дату (рррр-мм-дд): ")

date_format = "%Y-%m-%d"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

delta = date2 - date1

print(f"Різниця між датами: {delta.days} днів")
