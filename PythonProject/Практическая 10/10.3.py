#Москаленко Н.В. вариант 23
#Сформировать двухмерный массив и удалить из него все столбцы, в которых встречается заданное число.
from random import randint

a = 5
b = int(input("Введите число для поиска в столбцах: "))
mas = [[randint(1, 10) for j in range(a)] for i in range(a)]

print("Исходная матрица:")
for row in mas:
    print(row)

columns_to_delete = []
for j in range(a):
    for i in range(a):
        if mas[i][j] == b:
            columns_to_delete.append(j)
            break


columns_to_delete = list(set(columns_to_delete))
columns_to_delete.sort(reverse=True)


for col_index in columns_to_delete:
    for row in mas:
        del row[col_index]

print("\nМатрица после удаления столбцов с числом", b, ":")
for row in mas:
    print(row)