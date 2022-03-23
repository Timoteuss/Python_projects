# FizzBuzz
n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print('SoloLearn')
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        print('Solo')
    elif x % 5 == 0:
        print('Learn')
    else:
        print(x)


# Конвертер градусов Цельсия в градусы Фаренгейта
celsius = int(input())

def conv(c):
    return 9/5 * c + 32

fahrenheit = conv(celsius)
print(fahrenheit)
