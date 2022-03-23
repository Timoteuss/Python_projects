import random

# Классы
# Класс описывает, каким будет объект. Может быть описан как шаблон объекта, описание или определение
# Класс с именем Cat имеет два атрибута color и legs
class Cat:
    def __init__(self, color, legs):   #метод __init__ является конструктором класса
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):  #У классов могут быть и другие методы. Они должны иметь self в качестве первого параметра.
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi from " + self.name)

s1 = Student("Amy")
s1.sayHi()

# Наследование
# Наследование представляет способ передачи функциональности между классами. Подкласс наследуется из суперкласса
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat_1(Animal):
    def purr(self):
        print("Purr...")

class Dog_1(Animal):
    def bark(self):
        print("Woof!")

booldog = Dog_1("Booldog", "brown")
print(booldog.color)
booldog.bark()

class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(2)
        super().method()  # super - функция для нахождения метода в родительском классе (суперклассе)

B().method()

# Магические методы (дандеры) имеют двойное подчеркивание в начале и в конце имени
# Перегрузка операторов позволяет использовать "+" и "*"
# Метод __add__ определяет поведение для оператора "+" в классе. После определения можно сложить два объекта класса
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# __add__ for +
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
# Если магический метод не реализован то вызывается он при помощи добавления r.
# Например, в A() ^ B(), если А не реализует маг.метод будет оцениваться как B().__rxor__(A())


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# Python также предоставляет магические методы для сравнения
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
# Если __ne__ не реализован, он возвращает обратное от __eq__.

class SpecialString1:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString1("spam")
eggs = SpecialString1("eggs")
spam > eggs

# Есть маг.методы, которые заставляют классы вести себя как контейнеры
# __len__ для len()
# __getitem__ для индексирования
# __setitem__ для присвоения индексированных значений
# __delitem__ для удаления индексированных значений
# __iter__ для итерации по объектам (например в циклах for)
# __contains__ для in
# Есть и другие маг.методы. Например:
# __call__ для вызова объекта в качестве функции
# __int__, __str__ и подобные для преобразования объектов во встроенные типы

# Можно переписать функции так, чтобы они возвращали случайное число в диапазоне, вместо конкретных
class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

# Скрытие данных
# Инкапсуляция подразумевает упаковку связанных переменных и функций в экземпляр класса
# Слабо приватные методы имеют одинарное подчеркивание в начале
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):   # Этот метод для строкового представления экземпляра
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Строго приватные методы и атрибуты имеют двойное подчеркивание в начале своего имени
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg)  # Python защищает эти члены, изнутри изменяя имя для включения имени класса

# Методы класса
# В отличие от методобов объектов - вызываются классом, который передается в параметр cls метода
# Методы класса помечаются декоратором classmethod

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):   #new_square - метод класса и вызывается на классе, а не на экземпляре класса
        return cls(side_length, side_length)  # Он возвращает новый объект класса cls

square = Rectangle.new_square(5)
print(square.calculate_area())


# Статические методы. Они подобны методам класса, но не получают доп. аргументов. Помечаются декоратором @staticmethod
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onion", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
# Статические методы ведут себя как обычные функции, за исключением того, что их можно вызывать из экземпляра класса


# Свойства
# Это способ настройки доступа к атрибутам экземпляра. Создается путем помещения декоратора @property
class Pizza1:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza1 = Pizza1(['cheese', 'tomato'])
print(pizza1.pineapple_allowed)
# pizza1.pineapple_allowed = True

# Свойства также могут быть установлены путем определения функций setter/getter.
# Функция setter устанавливает значение соответствующего свойства, а getter - получает значение
# Чтобы определить setter/getter, нужно использовать декоратор с тем же именем, что и у свойства, с ключевым словом после точки

class Piiza2:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza2 = Piiza2(['cheese', 'tomato'])
print(pizza2._pineapple_allowed)
pizza2.pineapple_allowed = True
print(pizza2.pineapple_allowed)

