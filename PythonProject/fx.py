x = float(input("Введите значение x: "))

if x >= -3.5:
    fx = 4 * x**2 + 2 * x - 19
elif x < 3.5:
    fx = - (2 * x) / (-4 * x + 1)
else:
    fx = "error"
print("F(x) =", fx)