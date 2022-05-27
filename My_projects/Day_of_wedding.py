from _datetime import datetime, timedelta

now = datetime.now()
wedding_day = datetime(2022, 6, 24)
wedding_time = timedelta.days
period = wedding_day - now
print("Сейчас", now)
den = (1, 21, 31, 41, 51, 61, 71, 81)
dnya = (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84)

if period.days in den:
    print(f"До свадьбы остался {period.days} день!")
elif period.days in dnya:
    print(f"До свадьбы осталось {period.days} дня!")
else:
    print(f"До свадьбы осталось {period.days} дней!")


# print(wedding_time)