#Москаленко Н.В.
# №2 - Дан файл, содержащий произвольный текст. Определить,чего в нем больше: русских букв или цифр.
import re

# Укажите имя файла с текстом
filename = "text.txt"

# Функция для подсчета русских букв и цифр
def count_russian_letters_and_digits(filename):
    russian_letters = 0
    digits = 0

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Подсчет русских букв
    russian_letters = len(re.findall(r'[а-яА-Я]', text))

    # Подсчет цифр
    digits = len(re.findall(r'\d', text))

    return russian_letters, digits

# Выполнение кода
russian_letters, digits = count_russian_letters_and_digits(filename)

# Вывод результатов
print(f"Количество русских букв: {russian_letters}")
print(f"Количество цифр: {digits}")

if russian_letters > digits:
    print("В файле больше русских букв.")
elif russian_letters < digits:
    print("В файле больше цифр.")
else:
    print("Количество русских букв и цифр одинаково.")