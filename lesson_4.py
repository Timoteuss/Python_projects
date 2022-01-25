def bochka(a1, a2, a3, a4=100, a5=200, a6="Tim"):

    var_1 = a1 * 2
    var_2 = a2 * 10
    var_3 = a3 * 3

    result = [var_1, var_2, var_3]

    return var_1, var_3, var_2, a5

get_f1, get_f11, get_f111, get_f1111 = bochka(2, 5, 10, a5=500)

print('get_f1 ==', get_f1)
print('get_f11 ==', get_f11)
print('get_f111 ==', get_f111)
print('get_f1111 ==', get_f1111)

def lochka(*args):

    print(args)

get_f2 = lochka(3, 5, 7)

def sochka(**kwargs):

    print(kwargs)

sochka(b1=3, b2=5, b3=7)

def mochka(salary, *args, **kwargs):

    for k, v in kwargs.items():

        n1 = v * 2

        print("K=", k, 'V=', n1)

    print(salary, args, kwargs)

mochka(1000, 11, 22, 33, 55, 'Mam', b1=3, b2=5, b3=7)



