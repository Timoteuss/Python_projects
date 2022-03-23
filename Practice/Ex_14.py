import shlex

h = ['https:\\www.sait.com', 'https:\\www.something-sait.net', 'https:\\www.left-sait.com',
     'https:\\www.right-sait.com', 'https:\\www.sssaaaiiittt.net', 'https:\\www.another-sait.com']

n = [x.split('\\')[1] for x in h if '.com' in x]   # Генератор списка

print(type(n))

z = (x.split('\\')[1] for x in h if '.com' in x)   # Выражение генератор (у него нет индексов, есть функция next)

print(type(z))
print(next(z))

# def some():
#      list_text = []
#      with open('file.txt', encoding='utf-8') as r:
#           for x in r:
#                list_text.append(x)
#      return list_text
#
# for i in some():
#      print(i.split())

def some():
     with open('file.txt', encoding='utf-8') as r:
          for x in r:
               yield x

# for i in some():
#      print(i.split())

p = some()

print(next(p))
print(next(p))
print(next(p))

for i in p:
     print(i)