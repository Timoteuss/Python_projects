# n = list(range(10))
# m = []
#
# for i in n:
#     if i == 8:
#         continue
#     m += [i]
#
# else:
#     print(m)

# x = [9, 8, 7, 6, 5]
# x.append(4)
# # добавляет элемент в конец списка
# x.insert(1, 7)
# # добавляет под заданным индексом элемент в список
# print(x.count(7))
# x.sort()
# # сортирует список по возрастанию
# x.reverse()
# # переворачивает список в обратную сторону
# x.pop()
# # удаляет последний элемент списка, либо выбранный под индексом
# x.remove(7)
# # удаляет написанный в скобках элемент
# x.clear()
# # очищает полностью список
# x.extend(['a', 's', 'a'])
# #
# h = x.copy()
# print(h)
#
# print(x)

a = list(range(1, 21))
b = []
c = a.copy()
d = a[1::2]

for i in a:
    if i % 2 == 0:
        b.append(i)
        a.remove(i)

else:
    print(a)
    print(b)

print(c)
print(d)