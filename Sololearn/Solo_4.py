# Исключения
# Они возникают, когда что-то идет не так из-за недействительного ввода или кода.
# Когда возникает исключение программа немедленно останавливается
# Следующий код образует исключение ZeroDevisionError, пытаясь делить 7 на 0.

# num1 = 7
# num2 = 0
# print(num1/num2)

# Распространенные исключения:
# ImportError: ошибка импорта;
# IndexError: список проиндексирован с номером вне допустимого диапазона;
# NameError: используется неизвестная переменная;
# SyntaxError: код не может быть проанализирован должным образом;
# TypeError: функция ввызывается для значения несоответствующего типа;
# ValueError: функция ввызывается для значения правильного типа, но с несоответствующим значением

# Обработка исключений
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print('Done calculation')
except ZeroDivisionError:
    print('An error occurred')
    print("due to zero divizion")

# Конструкция try может иметь множество различных блоков except
# Множественные исключения также могут быть помещены в один блок except

try:
    variable = 10
    print(variable + 'hello')
    print(variable / 2)
except ZeroDivisionError:
    print('Divided by zero')
except (ValueError, TypeError):
    print('Error occurred')

# Конструкция except без указанного исключения будет перехватывать все ошибки.
# Обработка исключений особенно полезна при работе с пользовательским вводом

try:
    word = 'spam'
    print(word / 0)
except:
    print("An error occurred")

# finally после конструкции try/except выполняется в любом случае
try:
    print('Hello')
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

# Конструкция else также может использоваться с конструкцией try/except. Код внутри нее выполняется только, если нет ошибки в try
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

try:
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError:
    print(3)
else:
    print(4)

# Вызов исключений.
# Можно вызывать исключения при условиях. Например при пользовательском вводе. Осуществляется вызов при помощи raise
# Нужно также указать тип вызываемого исключения, например ниже ValueError

# num = 102
# if num > 100:
#     raise ValueError

# Исключения можно вызывать с аргументами для их описания. Так другим разработчикам будет понятнее почему оно вызвано.

# name = '123'
# raise NameError("Invalid name!")

# Утверждения
# Это проверка правильности кода. Выражение проверяется и если оно ложное, вызывается исключение.
# Утверждения создаются с помощью инструкции assert

# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# Программисты размещают утверждения в заголовке функции (проверить правильность ввода), а также после вызова функции
# (чтобы проверить правильность вывода)

# Утверждениям можно давать второй аргумент, который передается в блок AssertionError, выполняемый если утверждение ложно

# temp = -10
# assert (temp >= 0), "Colder than absolute zero!"

# Исключения AssertionError могут быть перехвачены и обработаны, как и любое другое исключение с помощью try/except.
# Если же AssertionError не обрабатывается, этот класс исключений приводит к остановке программы.
