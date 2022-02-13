import csv
import json

users = {}

users = {1: 'Vadim',
         2: 'Irina',
         'name': 'Alex'}

users_2 = {1: 'Vadim',
           2: 'Irina',
           3: ['Alex', 'Olga', 'Victor']}

users_3 = {1: 'Vadim',
           2: 'Irina',
           3: users}

users_4 = {1: 'Vadim',
           2: 'Irina',
           3: {'name': 'George',
               'age': 30,
               'height': 178,
               'family': {'children': ['Anna', 'Alex'],
                          'wife': 'Vanessa'}}}

print(users_4)

item_1 = users_4[3]['family']['children'][0]

print(item_1)
