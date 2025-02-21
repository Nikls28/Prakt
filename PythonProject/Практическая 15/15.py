#Москаленко Н.В.
# №27 - Из файла f получить файл g, исключив повторные вхожде­ния чисел и сохранив порядок их следования.
input_filename = "f.txt"  # Имя входного файла
output_filename = "g.txt"  # Имя выходного файла

seen = set()
unique_numbers = []

# Читаем входной файл
with open(input_filename, 'r') as f:
    for line in f:
        for number in line.split():
            if number not in seen:
                seen.add(number)
                unique_numbers.append(number)

# Записываем результат в выходной файл
with open(output_filename, 'w') as g:
    g.write(" ".join(unique_numbers))
print("Данные перенесены")