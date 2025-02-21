#Москаленко Н.В.
# №14 - Записать в файл последовательного доступа N действитель­ ных чисел. Найти разность первого и последнего чисел этого фай­ла.
def write_numbers_to_file(filename, numbers):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(f"{num}\n")

def read_and_calculate_difference(filename):
    with open(filename, "r") as file:
        numbers = [float(line.strip()) for line in file]

    if len(numbers) < 2:
        raise ValueError("В файле должно быть минимум два числа")

    return numbers[0] - numbers[-1]

filename = "numbers.txt"
N = int(input("Введите количество чисел: "))
numbers = [float(input(f"Число {i+1}: ")) for i in range(N)]

write_numbers_to_file(filename, numbers)
difference = read_and_calculate_difference(filename)

print(f"Разность первого и последнего числа: {difference}")