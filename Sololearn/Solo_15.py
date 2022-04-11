import re
# Регулярные выражения(РВ).
# Это мощное средство для работы со строками. Они представляют собой предметно-ориентированный язык(ПОЯ) и доступны
# как библиотека в большенстве языков программирования. Главным образом используются для выполнения двух задач:
# - чтобы проверить, соответствует ли строка определенному набору символов (например, имеет ли строка формат адреса
#   электронной почты)
# - Когда нужно выполнить замену внутри строки (например исправить правописание слова во всех его упоминаниях.
# ПОЯ - своего рода узкоспециализированные мини-языки программирования. На ряду с регулярными выражениями широко
# используется язык SQL. Кроме них есть частные ПОЯ, которые создаются компаниями под конкретные цели.

# Регулярные выражения в Python создаются с использованием модуля re, входящего в стандартную библиотеку.
# После того как вы определили регулярное выражение, с помощью функции re.match можно определить, есть ли совпадение
# в начале строки. Если совпадение не найдено, match возвращает объект совпадения; в противном случае - None.
# Во избежание путанницы при работе с регулярными выражениями, мы будем использовать "сырые" строки r"выражение".
# Сырые строки ничего не экранируют, поэтому с регулярными выражениями так легче работать.

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")
# В примере выше программа проверяет, совпадает ли строка с набором символов "spam".
# Мы использовали простое слово, но также используются различные символы, которые имеют специальное значение в РВ

# Для поиска совпадений используются и другие функции, такие как re.search и re.findall.
# Функция re.search используется для поиска набора символов в любом месте строки.
# Функция re.findall возвращает список всех подстрок с искомым набором символов.
# Функция re.finditer делает то же, что и re.findall, за исключением того, что возвращает итератор, а не список

if re.match(pattern, "eggspamsausagesspam"):  # Функция не найдет совпадений, т.к. ищет в начале строки
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagesspam"):  # Функция найдет совпадение в строке
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagesspam"))
print(re.finditer(pattern, "eggspamsausagesspam"))

# Поиск с регулярными выражениями возвращает объект с несколькими методами, содержащими информацию об объекте.
# Это такие методы, как group, возвращающий совпавшую строку, start и end, возвращающие начальную и конечную позицию
# первого совпадения, и span, возвращающий начальную и конечную позицию первого совпадения в виде кортежа.

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

# Один из самых важных методов re, используемых в регулярных выражениях, метод sub.
# Синтаксис:
# re.sub(pattern, repl, string, count=0)
# Этот метод заменяет все упоминания набора символов в строке на repl: заменяются все упоминания, если не установлено
# ограничение count. Метод возвращает новую версию строки.
str = 'My name is David. Hi David'
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

# Метасимволы
# Именно благодаря использованию метасимволов регулярные выражения эффективнее обычных строковых методов. Они позволяют
# выражать с помощью регулярных выражений такие сложные условия, как "одно или несколько повторений гласных".
# Существование метосимволов несколько усложняет создание регулярных выражений, состоящих из обычных символов,
# являющихся также метасимволами, например, $. В таких случаях метасимволы необходимо экранировать.
# Хотя такой способ также может создать проблемы, так как обратные косые черты также имеют функцию экранирования в коде
# Python. По этой причине может потребоваться три или четыре бэкслеша в строке.
# Чтобы этого не делать, можно использовать "сырую" строку, т.е. обычную строку, начинающуюся с "r"
str = r"I am \r\a\w!"
print(str)

# Первый метасимвол, с которым мы познакомимся - .(точка). Точка означает любой символ, исключая символ новой строки.

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

# Далее рассмотрим метасимволы ^ и $. Они указывают на начало и конец строки соответственно.
print("=========================")
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stringray"):
    print("Match 3")
# Набор символов "^gr.y$" означает, что строка должна начинаться с gr, в середине может быть любой символ и в конце y.

# Классы символов
# Классы символов предназначены для поиска конкретного символа из набора инструментов. Класс символов создается путем
# заключения искомых символов в квадратные скобки.
print("=========================")
pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")
# При поиске с набором [aeiou] будут найдены все строки, содержащие хотя бы один символ из набора.

# Классы символов могут также использоваться в заданном диапазоне. Вот несколько примеров:
# Класс [a-z] - поиск любой строчной буквы
# Класс [G-P] - поиск любого символа верхнего регистра от G до P
# Класс [0-9] - поиск любой цифры.
# Класс может состоять из больше, чем одгого диапазона. Например класс [A-Za-z] означает поиск любой буквы английского
# алфавита верхнего или нижнего регистра.
print("=========================")
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "lab"):
    print("Match 3")
# Набор символов совпадает со строками, которые содержат две прописных буквы с последующей цифрой

# Чтобы инвертировать класс символов, нужно поместить ^ в начало определения класса. Эта команда ищет любой символ,
# кроме символов класса. Другие метасимволы, такие как $ и . не имеют никакого специального значения в классах символов.
# Метасимвол ^ не имеет специального значения, если он не является первым символом класса.
print("=========================")
pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
# Набор символов [^A-Z] исключает строки с текстом в верхнем регистре. Чтобы класс символов был инвертирован, символ ^
# должен быть внутри скобок

# Среди других метасимволов: *,+,?,{ и }. С их помощью задается число упоминаний. Метасимвол * означает "ноль или более
# упоминаний объекта поиска". Это команда найти как можно больше упоминаний. "Объект поиска" указывается в скобках; им
# может быть один символ, класс или группа символов.
print("=========================")
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")
# Здесь будут найдены строки, начинающиеся с комбинации "egg", за которой следует (или нет) неограниченное число
# упоминаний "spam".

# Метасимвол + очень похож на * с тем отличием, что он означает "одно(или более) упоминание".
print("=========================")
pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "ggggggggggggggggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")
# Подсуммируем:
# * означает ноль или более упоминаний предшествующего выражения
# + означает одно (или более) упоминание предшествующего выражения

# Метасимвол ? означает "ноль повторений или одно повторение"
print("=========================")
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")

if re.match(pattern, "ice--cream"):
    print("Match 5")

# Фигурные скобки можно использовать для поиска числа упоминаний между двумя числами.
# Выражение {x,y} означает "упоминание объекта поиска между x и y".
# Следовательно, {0,1} - то же самое, что ?. Если первое число отсутствует, программа считает, что это число ноль.
# Если второе число отсутствует, программа будет искать до бесконечности
print("=========================")
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")
# 9{1,3}$ соответсвует строкам с 1-3 девятками.

#Группы
# Группа создается путем заключения части регулярного выражения в круглые скобки. Это означает, что группа может быть
# задана в качестве аргумента метасимволам, таким как * и ?