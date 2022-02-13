text = input("Введите текст:")
word = input("Введите слово, наличие которого нужно проверить в тексте:")


def search(a, b):
    run = a.split()
    if b in run:
        print("Word found")
    else:
        print("Word not found")

search(text, word)
