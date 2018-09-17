import atexit
import os
import re

while True:
    try:
        file_path = open(str(input('Введите путь к файлу (например C:\\numbers.txt):')))
        break
    except IOError:
        print('Файл не найден')
file_value = file_path.read()
file_numbers = re.findall('\d+', file_value)
print('Файл содержит значения: ', file_numbers)
# print(type(file_numbers))
print('Сортировка по возрастанию: ', sorted(file_numbers, key=int))
print('Сортировка по убыванию: ', sorted(file_numbers, key=int, reverse=True))


def press_any_key():
    if os.name == "nt":
        os.system("pause")


atexit.register(press_any_key)
