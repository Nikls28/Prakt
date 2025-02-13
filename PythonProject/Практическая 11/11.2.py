#Москаленко Н.В. вариант 11
#В заданной строке удалить все лишние пробелы (не используя встроенные функции).
def remove_all(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

input_string = input("Введите строку: ")
print("Результат:", remove_all(input_string))