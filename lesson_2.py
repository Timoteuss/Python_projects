

# Ветвления:

mm = 77
aa = 100
cc = 'Text'

if mm == 77 and aa == 100 or cc == 'Text':
    print("The first")
elif mm >= 77:
    print('Hello >= 77')
else:
    print('Hello ELSE 77')

if mm == 77:
    print("The first")

    if aa == 100:
        print("The inner first")

elif mm > 77:
    print('Hello > 77')
else:
    print('Hello ELSE 77')

tx = "Text"
tx1 = "text"

if tx > tx1:
    print("The first")
else:
    print("The Second")

# Циклы

ll = [0, 1, 2, 3, 4, 5, 'qw', True, False, [12, 'wq'], {'nn': 55}]

for i in ll:

    if type(i) == list:
        print('===========', i)
        continue

    print(i)

for yojik in range(2, len(ll)):

    print(ll[yojik])

m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(m[1][2])

stra = 'Hello world!'

print(stra[6])
