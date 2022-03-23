# import tkinter
#
# root = tkinter.Tk()
# root.geometry('800x400')
# root.title('Сколько Тиме и Лизе до дня свадьбы?')
# root.resizable(height=False, width=False)
# font = PhotoImage(file=())
# root.bind('<1>', img)
# Button(root, text='Нажми, чтобы узнать когда это случится', command=img).pack()
# root.mainloop()

def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('Повторите ввод...')
            h = f()
        return h
    return wrapper()

@decor # make = decor(make)
def make():
    enter = float(input('Введите число: '))
    return enter

@decor
def make2():
    enter = float(input('Введите число опять: '))
    return enter

make()
make2()
