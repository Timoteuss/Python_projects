# a = 5
# b = '55'
# c = int(b)
# print(a, b, c, sep='\n')
# j = {"name": 'Timothy',
#      'age': 27,
#      'salary': 1500}
#
# d = [a, b, c, 5, True, [7, 'dsfsdf', 14], j]
#
# for i in d:
#     print(i)
#
# print(d[::-1])
# ll = []
# for i in d:
#     if type(i) == dict:
#         for k, v in i.items():
#             if type(i) == int:
#                 print(k, v)
#                 ll.append(i)
#     elif type(i) == int:
#         print(i)
#         ll.append(i)
#     elif type(i) == list:
#         for z in i:
#             if type(z) == int:
#                 print(z)
#                 ll.append(z)
#
# print(ll)

# Есть список с рус.буквами:
# list1 = (а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я)
# на основании этого списка создать список, в котором будут цифры от первой буквы до размера списка с буквами.
# list2 = (1, ..., длина(list1))
# Проитерировать эти списки таким образом, чтобы на выходе получить массив,
#  в котором идет чередование сперва четная цифра потом буква по порядку,
# когда закончатся четные, добавляем нечетные и буквы продолжаются по порядку. Повторений быть не должно!
# Пример: [2, а, 4, б, 6, в....3, с, 5, т и т.д.]
list1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
list2 = []
for i in range(len(list1)):
    list2.append(i+1)
print(list2)

qq = []
zz = []
for t in list2:
    if t%2 == 0:
        gg.append(t)
    else:
        zz.append(t)
cc = []
for x in range(len(list1)):

    for y in range(len(list1)):
        if (list2[y]) % 2 == 0 and (list2[y]) > 0:
            cc.append(list2[k])
            cc.append(list1[x])
            list2[k]


print(cc)


