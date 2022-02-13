import datetime
import names
import time
import csv
import json

#
# with open('text.txt', 'w') as f:
#     date = str(datetime.datetime.now()) + " "
#     name = names.get_full_name()
#     writer = f.writelines([date, name, "\n"])

# while True:
#     with open('text.txt', 'a') as f:
#         date = str(datetime.datetime.now()) + " "
#         name = names.get_full_name()
#         writer = f.writelines([date, name, "\n"])
#     time.sleep(1)

# with open('text.csv', 'w', newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=['date', 'name'])
#     writer.writeheader()
#     while True:
#         date = str(datetime.date.today())
#         name = names.get_full_name()
#         writer.writerow({"date": date, "name": name})
#         time.sleep(1)

#
# while True:
#     with open('text.csv', 'a', newline="") as f:
#         date = str(datetime.datetime.now())
#         name = names.get_full_name()
#         writer = csv.writer(f, fieldnames=['date', 'name'])
#         writer.writeheader()
#         writer.writerow([date, name])
#     time.sleep(1)

