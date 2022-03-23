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
# Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
#
# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
#
# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами
#
# Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
#
# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
#
# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)
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

file_emails = file_path + "emals.csv"

with open(file_emails, 'w') as f:

        for n in range(0, 100):

                f.writelines(names.get_first_name()+ str(n) +'@gmail.com')
                f.write("\n")

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