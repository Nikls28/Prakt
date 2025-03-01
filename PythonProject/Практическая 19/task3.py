def solve():
    E = float(input("Введите точность E: "))
    S = 0
    n = 1
    while True:
        term = 1 / (n**2)
        if term < E:
            break
        S += term
        n += 1
    print(f"Результат для задачи 3: S = {S}")
