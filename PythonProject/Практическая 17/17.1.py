#Москаленко Н.В.
# №10 - Создать квадратную матрицу размером n x n(n вводится с клавиатуры), значение каждого элемента которой вычисляются по формуле
# Подсчитать сумму элементов первого столбца, произведение элементов второй строки и среднее арифметическое элементов матрицы A.
import math

n = int(input("Введите размер матрицы n: "))

A = [[math.sqrt(2 * j) + 1 + math.tan(i) for j in range(1, n + 1)] for i in range(1, n + 1)]

print("\nСформированная матрица:")
for row in A:
    print(row)

sum_first_column = sum(A[i][0] for i in range(n))
print(f"\nСумма элементов первого столбца: {sum_first_column}")

if n > 1:
    product_second_row = math.prod(A[1])
    print(f"Произведение элементов второй строки: {product_second_row}")
else:
    print("Вторая строка отсутствует (n = 1)")

sum_all_elements = sum(sum(row) for row in A)
average = sum_all_elements / (n * n)
print(f"Среднее арифметическое всех элементов матрицы: {average}")
