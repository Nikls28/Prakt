import math
a = int(input("введите число a: "))
b = int(input("введите число b: "))
c = int(input("введите число c: "))

if (a + b > c and b + c > a and c + a > b):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p -c))
    print("Площадь треугольника: ", s)
else:
    s = "Стороны не подходят для треугольника"
    print(s)