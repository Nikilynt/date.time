from datetime import datetime

specified_date_str = input("Введіть вказану дату (рррр мм дд гг хх мм сс): ")
current_date_str = input("Введіть поточну дату (рррр мм дд гг хх мм сс): ")


specified_date_parts = map(int, specified_date_str.split())
current_date_parts = map(int, current_date_str.split())


specified_date = datetime(*specified_date_parts)
current_date = datetime(*current_date_parts)


time_difference = current_date - specified_date

days, seconds = divmod(time_difference.total_seconds(), 24*60*60)
hours, seconds = divmod(seconds, 60*60)
minutes, seconds = divmod(seconds, 60)

print(f"Різниця часу між вказаною та поточною датою: {int(days)} днів, {int(hours)} годин, {int(minutes)} хвилин, {int(seconds)} секунд")

