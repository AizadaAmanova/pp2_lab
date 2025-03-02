import os

path = input("Введите путь: ")

if os.path.exists(path):
    print("Путь существует!")
    directory, filename = os.path.split(path)  # Разбиваем путь
    print("Папка:", directory)
    print("Файл:", filename if filename else "Это директория")
else:
    print("Путь не существует!")
