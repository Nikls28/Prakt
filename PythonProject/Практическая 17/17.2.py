#Москаленко Н.В.
# №10 - Вычислить среднее арифметическое отрицательных элементов матрицы, стоящих выше главной диагонали. Найти в матрице последнюю по порядку строку с наименьшей суммой элементов. Вывести ее номер.
import random

n = int(input("Введите размер матрицы n: "))

matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

negative_numbers = []
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] < 0:
            negative_numbers.append(matrix[i][j])

if negative_numbers:
    avg_negative = sum(negative_numbers) / len(negative_numbers)
    print(f"\nСреднее арифметическое отрицательных элементов выше главной диагонали: {avg_negative}")
else:
    print("\nНет отрицательных элементов выше главной диагонали.")

min_sum = float('inf')
min_row_index = -1

for i in range(n):
    row_sum = sum(matrix[i])
    if row_sum <= min_sum:
        min_sum = row_sum
        min_row_index = i

print(f"\nПоследняя по порядку строка с наименьшей суммой элементов: {min_row_index + 1} (нумерация с 1)")
