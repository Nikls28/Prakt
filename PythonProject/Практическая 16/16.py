#Москаленко Н.В.
# №2 - Список A содержит N элементов, значения которых не определены. Организуйте запрос: «Сколько элементов списка следует заполнить?» Заполните список заданным числовым значением znach. Назначение функции: 
# заполнение заданного числа элементов заданным значением. Оформите созданную функцию в виде программного модуля и подключите его к основной программе.
N = int(input("Сколько элементов списка следует заполнить? "))

znach = int(input("Введите числовое значение для заполнения списка: "))

A = [znach] * N

print("Полученный список:", A)
