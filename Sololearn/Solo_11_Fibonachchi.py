# Задача Последовательность Фибоначчи
# Написать программу, которая будет принимать число N и выводить первые N чисел последовательности Фибоначчи

num = int(input())

def fib(x):
    if x == 1:
        # print(x)
        return 1
    elif x == 0:
        # print(x)
        return 0
    else:
        # print(x)
        x = fib(x-1) + fib(x-2)
        return x

def fibonacci(n):
    for i in range(n):
        print(fib(i))

# Костыли==============))))))))))))))
# def fibonacci(n):
#     x = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
#     for i in range(n):
#         print(x[i])

fibonacci(num)
