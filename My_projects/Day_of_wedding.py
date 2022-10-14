from _datetime import datetime, timedelta


now = datetime.now()
wedding_day = datetime(2022, 6, 24)
wedding_time = timedelta.days
period = wedding_day - now
print("Сейчас", now)
period_days = period.days

if period_days > 0:
    if str(period_days)[-1] == "1":
        print(f"До свадьбы остался {period_days} день!")
    elif str(period_days)[-1] == "2" or str(period_days)[-1] == "3" or str(period_days)[-1] == "4":
        print(f"До свадьбы осталось {period_days} дня!")
    else:
        print(f"До свадьбы осталось {period_days} дней!")
else:
    period_days *= -1
    if str(period_days)[-1] == "1":
        print(f"Cо свадьбы прошел {period_days} день!")
    elif str(period_days)[-1] == "2" or str(period_days)[-1] == "3" or str(period_days)[-1] == "4":
        print(f"Cо свадьбы прошло {period_days} дня!")
    else:
        print(f"Cо свадьбы прошло {period_days} дней!")

# print(wedding_time)
