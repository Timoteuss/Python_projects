# Кодировщик заголовков.
# Создать файл с названиями книг, каждое на новой строке. Чтобы зашифровать названия книг, нужно взять первые буквы каждого
# слова в названии и объединить их.

with open("Solo_7.txt", 'w') as w:
    w.write("Game of Thrones\nAdventures of Tom Sawyer\nDon Quixote")


with open("Solo_7.txt") as r:
    for line in r.readlines():
        y = line.split()
        z = ""
        for x in y:
            z += x[0]
        print(z)

# Взять первую букву названия книги и количество символов в названии и объединить их.

with open("Solo_7.txt") as r:
    for l in r.readlines():
        if '\n' in l:
            x = str(len(l)-1)
            z = l[0] + x
            print(z)
        else:
            x = str(len(l))
            z = l[0] + x
            print(z)
