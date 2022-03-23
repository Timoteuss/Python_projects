import time


# t = {1, 2, 3, (4, 5), 'a', 't', 3}


# def f(*args):
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#     return list_new
#
# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))
#
# start = time.time()
# f(z, x, c)
# stop = time.time() - start
# print(stop)
#
# start2 = time.time()
# r = set(z)
# t = r.union(set(x), set(c))
# stop2 = time.time() - start2
# print(stop2)

#
# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}
# z.add(6) # добавить элемент во множество (если добавить существующий - ничего не изменится)
# z.discard(6) # удалить элемент из множества (если такого элемента нет - ничего не произойдет)
# z.remove(3) # удалить элемент из множества (если такого элемента нет - выскочит ошибка)
# y = z.union(x) #объединяет множество уникальными значениями
# z.update(x) #объединяет множество уникальными значениями
# q = z.intersection(x) #показывает общие элементы из разных множеств
# w = z.difference(x) #показывает какие элементы в списке z не встречаются в множестве x
#
# print(w)

new = set()

r = open('text.txt')
new.update(set(r.read().split()))
r.close()