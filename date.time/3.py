import calendar


year = int(input("Введите год (например, 2023): "))
month = int(input("Введите месяц (1-12): "))


cal = calendar.month(year, month)
print(f"Календарь для {calendar.month_name[month]} {year}:\n")
print(cal)
