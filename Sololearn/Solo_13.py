# Простая игра
# При работе с различными объектами и их отношениями широко используется объектная ориентация.
# Основная область применения - разработка игр, где часто используются персонажи с различной функциональностью.
# Рассмотрим это на примере небольшого проекта, показывающем, как классы используются в разработке игр.
# Нам предстоит разработать старый добрый текстовый квест.
# Ниже описана функция, обрабатывающая ввод и делающая простой разбор.

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return
    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())

def say(noun):
    return 'You said "{}"'.format(noun)

verb_dict = {
    "say": say,
    }

while True:
    get_input()

# В приведенном выше фрагменте кода программа принимает ввод пользователя и сопоставляет первое слово с командой
# в verb_dict. В случае совпадения вызывается соответствующая функция.

# Следующим шагом будет создание игровых объектов с помощью классов.
class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)

# Мы создали класс Goblin, который наследует от класса GameObjects.
# Мы также создали новую функцию examine, которая возвращает описание объектов.
# Теперь мы можем добавить новый глагол "исследуй" в словарь и использовать его.
verb_dict = {
    "say": say,
    "examine": examine,
}

# В этом фрагменте кода добавлены дополнительные детали класса Goblin и возможность бороться против гоблинов.
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the Goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here".format(noun)
    return msg