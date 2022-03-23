import os

list_paths = []

for adress, papka, file in os.walk('C:\\Users\Timofey\PycharmProjects\Kurses\Practice'):
    for i in file:
        full_path = os.path.join(adress, i)
        list_paths.append(full_path)

# 'r' открыть для чтения (по умолчанию)
# 't' открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи, содержимое файла удаляется. Если файла нет - создается новый
# 'a' открыть для дозаписи в конец файла. Если файла нет - создается новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'

# r = open('text.txt', 'w')
# for x in list_paths:
#     r.write(x + '\n')
#
# r.close()


# r = open('text.txt')
#
# for i in r:
#     if '3.py' in i:
#         print(i)
# r.close()



# r = open('e.exe', 'rb')
# y = open('Kopia_e.exe', 'wb')
#
# while True:
#     var = r.read(1024*1024)
#     print(var.__sizeof__())
#     y.write(var)
#
# print('Контроль')
# r.close()
# y.close()

r = open('text2.txt', 'w', encoding='utf-8')
r.write('Строка текста под номером 1')
print(r)

r.close()


h = open('text2.txt', encoding='utf-8')
print(h.read())

r.close()