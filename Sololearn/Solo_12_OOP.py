import random

# Ранее мы ознакомились с двумя парадигмами программирования:
# - императивной (использование инструкций, циклов и функций в качестве подпрограмм)
# - функциональной (использование чистых функций, функций высшего порядка и рекурсий).
# Ещё одна очень важная парадигма -
# Объектно-ориентированное программирование(ООП). Объекты создаются с помощью классов.
# Классы.
# Класс описывает объект, но является независимым от него. Класс - это экземпляр, описание или определение объекта
# Можно создавать класс в качестве образца для создания различных объектов.
# Классы оформляются с помощью ключевого слова class и блока с отступом, содержащим методы класса(функциями)

# Класс с именем Cat имеет два атрибута color и legs. Затем класс используется для создания 3 отдельных объектов,
# принадлежащих этому классу
class Cat:
    def __init__(self, color, legs):   #метод __init__ является конструктором класса
        self.color = color  # Метод __init__ принимает два аргумента и присваивает их объекту в качестве атрибутов.
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)
# Метод __init__ - самый важный метод класса. Он выхывается, когда создается экземпляр(объект) класса;
# имя класса используется как функция.
# Все методы должны иметь "self" в качестве своего первого параметра; хотя "self" непосредственно не передается,
# Python добавляет инструкцию "self" в список сам; также не нужно включать "self", когда вызываешь методы.
# В пределах определения метода, инструкция "self" относится к экземпляру класса, вызывающему метод.
# Экземпляры класса берут атрибуты - фрагменты связанных с ними данных.
# В нашем примере, экземпляры класса Cat имеют атрибуты color и legs. Их можно получить, указав точку и имя атрибута
# после экземпляра. Так внутри метода __init__ с помощью self.attribute можно задать начальное значение атрибутов экземпляра

# Можно использовать и другие методы, расширяющие функциональность классов. Первый параметр всех методов - self
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

# Попытка вызова атрибута экземпляра, который не был определен вызывает AttributeError.
# Такая же ошибка выдается при попытке вызова несуществующего метода
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
# print(rect.color)

# Наследование
# Наследование представляет способ передачи функциональности между классами. Подкласс наследуется из суперкласса.
# Допустим у нас есть несколько классов: Cat_1, Dog_1, Rabbit и другие. Некоторые методы этих классов будут уникальными:
# только Dog_1 будет иметь метод bark (лай). А другие методы будут одинаковыми: все классы имеют color и name.
# Наследование оформляется путем заключения в круглые скобки имени суперкласса, следующего за именем класса
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

# Класс, наследующий атрибуты или методы другого класса, назыается подклассом.
# Класс, из которого наследуются атрибуты или методы, называется суперклассом.
# Если наследуемый класс имеет такие же методы или атрибуты, что и класс-наследник, то класс-наследник переопределяет их
class Wolf:  # Суперкласс
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grr...")

class Dog_2(Wolf):  # Подкласс
    def bark(self):
        print("Woof...")

husky = Dog_2("Max", "grey")
husky.bark()

# Наследование может быть также непрямым. Один класс может наследовать от другого класса, который наследует от третьего.
# Круговое наследование, тем не менее, не поддерживается.
class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_method()
c.third_method()

# Функция super - полезная функция наследования, которая указывает на родительский класс.
# Она предназначена для поиска метода по его имени в суперклассе объекта.
class A1:
    def spam(self):
        print(1)

class B1(A1):
    def spam(self):
        print(2)
        super().spam()  # Эта строчка вызывает метод суперкласса spam

B1().spam()

# Магические методы (дандеры) имеют двойное подчеркивание в начале и в конце имени.
# Они предназначены для создания специальной функциональности. Применяются часто для переопределения операторов.
# Перегрузка операторов позволяет использовать "+" и "*"
# Метод __add__ определяет поведение для оператора "+" в классе. После определения можно сложить два объекта класса.
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

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

a = BankAccount(1024)
b = BankAccount(42)
result = a + b
print(result.balance)

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
# В приведенном выше примере мы определили операцию разделения для класса SpecialString

# Python также предоставляет магические методы для сравнения
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
# Если __ne__ не реализован, он возвращает обратное от __eq__. Других отношений между операторами сравнения нет.

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
spam > eggs  # Пример того, как переопределяя операторы можно задавать им любое специальное поведение

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
# Функция индексации также может возвращать случайный элемент в заданном диапазоне со списка, если сделать так:
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

# Жизненный цикл объекта.
# Создание, использование и уничтожение
# Первый этап ЖЦО - определение класса, к которому он принадлежит.
# Следующий этап - инстанцирование экземпляра, когда вызывается метод __init__. Выделяется память для хранения экземпляра.
# Непосредственно перед этим вызывается метод класса __new__. Это действие, как правило, отменяется очень редко.
# После этого объект готов к использованию. С ним можно взаимодействовать: вызывать функции и использовать его атрибуты.
# Когда объект больше не нужен, он может быть уничтожен.

