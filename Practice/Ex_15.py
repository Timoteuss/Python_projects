from dis import dis

def some(x):
    return x/5

var = lambda x: x/5   # Анонимная функция

print(some(7))
print(var(7))

print(dis(some))
print(dis(var))

list_of = [['Adam', 29], ["Jonny", 3*1/12], ['Jess', 25]]

# def s(x):
#     return x[1]
# r = sorted(list_of, key=s)

r = sorted(list_of, key=lambda x: x[1])

print(r)

x = list(filter(lambda x: x[1] > 18, list_of))
print(x)
