# Функциональное программирование

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

# named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

# lambda
print((lambda x: x**2 + 5*x + 4)(-4))

# map function (функция map принимает функцию и итерируемый объект и применяет к каждому аргументу объекта функцию)
# для использования "map", результат должен быть явно преобразован в список (list)
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# lambda
result = list(map(lambda x: x+5, nums))
print(result)

# Функция filter фильтрует итерируемый объект оставляя только те елементы, которые соответствуют условию (предикату)
# для использования "filter", результат должен быть явно преобразован в список (list)
res = list(filter(lambda x: x%2==0, nums))
print(res)

# Генераторы являются типом итерируемого объекта. Их можно создавать с помощью функций и оператора yield
# Оператор yield используется для определения генератора, заменяя возврат функции без разрушения локальных переменных
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

# Конечные генераторы можно преобразовать в списки
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

def make_world():
    word = ""
    for ch in "spam":
        word +=ch
        yield word
print(list(make_world()))

# Декораторы
def decor(func):
    def wrap():
        print("============")
        func()
        print('============')
    return wrap

# @decor
def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()

# Рекурсия - когда функция обращается к себе. Например:
# Факториал находит произведение всех положительных чисел до этого числа. Например, 5! (факториал 5) = 5*4*3*2*1(120)
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

# Косвенная рекурсия - когда функция вызывает другую функцию, которая вызывает первую. Так с любым кол-ом функций
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))

# *args(элементы становятся доступными в качестве кортежа в теле функции
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# **kwargs аргументы ключевого слова (возвращаются в словарь, где ключ - имя аргумента, а значение - аргумент)
def my_func(x, y, *args, **kwargs):
    print(kwargs)
my_func(2, 3, 4, 5, 6, a=7, b=8)
# a и b являются именами аргументов, которые мы передаем в вызов фунции

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
print(power(2, 3))

# Функция для записи текста в обратном направлении в столбик по буквам
def spell(txt):
    x = reversed(txt)
    for i in x:
        print(i)
        continue
txt = input("Введите текст: ")
spell(txt)
