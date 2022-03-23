import os
# программа для запуска браузера с введенной строкой сайта

while True:

    sayt = input("Введите адрес сайта:\n ")

    if sayt == 'Завершить':
        break

    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')

    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
        print('elif')

    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)
        print('else')
