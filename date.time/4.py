import time
import datetime

current_time = time.localtime()

time_format_time = time.strftime("%H:%M:%S", current_time)
time_format_date = time.strftime("%Y-%m-%d", current_time)

current_datetime = datetime.datetime.now()

datetime_format_time = current_datetime.strftime("%H:%M:%S")
datetime_format_date = current_datetime.strftime("%Y-%m-%d %A")

print("Поточний час за допомогою модуля time:")
print("Час:", time_format_time)
print("Дата:", time_format_date)
print("\nПоточний час за допомогою модуля datetime:")
print("Час:", datetime_format_time)
print("Дата:", datetime_format_date)
