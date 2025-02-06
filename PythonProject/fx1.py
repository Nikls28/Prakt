import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))
h = float(input("Введите h: "))

x = a
while x <= b:
    try:
        ctg_x3 = 1 / math.tan(x / 3)
        sin_x = math.sin(x)
        F_x = ctg_x3 + 0.5 * sin_x
        print(f"{x:.2f}\t\t{F_x:.6f}")
    except ZeroDivisionError:
        print(f"{x:.2f}\t\tне определено")
    x += h