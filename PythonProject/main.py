import math
x = int(input("Введите значение переиенной x: "))
b = int(input("Введите значение переиенной b: "))
z = int(input("Введите значение переиенной z: "))

num1 = ((x + 2) / (b - 3)) - (1 / (z**3 - 2))
num2 = (x + b**2 + 3 * z)/(2 - 5 * x * b)
k= abs(num1) + num2
print("k =",k)