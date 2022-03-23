# Объект None. Отсутствие значения.
# Объект None возвращается функцией, которая не запрограмированна что-либо возвращать.
def some_func():
    print("Hi")

var = some_func()
print(var)

# Словари. Каждый элемент в словаре выражен в форме key: value
# Попытка сослаться на ключ, которого нет в словаре, возвращает ошибку KeyError
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
# print(ages["LOL"])

# В качестве ключа могут быть использованы неизменяемые объекты immutable.
# Попытка вызвать изменяемый объект (список, словарь и т.п.) в качестве ключа - вызывает TypeError

# bad_dict = {[1, 2, 3]: "one two three"}

# Ключам словаря можно присваивать значения, в том числе и создавая так новые пары ключ: значение
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

# Можно определить есть ли ключ в словаре при помощи in и not in
nums = {1: "one", 2: "two", 3: "three"}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

# Метод get выполняет то же, что и индексация, но если ключ не найден он возвращает другое указанное значение(по умолчанию None)
pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: True,
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

# Кортежи (tuple) являются неизменными. Попытка переназначить значение в кортеже возвращает ошибку TypeError
# Кортежи можно вкладывать друг в друга.
words = ("spam", "eggs", "sausages")
print(words[0])
# words[1] = "cheese"

# Кортежи можно создавать без скобок, просто разделив значения запятыми
my_tuple = "one", "two", "three"
print(my_tuple[0])

# Срезы. Более продвинутый способ получить значения из списка. Для этого нужно индексировать два целых числа.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])  # Подобно аргументам range, второй аргумент не включается в срез.
print(squares[:7])  # Без первого аргумента программа выбирает с начала списка
print(squares[7:])  # Без второго аргумента программа выбирает до конца списка
print(squares[::2])  # Третий параметр задает шаг
print(squares[2:8:3])
print(squares[1:-1])
print(squares[::-1])  # Распространенный способ обратить список - присвоить отрицательное значение шагу
print(squares[7:5:-1])

# Списковое включение - быстрый способ создания списков
cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

# Попытка создать очень обширный список приведет к ошибке MemoryError
# even = [2*i for i in range(10**100)]

# Форматирование строк. Метод format позволяет заменять аргументы строки
numbers = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(numbers[0], numbers[1], numbers[2])
print(msg)
print("{0}{1}{0}".format("abra", "cad"))

# Форматирование строк можно делать с помощью аргументов, которым были присвоены имена
a = "{x}, {y}".format(x=5, y=12)
print(a)

# Функции обработки строк
print(", ".join(["spam", "eggs", "ham"]))  # Объединение последовательности строк с использованием разделителя ", "
print("Hello ME".replace("ME", "world"))  # Замена одной подстроки на другую
print("This is a sentence.".startswith("This"))  # Определяет есть ли подстрока в начале
print("This is a sentence.".endswith("sentence."))  # Определяет есть ли подстрока в конце
print("This is a sentence.".upper())  # Для изменения регистра строки на верхний
print("AN ALL CAPS SENTENCE.".lower())  # Для изменения регистра строки на нижний
print("spam, eggs, ham".split(", "))  # Противоположный join, делает из строки с определенным разделителем список

# Числовые функции
print(min(1, 2, 3, 4, 0, 2, 1))  # Наименьший элемент списка
print(max([1, 4, 9, 2, 5, 6, 8]))  # Наибольший элемент списка
print(abs(-99))  # Расстояние числа от нуля(его абсолютная величина
print(abs(42))
print(round(12.124324234, 2))  # для округления до определенного количества знаков после точки
print(sum([1, 2, 3, 4, 5]))  # для сложения всех чисел в списке

s = min([sum([11, 22]), max(abs(-30), 2)])
print(s)

# Функции списков.
# Функциям all и any можно присваивать список в качестве аргумента. Значение True возвращается если все аргументы True
# Функция enumerate может использоваться для одновременного перебора значений и показателей списка
numb = [55, 44, 33, 22, 11]

if all([i > 5 for i in numb]):
    print("All larger than 5")

if any([i % 2 == 0 for i in numb]):
    print("At least on is even")

for v in enumerate(numb):
    print(v)



# Анализатор текста
#
# def count_char(text,char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count
#
# filename = input("Enter a filename: ")
# with open(filename) as f:
#     text = f.read()
#
# for char in "abcdefghijklmnopqrstvwxyz":
#     perc = 100 * count_char(text, char) / len(text)
#     print("{0} - {1}%".format(char, round(perc, 2)))




# Задача "Самое длинное слово"
# txt = input()
txt = "Rnter a filename and what do you want to do with this differences"
spl = txt.split(" ")
y = []

for i in spl:
    x = len(i)
    y.append(x)
m = max(y)
for i in spl:
    if len(i) == m:
        print(i)
