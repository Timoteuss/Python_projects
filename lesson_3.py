import time

for k in range(0, 5):

    print('Num =', k)

ll = [0, 1, 2, 3, 4, 5, 'qw', True, False, [12, 'wq'], {'nn': 55}]
count = 0

for i in ll:
    count += 1

    print(count, 'Element of the list - ', i)

dict_data = {
    "name": "Timofey",
    "age": 27,
    "weight": 75,
    "food": {"milk": ["Sirnichki", "milk", "protein", "tvorog"],
             "meat": ["pelmeni", "beef", "sosiska v teste"]},
    "salary": [250, 320, 700, 1100, 1200, 1500, 2000]
    }

key_list = []

for key, value in dict_data.items():


    key_list.append(key)
    print(key, '==', value)

print('========================')
print(key_list)

items_list_1 = []

for ii in range(0, 10):
    items_list_1.append(ii)

print(items_list_1)

count_1 = 0

while True:
    time.sleep(.500)

    input_value = input('Input your value: ')
    nn = int(input_value) * 2

    print("Your value x2 = ", nn)

    if nn > 100:
        break

    print('Hello', count_1)
    count_1 += 1

    if count_1 == 100:
        break
