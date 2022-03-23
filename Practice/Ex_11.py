import sys


#
# while True:
#     try:
#         enter = float(input('Введите число: '))
#         print(100/enter)
#         # break
#
#     except ValueError:  #Исключение
#         print('Вы ввели не число!!!')
#
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!!!")
#
#     else:
#         print("Пользователь молодец с первого раза!")
#
#     finally: #Выполняется всегда, даже когда выскактвает ошибка
#         print('Вывод finally')
#
# print('Всё Ok')

url_list = ['text.txt', "text2.txt", 'text25.txt', 'text3.txt']

list_defect = []
list_info = []

# try:
#     for url in url_list:
#         try:
#             r = open(url)
#             list_info.append(r.read())
#             print('здесь')
#         except Exception:
#             list_defect.append(url)
#             print('тут')
#             sys.exit()
#             continue
#
# finally:
#     r = open('save.txt', 'a')
#     for i in list_info:
#         r.write(i)
#     r.write(str(list_defect))
#     r.close()
#     print('Я всё записал, несмотря ни на что')


with open('file.txt', 'a') as r:
    r.write('something' + '\n')
    r.write('что-то')

print("It's Ok")