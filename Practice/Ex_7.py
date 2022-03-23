# pairs = {
#     1: "apple",
#     "orange": [2, 3, 4],
#     True: False,
#     12: "True",
# }
#
# print(pairs.get("orange"))
# print(pairs.get(7, 42))
# print(pairs.get(12345, "not found"))

# d1 = {'a': 7, 'b': 9}
# d2 = dict([[1, 2],[3, 4],[5, 6]])
# d3 = dict.fromkeys([1, 2, 3, 4, 5], "value")


# d4 = d1.copy()
# print(d1.items()) #возвращает список ключей и значений в кортеже(удобно работать с циклом for)
# print(d1.keys()) #возвращает ключи в словаре в виде списка
# print(d1.values()) #возвращает значения в словаре в виде списка
# d1.update(d2)
# print(d1)

# if 'c' in d1:
#     d1['c']
#
# y = d1.get('c', 'value')
# print(y)
#
# t = d1.pop('a')
# print(t, d1)

price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}
new_price = {}

for i in price:
    new_price[i] = round(price[i] * 0.85, 2) #сделать скидку 15% и округлить до 2 знаков после запятой

print(price)
print(new_price)
x = price.items()
new = {}

for key, value in x:
    print(key)
    print(value)
    new[value] = key

print(new)

for value in price.values():
    print(value)

for key in price.keys():
    print(key)
