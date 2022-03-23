# Работа с файлами.
# Открытие файлов. Аргумент open является путем к файлу. Если файл в текущем каталоге, то можно указать только имя.
# После чтения/записи файл следует закрывать.
my_file = open("../Practice/file.txt")
my_file.close()

# Режим открытия файла используется в качестве второго аргумента.
# Отправка "r" означает открытие в режиме чтения, он используется по умолчанию
# Отправка "w" означает режим записи для перезаписи содержимого файла
# Отправка "а" означает режим добавления нового содержимого в конец файла.
# Добавив "b" в режим - можно открыть файл в двоичном режиме. Используется для нетекстовых файлов(изображения, аудиофайлы)

# # write mode
# open('file.txt', "w")
#
# # read mode
# open('file.txt', "r")
# open('file.txt')
#
# # binary write mode
# open('file.txt', "wb")

# Читать файлы можно с помощью метода read
my_file = open("../Practice/file.txt")
cont = my_file.read()
print(cont)
my_file.close()

# Чтобы прочитать определенный объем файла, можно указать количество байтов в качестве аргумента функции read.
my_file = open("../Practice/file.txt")
print(my_file.read(5))  # Это прочитает первые 5 символов (если один символ составляет 1 байт)
print(my_file.read(7))  # Это прочитает следующие 7 символов
print(my_file.read())   # Это вернет остальную часть содержимого файла
my_file.close()

# Чтобы получить каждую строку в файле, можно использовать метод readlines() для возврата списка
file = open("../Practice/file.txt")

for line in file.readlines():
    print(line)

file.close()

# Если список не нужен, можно просто обойти переменную циклами
file = open("../Practice/file.txt")

for line in file:
    print(line)

file.close()

# Для записи файлов используется метод write. Если файл существует - содержимое будет заменено.
file = open("../Practice/file.txt", 'w')
file.write("This has been written to a file")
file.close()

# Для добавления содержимого в существующий файл, можно открыть в режиме "а"(for "append")
file = open("../Practice/file.txt", 'a')
file.write("\nThe Da Vinci Code")
file.close()

# Метод write возвращает количество байтов записанных в файл в случае успеха
msg = "Hello world!"
file = open("../Practice/file.txt", 'w')
amount_written = file.write(msg)
print(amount_written)
file.close()

# Один из способов всегда закрывать файл - использовать try и finally. Это гарантирует закрытие файла в случае ошибки
try:
    f = open("../Practice/file.txt")
    cont = f.read()
    print(cont)
finally:
    f.close()

# Это можно сделать также, используя конструкцию with. Это создаст временную переменную, которая доступна только в этом блоке
# Файл автоматически закроется в конце конструкции with, даже если возникнет исключение.
with open("../Practice/file.txt") as f:
    print(f.read())
