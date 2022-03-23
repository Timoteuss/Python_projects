from _datetime import datetime, timedelta

now = datetime.now()
wedding_day = datetime(2022, 6, 24)
wedding_time = timedelta.days
period = wedding_day - now
print("Сейчас", now)
print(f"До свадьбы осталось {period.days} дня(дней)")
# print(wedding_time)