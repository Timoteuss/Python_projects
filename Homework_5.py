import csv
import names
import random

# Python CSV
#
# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
#
# Создать пустой empty.csv файл.
#
# Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
#
# Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
#
# Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
#
# Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
#
# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
#
# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами
#
# Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
#
# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
#
# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (распределение рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (распределение рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (распределение рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2022 (распределение рандомно)
#
#
# Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

file_path = "C:/Users/Timofey/PycharmProjects/Kurses/text_files/"
csv_file_title = "empty.csv"
file_title = file_path + csv_file_title

file_digits = file_path + "digits.csv"

with open(file_digits, 'w') as f:

        for i in range(0, 151):

                f.write(str(i))
                f.write('\n')

file_names = file_path + "names.csv"

with open(file_names, 'w') as f:

        for n in range(0, 100):

                f.writelines(names.get_first_name())
                f.write("\n")

file_emails = file_path + "emails.csv"

with open(file_emails, 'w') as f:

        for n in range(0, 100):

                f.writelines(names.get_first_name() + str(n) + '@gmail.com')
                f.write("\n")

file_nne = file_path + "nne.csv"

with open(file_nne, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=['Number', 'Name', 'Email'])
        writer.writeheader()
        for i in range(1, 101):

                number = i
                name = names.get_first_name()
                email = f'{name}@gmail.com'
                writer.writerow({"Number": number, "Name": name, "Email": email})

file_digits_2 = file_path + "digits_2.csv"
number_d2 = []
for i in range(10, 311):
        number_d2.append(i)

with open(file_digits_2, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["number"])
        writer.writeheader()
        for i in number_d2:
                writer.writerow({"number": i})

file_names_2 = file_path + "names_2.csv"
name_2 = []
for i in range(1, 401):
        name_2.append(names.get_first_name())

with open(file_names_2, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name"])
        writer.writeheader()
        for i in name_2:
                writer.writerow({"name": i})

file_emails_2 = file_path + "emails_2.csv"
email_2 = []
for i in range(1,401):
        email_2.append(names.get_first_name() + str(i) + str(random.randint(1, 999)) + '@gmail.com')

with open(file_emails_2, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["email"])
        writer.writeheader()
        for i in email_2:
                writer.writerow({"email": i})

file_nne_2 = file_path + "nne_2.csv"
number_n = []
name_n = []
email_n = []
for i in range(1, 451):
        number_n.append(i)
        name_n2 = names.get_first_name()
        name_n.append(name_n2)
        email_n.append(name_n2 + "@gmail.com")

with open(file_nne_2, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Number", "Name", "Email"])
        writer.writeheader()
        for i in range(0, 450):
                writer.writerow({"Number": number_n[i], "Name": name_n[i], "Email": email_n[i]})

date = []
for i in range(0, 50):
        date.append(random.randint(1980, 1991))
for i in range(0,100):
        date.append(random.randint(1991, 2001))
for i in range(0, 150):
        date.append(random.randint(2001, 2011))
for i in range(0, 150):
        date.append(random.randint(2011, 2022))

with open(file_nne_2, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Number", "Name", "Email", "Date"])
        writer.writeheader()
        for i in range(0, 450):
                writer.writerow({"Date": date[i]})



# with open(file_names, 'a', encoding='utf-8') as f:
#
#     # f.writelines(ll)
#     # f.write('\n'.join(ll))
#
#     for n in range(0, 10):
#         for i in ll:
#             # f.write(i)
#             # f.write('\n')
#             w_line = str(n) + '_' + i
#
#             f.writelines(w_line)
#             f.write('\n')