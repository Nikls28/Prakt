#Москаленко Н.В. вариант 23
#Сформировать квадратную матрицу порядка n (где n – четное число) по заданному образцу:(там картинка)
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    matrix[0][0] = 1
    matrix[0][n - 1] = 1

    matrix[1][0] = 1
    matrix[1][n - 2] = 1
    matrix[1][n - 1] = 1

    for i in range(2, n - 2):
        for j in range(n):
            matrix[i][j] = 1

    matrix[n - 2][0] = 1
    matrix[n - 2][1] = 1
    matrix[n - 2][n - 2] = 1
    matrix[n - 2][n - 1] = 1

    matrix[n - 1][0] = 1
    matrix[n - 1][n - 1] = 1

    return matrix


if __name__ == "__main__":
    n = int(input("Введите чётное число n: "))

    result_matrix = create_matrix(n)

    for row in result_matrix:
        print(*row)