import math

def solve():
    x = float(input("Введите x: "))
    a = 54 * 10**-3
    
    numerator = 1 + math.cos(a / x)
    denominator = a * x * x * math.sin(a * x)
    fraction = math.sqrt(numerator / denominator)
    
    y = math.log(math.sin(x) * fraction + math.sqrt(math.sin(x) / x))
    
    print(f"Результат для задачи 2: y = {y}")
