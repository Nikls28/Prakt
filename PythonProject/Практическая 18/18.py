from convert import convert

def main():
    number = int(input("Введите натуральное число: "))
    base = int(input("Введите систему счисления (от 2 до 9): "))

    if 2 <= base <= 9:
        result = convert(number, base)
        print(f"Число {number} в {base}-ичной системе: {result}")
    else:
        print("Основание системы счисления должно быть от 2 до 9.")

if __name__ == "__main__":
    main()
