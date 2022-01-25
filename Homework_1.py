

# 1) Создать переменную типа String
String = 'String'
# 2) Создать переменную типа Integer
Integer = 42
# 3) Создать переменную типа Float
Float = 32.42
# 4) Создать переменную типа Bytes
Bytes = b'Byte'
# 5) Создать переменную типа List
List = [22, 'list', {'dns': '00000'}, [12, 'rrr', 13.4]]
# 6) Создать переменную типа Tuple
Tuple = (14, 12, 55, 789)
# 7) Создать переменную типа Set
Set = set('Hello world')
# 8. Создать переменную типа Frozen set
Frozen_set = frozenset('Hello world!!!')
# 9) Создать переменную типа Dict
Dict = {'key': 'value', 'bla': 'bla-bla-bla'}
#
#
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
x = [String, Integer, Float, Bytes, List, Tuple, Set, Frozen_set, Dict]
for i in x:

    if i != 0:
        print(i, 'Тип данных: ', type(i))
#
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str1 = 'Hello '
str2 = 'world!'
str_sum = str1 + str2

print(str_sum)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(String, Integer)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(String + str(Integer))