# Когда объект уничтожается, выделенная для него память освобождается и может использована для других целей.
# Уничтожение объекта происходит, когда кол-во ссылок на него достигнет нуля. Кол-во ссылок - это число переменных и пр.
# Если на объект ничего не ссылается, ничто не взаимодействует с ним, так что его можно удалять.
# В некоторых случаях, два(или более) объекта могут ссылаться друг на друга, и также могут быть удалены.
# Инструкция del(метод __del__) уменьшает число ссылок на единицу, что часто приводит к его удалению.
# Процесс удаления ненужных объектов называется сборкой мусора.
# Когда объекту присваивается новое имя или его включают в контейнер(кортеж, список, словарь), кол-во ссылок растет(+1)
# Число ссылок объекта уменьшается, когда он удаляется инструкцией del, одна из его ссылок бела переназначена,
# или когда его ссылка указывает на элемент за рамками доступного диапазона.
# Когда кол-во ссылок объекта достигает нуля, Python автоматически удаляет его.
# Пример:
a = 42  # Create object <42>
b = a  # Increase ref. count of <42>
c = [a]  # Increase ref. count of <42>

del a  # Dicrease ref. count of <42>
b = 100  # Dicrease ref. count of <42>
c[0] = -1  # Dicrease ref. count of <42>
# Низкоуровневые языки вроде С не имеют такого автоматизированного управления памятью.

# Сокрытие данных.
# Одно из ключевых понятий ООП - это инкапсуляция = упаковка в целях простоты использования связанных переменных
# и функций в один объект(экземпляр класса).
# Сокрытие данных - близкое к инкапсуляции понятие, суть которого в том, что детали реализованного класса должны быть
# скрыты, и чистый стандартный интерфейс должен быть представлен тем, кто будет использовать класс.
# В других языках прог. это достигается с использованием частных методов и атрибутов, которые закрывают доступ извне.
#
# Условно частные методы и атрибуты оформляются с единым подчеркиванием в начале имени.
# Это частные методы, которые не должны взаимодействовать со внешей частью программы. Но это правило условно.
# Реальная особенность этих методов в том, что "from module_name import *" не будет импортировать переменные,
# которые начинаются с единого подчеркивания.

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)  # Этот атрибут помечен как частный, но внешний код может получить доступ к нему

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):  # Этот маг.метод возвращает экземпляр в виде строки
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Строго частные методы и атрибуты оформляются с двойным подчеркиванием в начале имени. Таким образом их имена
# искажаются, и внешняя часть программы не может получить к ним доступ. Но это делается не для того, чтобы обеспечить
# их частность, а чтобы избежать ошибок, если где-либо есть подклассы, которые имеют методы или атрибуты с такими же
# именами. Методы с искаженными именами всё же могут быть вызваны извне, но по другим именам.
# Метод __privatemethod класса Spam может быть вызван извне по имени _Spam__privatemethod.
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)  # Python защищает члены класса: автоматически включает имя класса в их имена
# print(s.__egg)

# Методы класса.
# Методы объектов вызываются экземпляром класса, который затем передается в параметр метода self.
# Методы класса несколько другие: они вызываются классом, который передается параметру cls метода.
# Чаще всего это используется в фабричных методах: создается экземпляр класса, при этом используются иные параметры,
# чем те, которые обычно передаются в конструктор класса. Методы класса оформляются с декоратором classmethod.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):   #new_square - метод класса и вызывается для класса, а не для экземпляра класса
        return cls(side_length, side_length)  # Он возвращает новый объект класса cls

square = Rectangle.new_square(5)
print(square.calculate_area())
# Практически параметры self и cls используют по традиции.

# Статические методы. Они подобны методам класса, но не получают доп. аргументов; они аналогичны обычным функциям класса
# Помечаются декоратором @staticmethod
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
# Статические методы ведут себя как обычные функции, за исключением того, что их можно вызывать экземпляром класса


# Свойства
# В свойствах можно настроить доступ к атрибутам экземпляра. Создается путем помещения декоратора @property перед
# методом: при вызове атрибута экземпляра с таким же именем, что и у метода, вместо него будет вызван метод.
# Один из распространенных способов их применения - присвоение атрибуту свойства "только для чтения".

class Pizza1:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza1 = Pizza1(['cheese', 'tomato'])
print(pizza1.pineapple_allowed)
# pizza1.pineapple_allowed = True

class Person:
    def __init__(self, age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False

# Свойства также могут быть установлены путем определения функций setter/getter.
# Функция setter устанавливает значение соответствующего свойства, а getter - возвращает значение.
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


