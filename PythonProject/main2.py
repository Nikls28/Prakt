import math
e = int(input("Введите значение e: "))
x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))

f1 = e**x - x - 2 + (1 + x)**x
f2 = (1 - math.tan(x))**(1 / math.tan(x)) + math.cos((x - y))
print(f1)
print(f2)