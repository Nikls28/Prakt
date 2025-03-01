import math

def solve():
    x = float(input("Введите x: "))
    y = math.sin(x) + abs(x**2 + 1)**3 - math.sqrt(x**2 / abs(x**2 + 5))
    print(f"Результат для задачи 1: y = {y}")