import os

h = [9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 5, -2]

# Генераторы списков, множеств, словарей

newh = []
for x in h:
    newh.append(x*2)
print(newh)

n = [x*2 for x in h]
z = {x*2 for x in h}
f = {x: x*2 for x in h}

print(n)
print(z)
print(f)

g = [x for x in h if x % 2 == 0 and x > 0]
print(g)
print(type(g))

# g1 = [os.path.join(z, i) for z, x, c in os.walk('C:\\') for i in c if '.txt' in i]
# print(g1)

price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d)